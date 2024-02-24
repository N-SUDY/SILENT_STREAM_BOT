WelcomeText = \
"""<b>ᴊᴀɪ sʜʀᴇᴇ Rᴀᴍ {}!,
I ᴀᴍ Fɪʟᴇ ᴛᴏ Lɪɴᴋ Gᴇɴᴇʀᴀᴛᴏʀ Bᴏᴛ ᴡɪᴛʜ Cʜᴀɴɴᴇʟ sᴜᴘᴘᴏʀᴛ.

Sᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇ ᴀɴᴅ ɢᴇᴛ ᴀ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ ᴀɴᴅ sᴛʀᴇᴀᴍᴀʙʟᴇ ʟɪɴᴋ.!

ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/THE_SILENT_TEAMS'>Tʜᴇ Sɪʟᴇɴᴛ Tᴇᴀᴍ</a></b>"""

UserInfoText = \
"""
**First Name:**
`{sender.first_name}`

**Last Name:**
`{sender.last_name}`

**User ID:**
`{sender.id}`

**Username:**
`@{sender.username}`
"""

FileLinksText = \
"""
**📥Download Link:**
\n  `[Click Here](%(dl_link)s)`

**📁Telegram File:**
\n  `[Click Here](%(tg_link)s)`
"""

MediaLinksText = \
"""
**📥Download Link:**
\n  `%(dl_link)s`

**📺Stream Link:**
\n  `%(stream_link)s`

**📁Telegram File:**
\n  `%(tg_link)s`
"""

InvalidQueryText = \
"""
Query data mismatched.
"""

MessageNotExist = \
"""
File revoked or not exist.
"""

LinkRevokedText = \
"""
The link has been revoked. It may take some time for the changes to take effect.
"""

InvalidPayloadText = \
"""
Invalid payload.
"""

MediaTypeNotSupportedText = \
"""
Sorry, this media type is not supported.
"""
