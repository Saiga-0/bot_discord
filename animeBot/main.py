from discord.ext import commands


bot = commands.Bot(command_prefix='!')

@bot.command()

async def new(ctx):
    channel = ctx.message.channel

    def checkMsg(msg):
        return msg.channel == channel and msg.author == ctx.message.author

    def checkReaction(reaction, user):
        return user == ctx.message.author 


    #ca demande le titre du mangas  
    await channel.send('Quel est le titre du manga ?')

    # on récupère le titre 
    answer_title = await bot.wait_for('message', check=checkMsg)
    title = answer_title.content

    # ca demande un résumé ( cliquez sur la croix si on ne veut pas mettre de résumé  )
    ask_summary = await channel.send('ajouter un résumé ?')
    await ask_summary.add_reaction("✅") 
    await ask_summary.add_reaction("❌")

    if_summary, user = await bot.wait_for('reaction_add', check=checkReaction)

    # on récupère le résumé
    if (str(if_summary.emoji) == "✅"):
        await channel.send('ajoutez votre résumé :')
        answer_summary = await bot.wait_for('message', check=checkMsg)
        summary = "*{x}*".format(x=answer_summary.content)
    else:
        summary=''
    
    # ca demande un lien pour lire le mangas ( cliquez sur la croix si aucun lien dispo)
    ask_link = await channel.send('ajouter un lien ?')
    await ask_link.add_reaction("✅") 
    await ask_link.add_reaction("❌")

    if_link, user = await bot.wait_for('reaction_add', check=checkReaction)

    # on récupère le lien
    if (str(if_link.emoji) == "✅"):
        await channel.send('ajoutez votre lien :')
        answer_link = await bot.wait_for('message', check=checkMsg)
        link = answer_link.content
    else:
        link='  '

    new_mangas = "**__{title}__**\n\n{summary}\n\n **Lien :** ```{link}```".format(title=title, summary=summary, link=link)
  
    
    last_msg = await channel.send(new_mangas)
    await last_msg.add_reaction("🛡️")



    messages = await channel.history(limit=200).flatten()
    for x in messages:
        if (x.reactions == [] or (str(x.reactions[0]) != "🛡️")):
            await x.delete()
                   











  
                


bot.run('OTM2ODc3MTM5NTkxMDQ1MTcw.YfTk1A.3kybzTb2hy20GeWlzC8AZHvDdbA')