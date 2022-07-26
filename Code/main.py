# list of insults
insults = ["shit", "Shit", "Fuck off", "fuck off", "fuck", "Fuck", "fck", "Fck", "Fck off", "fck off", "sht", "Sht", "Twat", "twat", "fuck yourself", "Fuck yourself", "Fck yourself", "fck yourself", "screw you", "Screw you", "Asshole", "asshole", "bullshit", "Bullshit", "bitch", "Bitch", "btch", "Btch", "stfu", "Stfu", "STFU", "StFu", "s.t.f.u", "S.T.F.U", "S.T.F.U.", "s.t.f.u.", "Stfu.", "stfu.", "motherfucker", "Motherfucker", "motherFucker", "mother fucker", "Mother fucker", "Mother Fucker", "Fucker", "son of bitch", "Son of bitch", "son of Bitch", "ur mom", "Ur mom", "Ur Mom", "ur Mom", "ur mum", "Ur mum", "Your mom", "your mom", "Idiot", "idiot", "dumbass", "Dumbass", "dumb ass", "Dumb ass", "Jerk", "jerk", "piss off", "Piss off", "cock sucker", "Cock", "Cock sucker", "dick head", "dickhead", "Dickhead", "Dick Head", "Dick", "Pennis", "dick", "pennis", "whore", "Whore", "pussy", "Pussy", "P*ussy", "Prick", "prick", "White Trash", "white trash", "kiss my ass", "Kiss my ass", "moron", "Moron", "cock", "Cock", "Holy Shit", "holy shit", "Holy shit", "God Damn it", "God damn it", "god Damn it", "god damn it", "piece of trash", "Pieve of trash", "bastard", "Bastard", "gives a fuck", "Gives a fuck", "Freaking idiot", "freaking idiot", "ass", "Ass", "f*ck", "F*ck"]


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
        embed1 = nextcord.Embed(description="Anti insult system has been enabled, when someone beefs the bot will delete and warn the user.", color=0xf1c40f)
        await ctx.send(embed=embed1)


    if anti_link == 'off':
        anti_link = 'on'
        with open("anti-insult-system.json", "r") as f:
            antilink= json.load(f)

        antilink[str(ctx.guild.id)] = anti_link
        
        with open("anti-insult-system.json", "w") as f: # Opening the JSON file but with write mode so we can dump the changes
            json.dump(antilink, f, indent=4) # Dumping the changes

        embed2 = nextcord.Embed(description="Anti insult system has been enabled, when someone beefs the bot will delete and warn the user.", color=0xf1c40f)
        await ctx.send(embed=embed2)
        
    else:
        """Doing the same thing here"""
        anti_link = 'off'
        with open("anti-insult-system.json", "r") as f:
            antilink= json.load(f)
            
        antilink[str(ctx.guild.id)] = anti_link # setting the guild toggle to 'off'
        
        with open("anti-insult-system.json", "w") as f: # Opening the JSON file but with write mode so we can dump the changes
            json.dump(antilink, f, indent=4) # Dumping the changes
        embed3 = nextcord.Embed(description="Anti insult system has been Disabled.", color=0xf1c40f)
        await ctx.send(embed=embed3)
