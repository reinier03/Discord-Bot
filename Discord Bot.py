import easy_bot_reima
import os
import threading
import requests 
from bs4 import BeautifulSoup as bs
from time import sleep


id_canal=1189687855774191687


user={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0"}
diccionario={}



intentos = easy_bot_reima.discord.Intents.all()
client = easy_bot_reima.EasyBot(intents=intentos)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # Verificar que el mensaje sea del servidor y no del bot
    if message.guild and not message.author.bot:
        # Verificar si el mensaje contiene un enlace a Twitter
        if "https://" in message.content.lower() and (message.channel.name.lower()=="☆promote-yourself✿" or message.channel.name.lower()=="🔞nsfw-uwu"):
            return

        elif "https://" in message.content.lower():

            try:
                await message.delete()
                await message.channel.send(f"{message.author.mention} you cannot publish links outside of https://discord.com/channels/1189657001861582918/1189722970520813700")
            except:
                return

        else:
            return

            
        #elif "https://twitter.com" in message.content.lower():
            #lista=message.content.split("//")
            #try:
                #lista.remove("")
            #except:
                #pass
            
            #palabra="//vx".join(lista)
            # Crear una copia del mensaje con "vx" agregado al inicio
            #new_content = f"{palabra}"

            # Borrar el mensaje original
            #await message.delete()

            # Enviar el mensaje copiado al mismo canal
            #await message.channel.send(new_content)
        





def obtener_memes():
    global diccionario
    global user
    contador=0
    diccionario.clear()
    while not len(diccionario)>=48:
        contador+=1
        res=requests.get(f"https://www.memedroid.com/memes/random?page={contador}", headers=user)
        soup=bs(res.text, features="html.parser")
        articulos=soup.find_all("article", class_="gallery-item")
        for e, i in enumerate(articulos, start=len(diccionario)+1):
            try:
                imagen=i.find("img", class_="img-responsive grey-background").attrs.get("src")
                texto=i.find("a", class_="item-header-title dyn-link").text
                diccionario[e]=[imagen, texto]
                if len(diccionario)>= 48:
                    break
            except:
                video=i.find("video", class_="item-video gallery-item-video grey-background").find("source").attrs.get("src")
                texto=i.find("a", class_="item-header-title dyn-link").text
                diccionario[e]=[video, texto]
                if len(diccionario)>= 48:
                    break
                
                
    return publicar(diccionario, user)


def publicar(diccionario, user):
    canal=client.get_channel(1189687855774191687) #reemplazar este valor con el chat id del destino
    for e, i in enumerate(diccionario, start=1):
        res=requests.get(diccionario[e][0], headers=user)
        
        with open(f"{os.path.basename(diccionario[e][0])}", "wb") as archivo_escritura:
            archivo_escritura.write(res.content)
            
        archivo_lectura=open(f"{os.path.basename(diccionario[e][0])}", "rb")
        archivo=easy_bot_reima.discord.File(archivo_lectura)
        canal.send(f"{diccionario[e][1]}",file=archivo) 
                
        archivo_lectura.close()
        os.remove(os.path.basename(diccionario[e][0]))
        sleep(1800)
    return
            
                
                
                

@client.event
async def on_ready():
    lista=threading.enumerate()
    for i in lista:
        if "hilo" in str(i):
            break
    else:
        hilo=threading.Thread(target=obtener_memes, name="hilo")
        hilo.start()





# Iniciar el bot
client.run(os.environ["token"])
