const Discord = require('discord.js');
const bot = new Discord.Client()

const ytdl = require('ytdl-core');
const token = 'ODAyMzA4OTMwNDQ0ODUzMjY4.YAtWaw.SX3SGgx7Gv6kxblfkdGzqe4ENpU';
bot.on('ready',() => {
    console.log('Bot is currently online!');
})

const PREFIX = '#';

var servers = {};


bot.on('message',message=>{
    serverQueue = queue.get(message.guild.id)
    let args = message.content.substring(PREFIX.length).split(" ");


    switch(args[0]){
        case 'loop':
            Loop(args,serverQueue)
            break;
        case 'play':
            function play(connection,message){

                var server = servers[message.guild.id];
                server.dispatcher = connection.play(ytdl(server.queue[0], {filter: "audioonly",quality:"highestaudio"}));
                server.queue.shift();

                server.dispatcher.on("end", function(){
                    if(server.queue[0]){
                        play(connection,message);

                    }else{
                        connection.disconnect();

                    }
                })
            }

            if(!args[1]){
                message.channel.send("second parameter link missing!")
                return;
            }
            if(!message.member.voice.channel){
                message.channel.send("Status:  you are not in a channel")
                return;
            }
            if(!servers[message.guild.id]) servers[message.guild.id] = {
                queue: []
            

            }

            var server = servers[message.guild.id]

            server.queue.push(args[1])
            currentSong = args[1]

            if(!message.guild.voiceChannel) message.member.voice.channel.join().then(function(connection){
                play(connection,message)
            })


        break;

        case 'stop':
            var server = servers[message.guild.id];
            if(server.dispatcher) server.dispatcher.end();
            message.channel.send("Song stopped!")
        break;   
    
        case 'loop':
            
            function play(connection,message){
                var server = servers[message.guild.id];
                server.dispatcher = connection.play(ytdl(server.queue[0], {filter: "audioonly",quality:"highestaudio"}));
                
            }

            
            if(!message.member.voice.channel){
                message.channel.send("Status:  you are not in a channel")
                return;
            }
            if(!servers[message.guild.id]) servers[message.guild.id] = {
                queue: []
            

            }

            var server = servers[message.guild.id]
            try{
            server.queue.push(currentSong)
            }
            catch (err){
                message.channel.send("Song not playing")
            }
            if(!message.guild.voiceChannel) message.member.voice.channel.join().then(function(connection){
                play(connection,message)
            })


        break;

        
    }
})

bot.login(token);


