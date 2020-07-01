#Discord Importen
import discord

#Verinfachung: Client definieren

client = discord.Client()

# Event

@client.event
#Wenn der Bot Ready ist
async def on_ready():
    #Etwas ausgeben
    print("Gestartet")

#Client starten
client.run("token")