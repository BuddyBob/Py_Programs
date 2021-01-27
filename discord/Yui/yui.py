import discord
import random
import sqlite3
import traceback
from discord.ext import  commands, tasks
from itertools import cycle
client = commands.Bot(command_prefix = '.')

status = cycle(['Eating Kids','Hurting myself','Being a bully','Making People Angry'])
conn = sqlite3.connect('players.db')
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
        await ctx.send('Please pass in all required arguments \n(8ball,question)')


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

global loggedIn
@client.command()
async def login(ctx):
    global money
    try:
        c.execute("""CREATE TABLE players(
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
        c.execute("SELECT * FROM players")
        print('Database: '+str(c.fetchall()))

    #check if user is located in db
    c.execute("SELECT * FROM players WHERE name='{}' AND id='{}'".format(client_name,client_id))
    user_info = c.fetchone()
    print('user info:',user_info)

    #Not in database
    if user_info == None:
        money = 0
        c.execute("INSERT INTO players VALUES (:name,:id,:money)",{'name':client_name,'id':client_id,'money':money})
        conn.commit()
        await ctx.send(f'{client_name} balance: **{money}**')
    #User info in database
    #get money
    else:
        money = user_info[2]
        await ctx.send(f'{client_name} balance: **{money}**')
    with conn:
        c.execute("SELECT * FROM players")
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
            c.execute("SELECT * FROM players WHERE name='{}' AND id='{}'".format(client_name,client_id))
            user_info = c.fetchone()
            money = user_info[2]
        money += mined
        print(money)
        c.execute("UPDATE players SET money = :money  WHERE  name = :name AND id =  :id",{'money':money,'name':client_name,'id':client_id})
        conn.commit()
    @client.command()
    async def balance(ctx):
        client_name = ctx.author.name
        client_id = ctx.author.id
        c.execute("SELECT * FROM players WHERE name='{}' AND id='{}'".format(client_name,client_id))
        user_info = c.fetchone()
        money = user_info[2]
        await ctx.send(f'Your current balance: **{money}**')
    @client.command()
    async def automine(ctx,turns=20):
        client_name = ctx.author.name
        client_id = ctx.author.id
        moneyOpt = [10] * 80 + [100] * 28 + [1000] * 2
        c.execute("SELECT * FROM players WHERE name='{}' AND id='{}'".format(client_name,client_id))
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
            c.execute("UPDATE players SET money = :money  WHERE  name = :name AND id =  :id",{'money':money,'name':client_name,'id':client_id})
            conn.commit()
        else:
            c.execute("SELECT * FROM players WHERE name='{}' AND id='{}'".format(client_name,client_id))
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
    embed.add_field(name="Mining: ⛏",value='=======')
    embed.add_field(name="Moderate: 🚔",value='=======')
    embed.add_field(name="Fun ✌",value="=======")
    msg = await ctx.send(embed = embed)
    emoji =  ['🔣','⛏','🚔','✌']
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
            embed.add_field(name="__Mining__",value = 'mining is a multiplayer game where you can mine for money',inline=True)
            embed.add_field(name=".login", value="In order to access any of the games commands .login is crucial",inline=True)
            embed.add_field(name=".mine", value="Mining will add money to your balance. The amount of money per mine is not fixed.",inline=True)
            embed.add_field(name=".balance", value="Check your bank accounts current balance/money",inline=True)
            embed.add_field(name=".automine turns", value="Insert two values here (.automine, turns) This should mine x turns for you.\nThe default turns if not set is 20",inline=True)
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




client.run('ODAyNTg0NDkxMDI4Nzc0OTEy.YAxXDQ.F6GmpxKQLsmXAJOGiJrtyfz1M0s')
conn.close()
c.close()  