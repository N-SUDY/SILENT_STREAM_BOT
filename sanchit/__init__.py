#(©) 𝚂𝙰𝙽𝙲𝙷𝙸𝚃 ♛⛧
from telethon import TelegramClient
from logging import getLogger
from logging.config import dictConfig
from .config import Telegram, LOGGER_CONFIG_JSON

dictConfig(LOGGER_CONFIG_JSON)

version = 1.6
logger = getLogger('sanchit')

Sanchit = TelegramClient(
    session='sanchit',
    api_id=Telegram.API_ID,
    api_hash=Telegram.API_HASH
)