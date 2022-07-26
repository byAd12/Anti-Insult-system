# list of insults
insults = ["insult1", "insult2"]

@bot.event
async def on_message(msg):
    if msg.author.bot:
        return
    #anti insult system
    for word in insults:
        if word in msg.content.lower():
            try:
                with open("anti-insult-system.json", "r") as f: 
                    antilink = json.load(f) 
                anti_link = antilink[str(msg.guild.id)]

            except KeyError:
                return
            
            with open("anti-insult-system.json", "r") as f: 
                antilink = json.load(f) 
            anti_link = antilink[str(msg.guild.id)]
            
            if anti_link == 'on':
                await msg.delete()
                evr = await msg.channel.send(f"{msg.author.mention} Insults are not allowed in this server")
                await asyncio.sleep(5)
                await evr.delete()
            else: 
                pass

# command to toggle the anti insult system
@bot.command()
@commands.has_permissions(administrator=True)
async def anti_insult(ctx):
    try:
        with open("anti-insult-system.json", "r") as f: # Opening JSON file in variable "f"
            antilink = json.load(f) # Parsing it
        anti_link = antilink[str(ctx.guild.id)] # Getting the Guild's Value via it's value

    except KeyError: # If guild toggle isnt in JSON file, Adding it
        antilink[str(ctx.guild.id)] = "on"
        with open("anti-insult-system.json", "w") as f:
            json.dump(antilink, f, indent=4) # Writing the changes to JSON
        embed1 = discord.Embed(description="Anti insult system has been enabled, when someone beefs the bot will delete and warn the user.", color=0xf1c40f)
        await ctx.send(embed=embed1)


    if anti_link == 'off':
        anti_link = 'on'
        with open("anti-insult-system.json", "r") as f:
            antilink= json.load(f)

        antilink[str(ctx.guild.id)] = anti_link
        
        with open("anti-insult-system.json", "w") as f: # Opening the JSON file but with write mode so we can dump the changes
            json.dump(antilink, f, indent=4) # Dumping the changes

        embed2 = discord.Embed(description="Anti insult system has been enabled, when someone beefs the bot will delete and warn the user.", color=0xf1c40f)
        await ctx.send(embed=embed2)
        
    else:
        """Doing the same thing here"""
        anti_link = 'off'
        with open("anti-insult-system.json", "r") as f:
            antilink= json.load(f)
            
        antilink[str(ctx.guild.id)] = anti_link # setting the guild toggle to 'off'
        
        with open("anti-insult-system.json", "w") as f: # Opening the JSON file but with write mode so we can dump the changes
            json.dump(antilink, f, indent=4) # Dumping the changes
        embed3 = discord.Embed(description="Anti insult system has been Disabled.", color=0xf1c40f)
        await ctx.send(embed=embed3)

bot.run("token")
