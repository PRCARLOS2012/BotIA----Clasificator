import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachments in ctx.message.attachments:
            name = attachments.filename
            url = attachments.url
            await attachments.save(name)
            await ctx.send("El archivo adjunto se guardo correctamente")
            

            try:
                class_name = get_class("keras_model.h5", "labels.txt", name)
                if class_name == "Pigeons":
                    await ctx.send("Esto es una paloma, y es un ave muy comun en zonas pobladas")
                elif class_name == "Sparrows":
                    await ctx.send("Esto es un Gorrion, y es un ave medio comun en zonas muy pobladas")

            except:
                await ctx.send("No se a podido hacer la clasificacion, recuerda que solo se permiten archivos jpg,png o jpe.")
    else:
        await ctx.send("No hay archivos adjuntos")

bot.run("token")