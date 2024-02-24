#(©) 𝚂𝙰𝙽𝙲𝙷𝙸𝚃 ♛⛧
from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", 25833520))
    API_HASH = env.get("TELEGRAM_API_HASH", "7d012a6cbfabc2d0436d7a09d8362af7")
    OWNER_ID = int(env.get("OWNER_ID", 1562935405))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "DS_FILE_2_LINK_BOT")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "6636524134:AAFaFIXJkUYvC5OcV251de3QtSH-jpnM13Q")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", -1001925180658))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 12))

class Server:
    BASE_URL = env.get("BASE_URL", "https://silent-streaming-fcf4d25626aa.herokuapp.com")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", 8080))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
