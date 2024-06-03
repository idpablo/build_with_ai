"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python

"""
import os
import json
import asyncio
import google.generativeai as genai

from util import logger
from dotenv import load_dotenv

file_path = '../json_data/'
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')

load_dotenv(dotenv_path=dotenv_path)

logger = logger.setup_logger('gemini_chat', '../log/bot.log') 

async def search_gemini(menssage):

  logger.info(f'Mensagem a ser processada:{menssage}')

  GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

  genai.configure(api_key=GEMINI_API_KEY)

  generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
  }

  safety_settings = [
    {
      "category": "HARM_CATEGORY_HARASSMENT",
      "threshold": "BLOCK_NONE",
    },
    {
      "category": "HARM_CATEGORY_HATE_SPEECH",
      "threshold": "BLOCK_NONE",
    },
    {
      "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
      "threshold": "BLOCK_NONE",
    },
    {
      "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
      "threshold": "BLOCK_NONE",
    },
  ]

  model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    safety_settings=safety_settings,
    generation_config=generation_config,
  )

  chat_session = model.start_chat(
    history=[
    ]
  )
    
  response = chat_session.send_message(menssage)
  # asyncio.create_task(save_response_to_json(response))

  print(response)

  return response.text

# async def save_response_to_json(response):
#     """
#     Salva a resposta em um arquivo JSON.

#     Args:
#         response (GenerateContentResponse): A resposta a ser salva.
#     """

#     try:
#         os.makedirs(os.path.dirname(file_path), exist_ok=True)
#         file_path_json = os.path.join(file_path, 'gemini_response.json')

#         json_response = json.dumps(response, indent=2)

#         with open(file_path_json, 'w') as arquivo_json:
#             json.dump(json_response, arquivo_json)

#         return True

#     except Exception as e:
#         logger.info(f'Erro ao salvar JSON: {e}')
#         return False