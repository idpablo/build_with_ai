import os
import random
import inspect
import discord
import asyncio
import schedule
import platform

from util import logger
from chat import gemini_chat
from dotenv import load_dotenv
from discord.ext.commands import Bot  
from discord.errors import GatewayNotFound

logger = logger.setup_logger('discord_chat', '../log/bot.log')
load_dotenv()

bot = Bot

DISCORD_API_KEY = os.getenv("DISCORD_API_KEY")
CHANNEL_ID = os.getenv("CHANNEL_ID")

channel = bot.get_channel(int(CHANNEL_ID))

intents = discord.Intents.all()
intents.messages = True

bot = Bot(command_prefix='!', intents=intents,)

def job():
    asyncio.create_task(send_message())

schedule.every().day.at("08:00").do(job)

async def send_message():

    processo_atual = inspect.currentframe().f_code.co_name 

    try:

        news, elapsed_time = await gemini_chat.search_news()

        await channel.send("Bom dia! Esta é a sua atualização de noticias diária às 8 horas da manhã.")
        if len(news) > 2000:
            for i in range(0, len(news), 2000):
                await channel.send(news[i:i+2000])
                await channel.send(f'Tempo de execução: {elapsed_time:.4f} segundos')
        else:
            await channel.send(news)
            await channel.send(f'Tempo de execução: {elapsed_time:.4f} segundos')
        
        await channel.send("Essa funcionalidade ainda está em beta 😢.")

        logger.info(f'Menssage enviada.')
    
    except Exception as exception:

        logger.error(f'{processo_atual} - {exception}')

@bot.command(name='chat')
async def chat(ctx, *, message: str):

    processo_atual = inspect.currentframe().f_code.co_name 

    try:

        response, elapsed_time = await gemini_chat.search_gemini(message)

        if len(response) > 2000:
            for i in range(0, len(response), 2000):
                await ctx.send(response[i:i+2000])
                await ctx.send(f'Tempo de execução: {elapsed_time:.4f} segundos')
        else:
            await ctx.send(response)
            await ctx.send(f'Tempo de execução: {elapsed_time:.4f} segundos')
        
        logger.info(f'Message: {message}')
        logger.info(ctx.guild)

        await status_bot()
    
    except Exception as exception:

        logger.error(f'{processo_atual} - {exception}')

async def status_bot(status=None, estado=None) -> None: 

    processo_atual = inspect.currentframe().f_code.co_name 

    try:
        statuses = ['com outros bots.', 'Paciência!', 'com humanos!']
        
        if status is None: 
            await bot.change_presence(activity=discord.Game(random.choice(statuses))) 
            logger.info(f'Status de presença do bot modificado aletoariamente.')
            return
        
        if status is not None: await bot.change_presence(activity=discord.Game(str(status))) 
        if estado is not None: await bot.change_presence(status=estado) 
    
    except Exception as exception:

        logger.error(f'{processo_atual} - {exception}')

@bot.event
async def on_close(error):
    if isinstance(error, discord.errors.GatewayNotFound):
        logger.warning(f'Gateway not found: {error}')
    else:
        logger.error(f'WebSocket closed unexpectedly: {error}')

@bot.event
async def on_ready():
   
    logger.info(f'Conectado com {bot.user.name}!') 
    logger.info(f'Versão API discord.py: {discord.__version__}')
    logger.info(f'Versão Python: {platform.python_version()}')
    logger.info(f'Rodando na plataforma: {platform.system()} {platform.release()} ({os.name})')
    logger.info('-------------------')

    logger.info('Sincronizado com comandos globais...')

    await status_bot()
    await bot.tree.sync()

    while True:
        schedule.run_pending()
        await asyncio.sleep(1)

try:

    bot.run(DISCORD_API_KEY) 
    
except GatewayNotFound as exeption:

    logger.warnning(f'{exeption}')