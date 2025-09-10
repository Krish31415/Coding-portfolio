import discord, time, random, nacl

TOKEN = "Insert token here"
client = discord.Client()
answers = []
cuss = mention = off = False
word = " "
bad = []
# x=open('cuss.txt','r')
# while word!='stop':
#     word=x.readline()
#     bad.append(word[:-1])
# bad.pop()

# users={}
# word=['Krish Kalra']
# y=open('users.txt','r')
# while word[0]!='stop':
#     word=(y.readline()).split(' ')
#     if word[0]!='stop': users[word[1]]=word[0]


@client.event
async def on_ready():
    print(f"{client.user} is online!")


@client.event
async def on_message(message):
    global off
    global cuss
    global mention
    global answers
    if message.author == client.user or len(message.content) == 0:
        return

    text = message.content.lower()
    ogtext = message.content

    # users[str(message.author.id)+'\n']=((message.author.display_name).replace(' ',''))

    # for a in (text.split()):
    #     if a.lower() in bad and cuss: await message.channel.send('\"Language\"-Cap')

    if text[0] != ".":
        return
    # dev commands
    if message.author.id == ('put your discord id here, it can be accessed with dev tools'):
        if text[1:7] == "rename":
            text = message.content.split(" ")
            channel = await client.fetch_channel(text[1])
            x = ""
            for a in range(2, len(text)):
                x += text[a] + " "
            print(x)
            await channel.edit(name=x)

        if text[1:6] == "troll":
            await message.delete()
            text = message.content.split(" ")
            vc = await client.fetch_channel(text[1])
            for a in range(int(text[2])):
                VC = await vc.connect()
                await VC.disconnect()
                time.sleep(random.uniform(0.1, 3))

        if text[1:4] == "bot":
            off = not off
            await message.channel.send(
                "The bot is now " + ("disabled." if off else "enabled.")
            )

        if text[1:7] == "update":
            await client.close()

        if text[1:5] == "cuss":
            cuss = not cuss
            await message.channel.send(
                "The cuss detector is now " + ("enabled." if cuss else "disabled.")
            )

        if text[1:] == "mention":
            mention = not mention
            await message.channel.send(
                "The mention command is now " + ("enabled." if mention else "disabled.")
            )

        if text[1:] == "custom":
            await message.delete()
            print(message.guild.roles[-1].id)
    if off:
        return

    if text[1:5] == "idea":
        user = await client.fetch_user(655996089526124572)
        await user.send(text[6:])

    if text[1:9] == "help":
        x = discord.Embed(title="List of commands")
        x.add_field(
            name=".",
            value="This is the current prefix for the commands below",
            inline=False,
        )
        x.add_field(
            name="idea",
            value="Use this command if you have an idea for the bot.",
            inline=False,
        )
        x.add_field(
            name="repeat",
            value="Will repeat what you say after .repeat .",
            inline=False,
        )
        x.add_field(
            name="reply",
            value="Same as .repeat but replys instead of just sending the text.",
            inline=False,
        )
        x.add_field(
            name="dm me",
            value="Private chats you what ever you type after .dm me .",
            inline=False,
        )
        x.add_field(
            name="rng(,)",
            value="Generates a random number between the 2 values you provide. EX: .rng(0,100)",
            inline=False,
        )
        x.add_field(name="math", value="Gives a random math equation.", inline=False)
        x.add_field(
            name="answer",
            value="Used to answer a question the bot asks you.",
            inline=False,
        )
        x.add_field(name="pass", value="Use this to pass a question.", inline=False)
        x.add_field(
            name="calculate()",
            value="Can take 2 numbers and an operation and returns answer. EX: .calculate(3*7)",
            inline=False,
        )
        x.add_field(
            name="tictactoe @Opponent",
            value="Mention your opponent and react with the symbol that corresponds to the spot on the board.",
            inline=False,
        )
        await message.channel.send(embed=x)

    # useless commands
    if text[1:7] == "repeat":
        await message.channel.send(text[8:])
    if text[1:6] == "dm me":
        await message.author.send(text[7:])
    if text[1:6] == "reply":
        await message.reply(text[7:], mention_author=False)

    # have some use
    if text[1:8] == "mention" and mention:
        await message.delete()
        user = (ogtext.split(" "))[1]
        print(user)
        b = message.guild.get_member_name(user)
        await message.channel.send("Hi %s" % b, delete_after=1)

    if text[1:4] == "rng":
        num1 = int(text[text.index("(") + 1 : text.index(",")])
        num2 = int(text[text.index(",") + 1 : text.index(")")])
        await message.channel.send(str(random.randint(num1, num2)))

    # actually decently useful
    if text[1:5] == "math":
        for a in answers:
            if message.author == a[1]:
                answers.remove(a)
        num1 = str(random.randint(0, 99))
        num2 = str(random.randint(0, 99))
        sign = random.choice(["+", "-", "*"])
        await message.reply(num1 + sign + num2, mention_author=True)

        answers.append([eval(num1 + sign + num2), message.author])
        # if sign == "+":
        #     answers.append([int(num1) + int(num2), message.author])
        # if sign == "-":
        #     answers.append([int(num1) - int(num2), message.author])
        # if sign == "*":
        #     answers.append([int(num1) * int(num2), message.author])

    if text[1:7] == "answer":
        for a in answers:
            if message.author == a[1]:
                if int(text[8:]) == a[0]:
                    await message.reply("Correct!")
                else:
                    await message.reply("Wrong, the correct answer was " + str(a[0]))

    if text[1:5] == "pass":
        for a in answers:
            if message.author == a[1]:
                await message.reply("The answer was " + str(a[0]))
                answers.remove(a)

    if text[1:10] == "calculate":
        if "+" in text:
            sign = "+"
        if "-" in text:
            sign = "-"
        if "*" in text:
            sign = "*"
        if "/" in text:
            sign = "/"
        await message.channel.send(eval(num1 + sign + num2))
        # num1 = float(text[text.index("(") + 1 : text.index(sign)])
        # num2 = float(text[text.index(sign) + 1 : text.index(")")])
        # if sign == "+":
        #     await message.channel.send(num1 + num2)
        # if sign == "-":
        #     await message.channel.send(num1 - num2)
        # if sign == "*":
        #     await message.channel.send(num1 * num2)
        # if sign == "/":
        #     await message.channel.send(num1 / num2)

    # main commands
    if text[1:10] == "tictactoe" and message.mentions:
        emojis = [
            "\u2196",
            "\u2B06",
            "\u2197",
            "\u2b05",
            "\u23fa",
            "\u27a1",
            "\u2199",
            "\u2b07",
            "\u2198",
        ]
        p1 = message.author
        p2 = message.mentions[0]
        blank = " :black_large_square: "
        state = ""
        for a in range(9):
            state += blank
            state += " \n---------------\n" if a % 3 == 2 else " | "
        e = discord.Embed(description=state[:-16])
        e.add_field(name="Players:", value=p1.mention + p2.mention)
        m = await message.channel.send(embed=e)
        state = state.split(" ")
        while "|" in state:
            state.remove("|")
        while "-" in state:
            state.remove("-")
        while "\n---------------\n" in state:
            state.remove("\n---------------\n")
        while "" in state:
            state.remove("")
        for a in range(9):
            if state[a] == ":black_large_square:":
                await m.add_reaction(emojis[a])


