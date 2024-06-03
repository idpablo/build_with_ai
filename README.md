# Gemini Chat
 Bot criado para consumir a api do gemini...
 
## Sobre

 Bot desenvolvido a partir das APIs disponibilizadas pelo Discord e Google Gemini:
 ###
 [Dashboard API](https://discord.com/developers/applications)
 ###
 [Documentação API](https://discord.com/developers/docs/intro)
 ###
 [Gemini API](https://ai.google.dev/gemini-api/docs?hl=pt-br)
 
## Tecnologias usadas

<div style="display: inline_block"><br>
  <img align="center" alt="Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
  <img align="center" alt="Discord" height="30" width="40" src="https://www.svgrepo.com/show/452188/discord.svg">
  <img align="center" alt="Ubuntu" height="30" width="40" src="https://github.com/devicons/devicon/blob/master/icons/ubuntu/ubuntu-original.svg">
  <img align="center" alt="Ubuntu" height="30" width="40" src="https://github.com/idpablo/build_with_ai/blob/main/img/google-gemini-icon.svg">
</div>

### Dependências globais
Python3 / NodeJS / pm2

Instale o PM2 de forma Global

```bash
npm install pm2 -g
```

## Configuração

1. Clone o repositório:

```bash
   git clone https://github.com/idpablo/build_with_ai.git
```
   
O comando a seguir deve ser executado após o download do codigo na pasta raiz que o diretorio foi clonado

```
raiz/
│
├──build_with_ai/
│ │
│ ├── src/
│ │   ├── chat/
│ │   ├── util/
│ │   └── discord_chat.py
```

2. Criando ambiente virtual

```bash
python -m venv build_with_ai
```

3. Iniciando ambiente virtual

```bash
cd build_with_ai
LINUX: ./Scripts/activate
WINDOWS: ./Scripts/activate.bat
```

4. Dependências locais

```bash
pip install -r dependency.md
```

5. Crie e configure as variaveis de ambiente com arquivo .env no diretorio src do projeto

   Inclua as seguintes variaveis:

```
GEMINI_API_KEY=
TOKEN=
PREFIX=!
```

6. Iniciar aplicação

```bash
pm2 start ecosystem.config.js
```

### Monitore gerencie a aplicação:

### logs

```bash
pm2 logs discord_chat
```

### Monitorar tarefas pm2

```bash
pm2 monit discord_chat
```

### Reiniciar aplicação

```bash
pm2 restart discord_chat
```

### Parar aplicação

```bash
pm2 stop discord_chat
```

