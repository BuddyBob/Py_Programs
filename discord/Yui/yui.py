import discord
import random
import sqlite3
import traceback
from urllib import request
import json
from discord.ext import  commands, tasks
from itertools import cycle
from keep_alive import  keep_alive
client = commands.Bot(command_prefix = '.')

status = cycle(['Eating Kids','Hurting myself','Being a bully','Making People Angry'])
conn = sqlite3.connect('games.db')
c = conn.cursor()




#loop status
@tasks.loop(minutes = 2)
async  def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

#Connect Bot
@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready')
#error
# @client.event
# async  def on_command_error(ctx,error):
#     if isinstance(error,commands.CommandNotFound):
#         await ctx.send(f'No such command')



#ping
@client.command()
async def ping(ctx):
    print(ping)
    await ctx.send('Pong! '+str(round(client.latency * 1000))+'ms')
@client.command()
async def chill(ctx):
    await ctx.send('chill')

#8ball
@client.command(aliases = ['8ball'])
async def _8Ball(ctx,*,question:str):
    respond = ['As I see it, yes.'
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predict now.',
            ''
            'Concentrate and ask again.',
            'Don’t count on it.',
            'It is certain.',
            'It is decidedly so.',
            'Most likely.',
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'Outlook good',
            'Reply hazy, try again.',
            'Signs point to yes.',
            'Very doubtful.',
            'Without a doubt.',
            'Yes.',
            'Yes – definitely.',
            'You may rely on it.']
    await ctx.send(f'Question:{question}\nAnswer:{random.choice(respond)}')
@_8Ball.error
async  def _8Ball_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all required arguments \n(8ball,question:str)')


#clear 
@client.command()
async def clear(ctx,amount=10):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'You cleared |{amount}| messages from {ctx.channel}!')

#kick
@client.command()
@commands.has_any_role('629862910285447169','776196644169187389','775844888574164993')
async def kick(ctx, member:discord.Member,*,reason=None):
    await member.kick(reason=reason)

