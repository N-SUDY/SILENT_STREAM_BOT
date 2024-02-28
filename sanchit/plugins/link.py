#(©) 𝚂𝙰𝙽𝙲𝙷𝙸𝚃 ♛⛧
import os
import asyncio
from telethon.events import NewMessage
from telethon import TelegramClient, events
from telethon.tl.custom import Button
from asyncio import TimeoutError
from sanchit import Sanchit
from sanchit.utils.database import Database
from sanchit.utils.human_readable import humanbytes
from sanchit.config import Telegram, Server
from pyrogram import filters, Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from sanchit.utils.file_properties import get_name, get_hash, get_media_file_size
from secrets import token_hex
from sanchit.modules.telegram import send_message, filter_files
from sanchit.modules.static import *


base_url = Server.BASE_URL

def get_name(message):
    if message.file.name:
        return message.file.name
    elif message.file.id:
        return f"file_{message.file.id}"
    else:
        return "unnamed"

def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    n = 0
    units = ['B', 'KiB', 'MiB', 'GiB', 'TiB']
    while size > power:
        size /= power
        n += 1
    return f"{round(size, 2)} {units[n]}"

def get_media_file_size(message):
    if message.file.size:
        return message.file.size
    elif message.video:
        return message.video.size
    elif message.audio:
        return message.audio.size
    elif message.photo:
        return message.photo.size
    else:
        return 0


@Sanchit.on(events.NewMessage(pattern="/link"))
async def gen_link_handler(event):
    try:
        reply_message = await event.get_reply_message()
        if reply_message and (reply_message.document or reply_message.video or reply_message.audio or reply_message.photo):
            media = reply_message.file
            file_name = media.name
            file_path = await reply_message.download_media(file_name)
            secret_code = token_hex(Telegram.SECRET_CODE_LENGTH)
            message_id = reply_message.id

            msg_text = f"""**‣ ʏᴏᴜʀ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴇᴅ ! 😎

‣ Fɪʟᴇ ɴᴀᴍᴇ : __{get_name(reply_message)}__

‣ Tʜɪꜱ Iꜱ Aɴ Aᴅᴠᴀɴᴄᴇ Fɪʟᴇ Sᴛʀᴇᴀᴍ Bᴏᴛ Bʏ : [Tʜᴇ Sɪʟᴇɴᴛ Tᴇᴀᴍ](https://t.me/THE_SILENT_TEAMS) ** 😆"""


            log_msg = await Sanchit.send_file(Telegram.CHANNEL_ID, file_path, caption=msg_text.format(file_name, humanbytes(media.size), f'{Server.BASE_URL}/stream/{message_id}?code={secret_code}', f'{Server.BASE_URL}/dl/{message_id}?code={secret_code}'))

            stream_link = f'{Server.BASE_URL}/stream/{message_id}?code={secret_code}'
            dl_link = f'{Server.BASE_URL}/dl/{message_id}?code={secret_code}'

            log_msg = await Sanchit.send_file(Telegram.CHANNEL_ID, file_path, caption=msg_text.format(file_name, humanbytes(media.size), stream_link, dl_link))
            os.remove(file_path)

            await event.reply(msg_text, buttons=[Button.url("sᴛʀᴇᴀᴍ🔺", url=stream_link), Button.url('ᴅᴏᴡɴʟᴏᴀᴅ🔻', url=dl_link)], link_preview=False, parse_mode = 'md')

        else:
            await event.reply("Reply to a valid media file with /link to generate a download link.")

    except Exception as e:
        await event.reply(f"Error generating link: {e}")
