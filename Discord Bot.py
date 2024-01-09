import discord_easy_commands
import os
from discord_easy_commands import flask

intentos = discord_easy_commands.discord.Intents.all()
client = discord_easy_commands.EasyBot(intents=intentos)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # Verificar que el mensaje sea del servidor y no del bot
    if message.guild and not message.author.bot:
        if message.content.lower()=="/servert":
            await message.channel.send(f"El servidor es: {flask.request.host_url}")
        # Verificar si el mensaje contiene un enlace a Twitter
        if "https://" in message.content.lower() and not message.channel.name.lower()=="☆promote-yourself✿":
            try:
                await message.delete()
                await message.channel.send(f"{message.author.mention} no puedes publicar mensajes fuera de https://discord.com/channels/1189657001861582918/1189722970520813700")
            except:
                pass
            
        elif "https://twitter.com" in message.content.lower():
            lista=message.content.split("//")
            try:
                lista.remove("")
            except:
                pass
            
            palabra="//vx".join(lista)
            # Crear una copia del mensaje con "vx" agregado al inicio
            new_content = f"{palabra}"

            # Borrar el mensaje original
            await message.delete()

            # Enviar el mensaje copiado al mismo canal
            await message.channel.send(new_content)
        

# Token de autenticación del bot (debes reemplazar esto con tu propio token)

# Iniciar el bot
client.run(os.environ["token"])