@client.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return

    if not reaction.message.embeds:
        return
    emojis = [
        "\u2196",
        "\u2B06",
        "\u2197",
        "\u2b05",
        "\u23fa",
        "\u27a1",
        "\u2199",
        "\u2b07",
        "\u2198",
    ]
    players = reaction.message.embeds[0].fields[0].value
    if "!" in list(players):
        players = players.replace("!", "")
    players = [
        int(players[2 : players.index(">")]),
        int(players[players.index(">") + 3 : -1]),
    ]
    if not user.id in players:
        return
    emoji = list(reaction.emoji)[0]
    state = reaction.message.embeds[0].description.split(" ")
    while "|" in state:
        state.remove("|")
    while "-" in state:
        state.remove("-")
    while "\n---------------\n" in state:
        state.remove("\n---------------\n")
    while "" in state:
        state.remove("")
    turn = 0
    for a in state:
        if ":x:" == a:
            turn += 1
        if ":o:" == a:
            turn -= 1
    if not (user.id == players[turn] or user.id == 655996089526124572):
        return
    letter = ":x:" if turn == 0 else ":o:"
    emoji = emojis.index(emoji)
    state[emoji] = letter
    s = ""
    for a in range(9):
        s += state[a]
        s += " \n---------------\n " if a % 3 == 2 else " | "
    e = discord.Embed(description=s[:-17])
    p1, p2 = "<@" + str(players[0]) + ">", "<@" + str(players[1]) + ">"
    e.add_field(name="Players:", value=("%s" % p1 + "%s" % p2))
    await reaction.message.edit(embed=e)
    await reaction.message.clear_reaction(reaction.emoji)
    win = True in [
        (state[0] == state[1] == state[2] != ":black_large_square:"),
        (state[3] == state[4] == state[5] != ":black_large_square:"),
        (state[6] == state[7] == state[8] != ":black_large_square:"),
        (state[0] == state[3] == state[6] != ":black_large_square:"),
        (state[4] == state[1] == state[7] != ":black_large_square:"),
        (state[8] == state[5] == state[2] != ":black_large_square:"),
        (state[0] == state[4] == state[8] != ":black_large_square:"),
        (state[6] == state[4] == state[2] != ":black_large_square:"),
    ]
    if win:
        await reaction.message.clear_reactions()
        return await reaction.message.edit(
            content=("%s" % ("<@" + str(players[turn]) + ">")) + " has won."
        )
    if ":black_large_square:" not in state:
        return await reaction.message.edit(
            content="Draw between"
            + ("%s" % ("<@" + str(players[0]) + ">"))
            + ("%s" % ("<@" + str(players[turn]) + ">"))
        )


client.run(TOKEN)
