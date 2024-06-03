module.exports = {
    apps: [
      {
        name: 'discord_chat', 
        script: 'discord_chat.py', 
        interpreter: 'python', 
        cwd: './src',
        watch: false, 
        autorestart: false,
        max_memory_restart: '200M',
        env: {
          PYTHONPATH: './scr',
        },
        ignore_watch: ['logs', '.git', '.vscode'],
      },
    ],
  };