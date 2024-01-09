import discord_easy_commands

intentos = discord_easy_commands.discord.Intents.all()
client = discord_easy_commands.EasyBot(intents=intentos)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # Verificar que el mensaje sea del servidor y no del bot
    if message.guild and not message.author.bot:
        # Verificar si el mensaje contiene un enlace a Twitter
        if "https://" in message.content.lower() and not message.channel.name.lower()=="☆promote-yourself✿":
            await message.delete()
            await message.channel.send(f"{message.author.mention} no puedes publicar mensajes fuera de https://discord.com/channels/1189657001861582918/1189722970520813700")
            
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
client.run("MTE5MDQzNzU3MTk3MzYzMjA5Mw.GpE-Zv.8R5lVgN8PKwFkXI9o7dCRm1gB1F6I59MXZGiiE")