"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python

"""
import os
import time
import inspect
import google.generativeai as genai

from util import logger
from dotenv import load_dotenv

logger = logger.setup_logger('gemini_chat', '../log/bot.log') 

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')

load_dotenv(dotenv_path=dotenv_path)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
)

async def search_gemini(message):

  start_time = time.time()
  current_process = inspect.currentframe().f_code.co_name 

  try:

    logger.info(f'Mensagem a ser processada:{message}')

    chat_session = model.start_chat(
      history=[
      ]
    )
      
    response = chat_session.send_message(message)

    end_time = time.time()
    elapsed_time = end_time - start_time
    
    logger.info(f'Mensagem enviada com exito.')
    logger.info(f"Tempo de execução: {elapsed_time:.4f} segundos")


    return response.text, elapsed_time

  except Exception as exception:

    logger.error(f'{current_process} - {exception}')


async def search_news():
    
    start_time = time.time()
    current_process = inspect.currentframe().f_code.co_name

    try:

        response = model.generate_content('Liste as noticias de tecnologia mais recentes.')

        end_time = time.time()
        elapsed_time = end_time - start_time
        
        logger.info(f'Mansagem enviada com exito.')
        logger.info(f"Tempo de execução: {elapsed_time:.4f} segundos")

        return response.text, elapsed_time

    except Exception as exception:

      logger.error(f'{current_process} - {exception}')