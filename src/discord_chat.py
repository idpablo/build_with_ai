import os
import random
import inspect
import discord
import platform

from util import logger
from config import config
from dotenv import load_dotenv
from discord.ext.commands import Bot  
from discord.ext import tasks, commands 
from discord.errors import GatewayNotFound

logger = logger.setup_logger('gemini_chat', '../log/gemini_chat.log')
config = config.config.load_config() 

bot = Bot
bot.config = config  

intents = discord.Intents.all()
intents.presences = False
intents.messages = True
intents.guilds = True

bot = Bot(
    command_prefix=commands.when_mentioned_or(config['prefix']), 
    intents=intents,
    help_command=None,
)

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

    if config['sync_commands_globally']: 
        logger.info('Sincronizado com comandos globais...')
        await bot.tree.sync()

@bot.event
async def on_close(error):
    if isinstance(error, discord.errors.GatewayNotFound):
        logger.warning(f'Gateway not found: {error}')
    else:
        logger.error(f'WebSocket closed unexpectedly: {error}')

try:

    bot.run(config['token']) 
    
except GatewayNotFound as exeption:

    logger.warnning(f'{exeption}')