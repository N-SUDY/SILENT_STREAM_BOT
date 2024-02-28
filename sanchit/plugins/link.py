#(©) 𝚂𝙰𝙽𝙲𝙷𝙸𝚃 ♛⛧
import os
import asyncio
from telethon.events import NewMessage
from telethon import TelegramClient, events, types
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

msg_text ="""<b>‣ ʏᴏᴜʀ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴇᴅ ! 😎

‣ Fɪʟᴇ ɴᴀᴍᴇ : <i>{}</i>
‣ Fɪʟᴇ ꜱɪᴢᴇ : {}

🔻 <a href="{}">𝗙𝗔𝗦𝗧 𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗</a>
🔺 <a href="{}">𝗪𝗔𝗧𝗖𝗛 𝗢𝗡𝗟𝗜𝗡𝗘</a>

‣ Tʜɪꜱ Iꜱ Aɴ Aᴅᴠᴀɴᴄᴇ Fɪʟᴇ Sᴛʀᴇᴀᴍ Bᴏᴛ Bʏ : [Tʜᴇ Sɪʟᴇɴᴛ Tᴇᴀᴍ](https://t.me/THE_SILENT_TEAMS) </b> 😆"""

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
            event.message.text = f'`{secret_code}`'
            message = await send_message(event.message)
            message_id = message.id

            log_msg = await Sanchit.send_file(Telegram.CHANNEL_ID, file_path, caption=msg_text.format(file_name, humanbytes(media.size), f'{base_url}/watch/{reply_message.id}/{quote_plus(get_name(reply_message))}?hash={await get_hash(reply_message)}', f'{base_url}/{reply_message.id}/{quote_plus(get_name(reply_message))}?hash={await get_hash(reply_message)}'))
            os.remove(file_path)

            await event.reply(text=msg_text.format(file_name, humanbytes(media.size), f'{Server.BASE_URL}/file/{message_id}?code={secret_code}', f'{Server.BASE_URL}/dl/{message_id}?code={secret_code}', reply_markup=types.ReplyKeyboardMarkup([[types.KeyboardButton("sᴛʀᴇᴀᴍ🔺"), types.KeyboardButton('ᴅᴏᴡɴʟᴏᴀᴅ🔻')]])))

            stream_link = f'{Server.BASE_URL}/stream/{message_id}?code={secret_code}'
            dl_link = f'{Server.BASE_URL}/dl/{message_id}?code={secret_code}'
            
            log_msg = await Sanchit.send_file(Telegram.CHANNEL_ID, file_path, caption=msg_text.format(file_name, humanbytes(media.size), f'{base_url}/watch/{reply_message.id}/{quote_plus(get_name(reply_message))}?hash={await get_hash(reply_message)}', f'{base_url}/{reply_message.id}/{quote_plus(get_name(reply_message))}?hash={await get_hash(reply_message)}'))
            os.remove(file_path)

            await event.reply(msg_text.format(get_name(media)), humanbytes(media.size), stream_link, dl_link, reply_markup=types.ReplyKeyboardMarkup([[types.KeyboardButton("sᴛʀᴇᴀᴍ🔺", url=stream_link), types.KeyboardButton('ᴅᴏᴡɴʟᴏᴀᴅ🔻', url=dl_link)]]))

        else:
            await event.reply("Reply to a valid media file with /link to generate a download link.")

    except Exception as e:
        await event.reply(f"Error generating link: {e}")
