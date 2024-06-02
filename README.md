# Gemini Chat
 Bot criado para consumir a api do gemini...
 
## Sobre

 Bot desenvolvido a partir da api disponibilizada pelo discord:
 [Dashboard API](https://discord.com/developers/applications) / [Documentação API](https://discord.com/developers/docs/intro)
 
## Tecnologias usadas

<div style="display: inline_block"><br>
  <img align="center" alt="Gemini-Chat-Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
  <img align="center" alt="Discord" height="30" width="40" src="https://www.svgrepo.com/show/452188/discord.svg">
  <img align="center" alt="Gemini-Chat-Python" height="30" width="40" src="https://github.com/devicons/devicon/blob/master/icons/ubuntu/ubuntu-plain.svg">
</div>

### Dependências globais
Python3 / NodeJS / pm2

### Criando ambiente virtual

```bash
python -m venv build_with_ai
```
### Iniciando ambiente virtual

```bash
cd build_with_ai
LINUX: ./Scripts/activate
WINDOWS: ./Scripts/activate.bat
```

### Dependências locais

```bash
pip install -r dependency.md
```

### Diretorios necessarios

```bash
mkdir /build_with_ai/log/
```

### Iniciar aplicação

```bash
pm2 start ecosystem.config.js
```

### logs prodatinha

```bash
pm2 logs prodatinha
```

### Monitorar tarefas pm2

```bash
pm2 monit
```

### Reiniciar aplicação

```bash
pm2 restart prodatinha
```

### Parar aplicação

```bash
pm2 stop prodatinha
```

### logs

```bash
pm2 logs prodatinha
```

# Melhorias

    Adicionar controle de containers para subir e testar se a aplicação esta funcionando corretamente;
