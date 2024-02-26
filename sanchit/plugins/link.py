#(©) 𝚂𝙰𝙽𝙲𝙷𝙸𝚃 ♛⛧
import os
import asyncio
from asyncio import TimeoutError
from sanchit import Sanchit
from sanchit.utils.database import Database
from sanchit.utils.human_readable import humanbytes
from sanchit.config import Telegram, Server
from urllib.parse import quote_plus
from pyrogram import filters, Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from sanchit.utils.file_properties import get_name, get_hash, get_media_file_size

msg_text ="""<b>‣ ʏᴏᴜʀ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴇᴅ ! 😎

‣ Fɪʟᴇ ɴᴀᴍᴇ : <i>{}</i>
‣ Fɪʟᴇ ꜱɪᴢᴇ : {}

🔻 <a href="{}">𝗙𝗔𝗦𝗧 𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗</a>
🔺 <a href="{}">𝗪𝗔𝗧𝗖𝗛 𝗢𝗡𝗟𝗜𝗡𝗘</a>

‣ Tʜɪꜱ Iꜱ Aɴ Aᴅᴠᴀɴᴄᴇ Fɪʟᴇ Sᴛʀᴇᴀᴍ Bᴏᴛ Bʏ : [Tʜᴇ Sɪʟᴇɴᴛ Tᴇᴀᴍ](https://t.me/THE_SILENT_TEAMS) </b> 😆"""

@Sanchit.on_message(filters.command("link"))
async def gen_link_handler(bot, message):
    try:
        media = message.reply_to_message
        if message.reply_to_message and (media.document or
                                          media.video or
                                          media.audio or
                                          media.photo):
            
            log_msg = await media.copy(int(Telegram.CHANNEL_ID))
            dl_link = f'{Server.BASE_URL}/dl/{message_id}?code={secret_code}'
            tg_link = f'{Server.BASE_URL}/file/{message_id}?code={secret_code}'

            await message.reply_text(
                text=msg_text.format(get_name(log_msg), humanbytes(get_media_file_size(log_msg)), dl_link, tg_link),
                quote=True,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("sᴛʀᴇᴀᴍ 🔺", url=tg_link),
                                                    InlineKeyboardButton('ᴅᴏᴡɴʟᴏᴀᴅ 🔻', url=dl_link)]])
            )                                  
            
        else:
            await message.reply_text("Reply to a valid media file with `/link` to generate a download link.")
    except Exception as e:
        await message.reply_text(f"Error generating link: {e}")
