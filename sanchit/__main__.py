#(©) 𝚂𝙰𝙽𝙲𝙷𝙸𝚃 ♛⛧
from importlib import import_module
from pathlib import Path
from sanchit import Sanchit, logger
from sanchit.config import Telegram
from sanchit.server import server

def load_plugins():
    count = 0
    for path in Path('sanchit/plugins').rglob('*.py'):
        import_module(f'sanchit.plugins.{path.stem}')
        count += 1
    logger.info(f'Loaded {count} {"plugins" if count > 1 else "plugin"}.')

if __name__ == '__main__':
    logger.info('initializing...')
    Sanchit.loop.create_task(server.serve())
    Sanchit.start(bot_token=Telegram.BOT_TOKEN)
    logger.info('Telegram client is now started.')
    logger.info('Loading bot plugins...')
    load_plugins()
    logger.info('Bot is now ready!')
    Sanchit.run_until_disconnected()