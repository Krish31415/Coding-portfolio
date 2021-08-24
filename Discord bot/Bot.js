const { prefix, TOKEN } = require('./config.json');
const Discord = require('discord.js');
const client = new Discord.Client();

client.once('ready', () => {
	console.log('Ready!');
});

client.on('message', message => {
	if (message.author===client.user || message.content.legnth===0 ){return}

	let text=message.content.toLowerCase()

	if (text.substring(0,1)!=='.'){return}

	if (message.author.id==='655996089526124572'){
		if(text.substring(1,7)==='custom'){
			message.delete()
			const vc = client.channels.cache.get("836294206463934464")
			vc.setName(message.content.substring(8,))
		}
		if (text.substring(1,6)==='troll'){
			message.delete();
			const vc = client.channels.cache.get("836294206463934464")
			vc.join()
			vc.leave()
		}
	}

	if (text.substring(1,5)==='help'){
		let x=new Discord.MessageEmbed().setTitle('List of Commands')
			.addField('.','This is the current prefix for the commands below',false)
			.addField('idea','Use this command if you have an idea for the bot.', false)
			.addField('repeat','Will repeat what you say after .repeat .',false)
			.addField('reply','Same as .repeat but replys instead of just sending the text.',false)
			.addField('dm me','Private chats you what ever you type after .dm me .',false)
			//.addField('rng ,','Generates a random number between the 2 values you provide. EX: .rng 0,100',false)
			//.addField('math','Gives a random math equation.',false)
			//.addField('answer','Used to answer a question the bot asks you.',false)
			//.addField('pass','Use this to pass a question.',false)
			.addField('calculate','Can take 2 numbers and an operation and returns answer. EX: .calculate 3*7',false)
			//.addField('tictactoe @Opponent','Mention your opponent and react with the symbol that corresponds to the spot on the board.',false);
        message.channel.send(embed=x)
	}

	//useless command
	if (text.substring(1,7)==='repeat' && text.substring(8,)){message.channel.send(text.substring(8,))};
	if (text.substring(1,6)==='reply'){message.reply(text.substring(7,))}
	if (text.substring(1,6)==='dm me'){message.author.send(text.substring(7,))}

	//have some use
	if (text.substring(1,5)==='idea'){
		let Krish=message.guild.members.cache.get('655996089526124572','ID');
		Krish.send(text.substring(6,))
	};

	if (text.substring(1,10)==='calculate'){
		text=text.split(" ")[1]
		message.channel.send(math.simplify(text).toString())
		/*
		if ('+' in text){let sign=text.indexOf('+')}
		if ('-' in text){let sign=text.indexOf('-')}
		if ('*' in text){let sign=text.indexOf('*')}
		if ('/' in text){let sign=text.indexOf('/')}
		let num1=text.substring(0,sign)
		let num2=text.substring(sign+1,)
		if (text[sign]==='+'){message.channel.send(num1+num2)}
		*/
	}

});

client.login(TOKEN);