#ban
@client.command()
@commands.has_any_role('629862910285447169','776196644169187389','775844888574164993')
async def ban(ctx, member:discord.Member,*,reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')



@client.command()
async def loginDog(ctx):
    try:
        c.execute("""CREATE TABLE dogs(
                    name text,
                    id integer,
                    money integer,
                    dogs integer,
                    energy integer
                )""") 
    except:
        pass

    def ui(client_name,client_id):
        c.execute("SELECT * FROM dogs WHERE name='{}' AND id='{}'".format(client_name,client_id))
        user_info = c.fetchone()
        return user_info


    client_name = ctx.author.name
    client_id = ctx.author.id
    #fetch all 
    with conn:
        c.execute("SELECT * FROM dogs")
        print('Database: '+str(c.fetchall()))
    
    #select all info from user; stored in user_info; print
    user_info = ui(client_name,client_id)
    print('user info:',user_info)
    if user_info == None:
        money = 0
        dogs = 5
        energy = 3
        c.execute("INSERT INTO dogs VALUES (:name,:id,:money,:dogs,:energy)",{'name':client_name,'id':client_id,'money':money,'dogs':dogs,'energy':energy})
        conn.commit()
        user_info = ui(client_name,client_id)
    embed = discord.Embed()
    embed.set_author(name=f"__ Dog Stats - {client_name} __")
    embed.add_field(name="Balance: " , value=user_info[2],inline=True)
    embed.add_field(name="Dog Count: " , value=user_info[3],inline=True)
    embed.add_field(name="Energy: " , value=user_info[4],inline=True)
    await ctx.send(embed = embed)
    @client.command(aliases = ['$'])
    async def stats(ctx):
        user_info = ui(client_name,client_id)
        embed = discord.Embed()
        embed.set_author(name=f"__ Dog Stats - {client_name} __")
        embed.add_field(name="Balance: " , value=user_info[2],inline=True)
        embed.add_field(name="Dog Count: " , value=user_info[3],inline=True)
        embed.add_field(name="Energy: " , value=user_info[4],inline=True)
        await ctx.send(embed = embed)
    @client.command()
    async def work(ctx):
        user_info = ui(client_name,client_id)
        e = user_info[4]
        moneyOpt = [200] * 80 + [500] * 28 + [1000] * 5
        if e >= 1:
            gain = random.choice(moneyOpt)
            await ctx.send(f'Your daily gain: **{gain}**')
            m = user_info[2]
            m += gain
            e -= 1
            print(e)
            c.execute("UPDATE dogs SET money = :money, energy = :energy WHERE  name = :name AND id =  :id",{'money':m,'energy':e,'name':client_name,'id':client_id})
            conn.commit()
            user_info = ui(client_name,client_id)
        else:
            await ctx.send(f'You do not have enough **energy** to work. Try **farming** for energy')
    @client.command()
    async def farm(ctx,count = 1):
        user_info = ui(client_name,client_id)
        dogs =  user_info[3]
        energy = user_info[4]
        if count == 0:
            await  ctx.send(f'Energy gained: {dogs} | Current Dog Supply: **0**')
            energy += dogs
            dogs = 0
            c.execute("UPDATE dogs SET dogs = :dogs, energy = :energy WHERE  name = :name AND id =  :id",{'dogs':dogs,'energy':energy,'name':client_name,'id':client_id})
            conn.commit()
            user_info = ui(client_name,client_id)
        elif dogs >= count:
            await ctx.send(f'Energy gained: **{count}**  |  Current Dog Supply: **{dogs - count}**')
        else:
            await ctx.send(f'You dont have enough dogs for **{count}** energy gains | max possible: {dogs}')
        for i in range(count):
            energy += 1
            dogs -= 1
            c.execute("UPDATE dogs SET dogs = :dogs, energy = :energy WHERE  name = :name AND id =  :id",{'dogs':dogs,'energy':energy,'name':client_name,'id':client_id})
            conn.commit()
            user_info = ui(client_name,client_id)
    @client.command()
    async def buy(ctx,count = 1):
        user_info = ui(client_name,client_id)
        dogs =  user_info[3]
        money = user_info[2]
        dogCost = 100
        if count == 0:
            await ctx.send(f'You bought **{money/dogCost}** dogs | Bill: **{dogCost * (money/dogCost)}** | Balance: **{money-(dogCost*(money/dogCost))}**')
            dogs += money/dogCost
            money -= dogCost * (money/dogCost)
            
        elif money >= count * dogCost:
            dogs += count
            money -= dogCost*count
            await ctx.send(f'You bought **{count}** dogs | Bill: **{dogCost * count}** | Balance: **{money}**')
        else:
            await ctx.send(f'You dont have enough money for **{count}** dogs | MaxCount: **{int(money/dogCost)}**')
        c.execute("UPDATE dogs SET dogs = :dogs, money = :money WHERE  name = :name AND id =  :id",{'dogs':dogs,'money':money,'name':client_name,'id':client_id})
        conn.commit()
        user_info = ui(client_name,client_id)




        









    




global loggedIn
@client.command()
async def loginMine(ctx):
    global money
    try:
        c.execute("""CREATE TABLE mine(
                    name text,
                    id integer,
                    money integer
                )""") 

    except Exception: 
        pass
        # print(traceback.format_exc())
    #retrieve user name and id
    client_name = ctx.author.name
    client_id = ctx.author.id
    await ctx.send(f'Client Id **{client_id}**')
    await ctx.send(f'Client Name **{client_name}**')

    #check database
    with conn:
        c.execute("SELECT * FROM mine")
        print('Database: '+str(c.fetchall()))

    #check if user is located in db
    c.execute("SELECT * FROM mine WHERE name='{}' AND id='{}'".format(client_name,client_id))
    user_info = c.fetchone()
    print('user info:',user_info)

    #Not in database
    if user_info == None:
        money = 0
        c.execute("INSERT INTO mine VALUES (:name,:id,:money)",{'name':client_name,'id':client_id,'money':money})
        conn.commit()
        await ctx.send(f'{client_name} balance: **{money}**')
    #User info in database
    #get money
    else:
        money = user_info[2]
        await ctx.send(f'{client_name} balance: **{money}**')
    with conn:
        c.execute("SELECT * FROM mine")
        print('Database: '+str(c.fetchall()))

    #check

    @client.command()
    async def mine(ctx):
        client_name = ctx.author.name
        client_id = ctx.author.id
        global money
        global moneyOpt
        moneyOpt = [10] * 80 + [100] * 28 + [1000] * 2
        mined = random.choice(moneyOpt)
        await ctx.send(f'You mined for **{mined}** dollars')
        try:
            money = user_info[2]
        except:
            c.execute("SELECT * FROM mine WHERE name='{}' AND id='{}'".format(client_name,client_id))
            user_info = c.fetchone()
            money = user_info[2]
        money += mined
        print(money)
        c.execute("UPDATE mine SET money = :money  WHERE  name = :name AND id =  :id",{'money':money,'name':client_name,'id':client_id})
        conn.commit()
    @client.command()
    async def balance(ctx):
        client_name = ctx.author.name
        client_id = ctx.author.id
        c.execute("SELECT * FROM mine WHERE name='{}' AND id='{}'".format(client_name,client_id))
        user_info = c.fetchone()
        money = user_info[2]
        await ctx.send(f'Your current balance: **{money}**')
    @client.command()
    async def automine(ctx,turns=20):
        client_name = ctx.author.name
        client_id = ctx.author.id
        moneyOpt = [10] * 80 + [100] * 28 + [1000] * 2
        c.execute("SELECT * FROM mine WHERE name='{}' AND id='{}'".format(client_name,client_id))
        user_info = c.fetchone()
        print(user_info)
        money = user_info[2]
        automineCost = turns*100
        total = 0
        if money >= automineCost:
            total = 0
            money = money - automineCost
            await ctx.send(f'**$-{automineCost}**')
            await ctx.send(f'automine activated (turns: **{turns}**)')
            for i in range(turns):
                mined = random.choice(moneyOpt)
                total += mined
            money += total
            await ctx.send(f'you mined a total of ${total} dollars')
            c.execute("UPDATE mine SET money = :money  WHERE  name = :name AND id =  :id",{'money':money,'name':client_name,'id':client_id})
            conn.commit()
        else:
            c.execute("SELECT * FROM mine WHERE name='{}' AND id='{}'".format(client_name,client_id))
            user_info = c.fetchone()
            money = user_info[2]
            await ctx.send(f'Oof, looks like you dont have enough money\n| balance: **{money}**, you are short: **{automineCost-money}**, Max turns currently: **{int(money/100)}**|')

@client.command()
async def ui(ctx,*, member: discord.Member):
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=member.color,timestamp=ctx.message.created_at)
    embed.set_author(name=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    embed.add_field(name="ID: " , value= member.id)
    embed.add_field(name="Guild name: ",value=member.display_name)
    embed.add_field(name="Created at: ", value=member.created_at.strftime("%a,%d %B %Y, %I:%M %p PST"))
    embed.add_field(name = f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
    embed.add_field(name="Top role: ",value=member.top_role.mention)
    embed.add_field(name="Joined at: ",value = member.joined_at.strftime("%a,%d %B %Y, %I:%M %p PST"))
    await ctx.send(embed = embed)

@ui.error
async  def ui_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all required arguments \n**( ui, @member )**')

@client.command()
async def helpme(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        colour = discord.Colour.green()
    )
    embed.set_author(name="Bot Commands - @AnEverything")
    embed.add_field(name="__Categories__", value='Enter .helpme then a category of your choice',inline=False)
    embed.add_field(name="Prefex: 🔣",value='=======')
    embed.add_field(name="Games: 🎮",value='=======')
    embed.add_field(name="Moderate: 🤴",value='=======')
    embed.add_field(name="Fun 👌",value="=======")
    msg = await ctx.send(embed = embed)
    emoji =  ['🔣','🎮','🤴','👌']
    for emo in emoji:
        await msg.add_reaction(emo)
    for emo in emoji:
        def check(rctn, user):
            if user.id == ctx.author.id and str(rctn) in emoji:
                return 'reacted'
        rctn, user = await client.wait_for("reaction_add", check=check)
        author = ctx.message.author
        embed = discord.Embed(
            colour = discord.Colour.blue()
        )
        if str(rctn) == emoji[0]:
            embed.set_author(name="Bot Commands - @AnEverything")
            embed.add_field(name="__Prefix__", value='A symbol you enter before a command',inline=False)
            embed.add_field(name="Prefix", value='(.)',inline=False)
            await ctx.send(embed=embed)
        if str(rctn) == emoji[1]:
            embed.set_author(name="Bot Commands - @AnEverything")
            embed.add_field(name="__Games__",value = 'mining is a multiplayer game where you can mine for money',inline=True)

            embed.add_field(name="`{Mining game}`", value="This is a mining simulator game where you can mine for money",inline=False)
            embed.add_field(name=".loginMining", value="In order to access any of the games commands .loginMine is crucial",inline=True)
            embed.add_field(name=".mine", value="Mining will add money to your balance. The amount of money per mine is not fixed.",inline=True)
            embed.add_field(name=".balance", value="Check your bank accounts current balance/money",inline=True)
            embed.add_field(name=".automine turns", value="Insert two values here (.automine, turns) This should mine x turns for you.\nThe default turns if not set is 20",inline=True)

            embed.add_field(name='`{Dog Game}`', value="This is a dog game where you work every day waisting energy. Your dogs help you farm for energy. You can also by dogs whent they die",inline=False)
            embed.add_field(name='.loginDog',value="In order to access any of the games commands .loginDog is crucial", inline=False)
            embed.add_field(name='.work',value='Work for money | This reduces your energy by 2')
            embed.add_field(name='.farm',value='Farming allows you to gain energy | You loose one dog per energy gained | second param = 0; max amount of energy')
            embed.add_field(name='.buy',value='Allows you to buy more dogs for farming | param 2 = dog count; param 2 = 0;  max amount of dogs')
            embed.add_field(name='.stats',value='Gives you your user_info')

            await ctx.send(embed=embed)
        if str(rctn) == emoji[2]:
            embed.set_author(name="Bot Commands - @AnEverything")
            embed.add_field(name="__Moderate__", value='These commands will allow you to easily moderate your server',inline=True)
            embed.add_field(name=".Ban @user", value='This will allow you to ban any user you would like',inline=True)
            embed.add_field(name=".Kick @user", value='This will allow you to Kick any user you would like',inline=True)
            embed.add_field(name=".mention @user Optional [ count ]", value='Allows you to mention user certain amount of times',inline=True)
            await ctx.send(embed=embed)
        if str(rctn) == emoji[3]:
            embed.set_author(name="Bot Commands - @AnEverything")
            embed.add_field(name="__Random__", value='A tree of commands where you can do random things',inline=True)
            embed.add_field(name=".ui @User", value='Allows you to retrive user info',inline=True)
            await ctx.send(embed=embed)

@client.command()
async def mention(ctx,user: discord.Member, count = 1):
    if count == "Max" or count == "max":
        pass
    for i in range(count):
        await ctx.send(user.mention)
@mention.error
async  def mention_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all required arguments \n**( mention, @member, Optional[**count**])**')
    else:
        print(error)

@client.command()
async def joke(ctx):
    url = 'http://official-joke-api.appspot.com/random_joke'
    r = request.urlopen(url)
    data = r.read()
    jsonData = json.loads(data)
    setup = jsonData["setup"]
    punchline = jsonData["punchline"]

    await ctx.send(setup)
    await ctx.send(f'**||{punchline}||**')
    
@client.command()
async def math(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        colour = discord.Colour.green()
    )
    embed.set_author(name="Math Categories")
    embed.add_field(name="Addition: ➕",value='=======')
    embed.add_field(name="Subtraction: ➖",value='=======')
    embed.add_field(name="Multiplication: ✖",value='=======')
    embed.add_field(name="Division ➗",value="=======")
    
    msg = await ctx.send(embed = embed)
    emoji =  ['➕','➖','✖','➗']
    for emo in emoji:
        await msg.add_reaction(emo)
    for emo in emoji:
        def check(rctn, user):
            if user.id == ctx.author.id and str(rctn) in emoji:
                return 'reacted'
        rctn, user = await client.wait_for("reaction_add", check=check)
        chose = True
        print(rctn)
        if str(rctn) == '➕':
            for i in range(10):
                channel = ctx.channel
                num1 = random.randint(1,100)
                num2 = random.randint(1,100)
                answer = num1 + num2
                await ctx.send(f"Problem: **{num1} + {num2}**")
                await ctx.send(f"peek **||{num1} + {num2} = {answer}||**")
                try:
                    @client.event
                    async def on_message(message):
                        msg = await client.wait_for('message', check=check(ctx.author,ctx.channel), timeout=30)
                        print(ctx)
                        print(ctx.content)
                except Exception as e: 
                    print(e)
                    await ctx.send('you took too long!')
                
                # @client.event
                # async def on_message(message):
                #     isBot = message.author.bot
                #     if isBot != True and message.content.startswith('a'):
                #         if int(message.content[1:]) == int(answer):
                #             print(message.content[1:])
                #             await message.channel.send(f"**correct!**")
                #         else:
                #             await message.channel.send(f"**incorrect!**")


keep_alive()
client.run('ODAyNTg0NDkxMDI4Nzc0OTEy.YAxXDQ.RFPJLNmq1UbDhzzCPjJpKl0CPmg')
conn.close()
c.close()  