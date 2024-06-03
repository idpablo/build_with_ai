import os
import random
import inspect
import discord
import platform

from util import logger
from chat import gemini_chat
from dotenv import load_dotenv
from discord.ext.commands import Bot  
from discord.ext import tasks, commands 
from discord.errors import GatewayNotFound

logger = logger.setup_logger('discord_chat', '../log/bot.log')
load_dotenv()

bot = Bot

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()
intents.messages = True

bot = Bot(command_prefix='!', intents=intents,)

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
async def on_ready():
   
    logger.info(f'Conectado com {bot.user.name}!') 
    logger.info(f'Versão API discord.py: {discord.__version__}')
    logger.info(f'Versão Python: {platform.python_version()}')
    logger.info(f'Rodando na plataforma: {platform.system()} {platform.release()} ({os.name})')
    logger.info('-------------------')

    logger.info('Sincronizado com comandos globais...')

@bot.event
async def on_close(error):
    if isinstance(error, discord.errors.GatewayNotFound):
        logger.warning(f'Gateway not found: {error}')
    else:
        logger.error(f'WebSocket closed unexpectedly: {error}')

@bot.command(name='chat')
async def chat(ctx, *, message: str):

    response = await gemini_chat.search_gemini(message)

    if len(response) > 2000:
        for i in range(0, len(response), 2000):
            await ctx.send(response[i:i+2000])
    else:
        await ctx.send(f'Resposta: {response}')
    
    logger.info(f'Message: {message}')
    logger.info(ctx.guild)

try:

    bot.run(TOKEN) 
    
except GatewayNotFound as exeption:

    logger.warnning(f'{exeption}')