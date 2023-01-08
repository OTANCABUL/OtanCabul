#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from config import LOG, LOG_GROUP_ID
from YukkiMusic import app
from YukkiMusic.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Private Group"
        logger_text = f"""
🐒**𝗢𝗧𝗔𝗡 𝗖𝗔𝗕𝗨𝗟 𝗣𝗟𝗔𝗬 𝗟𝗢𝗚**

👤**𝙽𝚊𝚖𝚊 𝙶𝚛𝚞𝚙𝚗𝚢𝚊:** {message.chat.title} [`{message.chat.id}`]
🥵**𝙽𝚊𝚖𝚊 𝙿𝚎𝚗𝚌𝚞𝚛𝚒𝚗𝚢𝚊:** {message.from_user.mention}
🧐**𝚄𝚜𝚎𝚛𝚗𝚊𝚖𝚎 𝙿𝚎𝚗𝚌𝚞𝚛𝚒𝚗𝚢𝚊:** @{message.from_user.username}
🆔**𝙸𝙳 𝙿𝚎𝚗𝚌𝚞𝚛𝚒𝚗𝚢𝚊:** `{message.from_user.id}`
♿**𝙻𝚒𝚗𝚔 𝙱𝚊𝚜𝚎𝙲𝚊𝚖𝚙𝚗𝚢𝚊:** {chatusername}

📀**Query:** {message.text}

💽**StreamType:** {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
