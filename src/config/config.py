import os
import sys
import json
import inspect
import util.logger as logger

logger = logger.setup_logger('gemini_chat', '../log/gemini_chat.log')

class config():

    def load_config():  

        funcao_atual = inspect.currentframe().f_code.co_name  

        try:

            if not os.path.isfile(f"{os.path.realpath(os.path.dirname(__file__))}/config.json"):
                sys.exit("'config.json' não encontrado, adicione e tente novamente.")
            else:
                with open(f"{os.path.realpath(os.path.dirname(__file__))}/config.json") as file:
                    
                    logger.info(f"{funcao_atual} - Leitura do arquivo config.json realizada!")   

                    config = json.load(file)

                    return config
        
        except Exception as exception:

            logger.error(f"{funcao_atual} - {exception}")  