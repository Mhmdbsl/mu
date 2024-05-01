import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZelzalMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZelzalMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","السورس","سورس حمو","سورس محمد","حمو"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/95d22359f7f37bceab69b.jpg",
        caption=f"""⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩", url=f"https://t.me/{app.username}?startgroup=true"),
                ],[
                    InlineKeyboardButton(
                        "ძᥱ᥎ ɦᥲꪔ᥆", url=f"https://t.me/JB_U7"),
                    InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐚𝐌𝐨", url=f"https://t.me/Y_U_U_9"),
                ],[
                    InlineKeyboardButton(
                        "", url=f"https://t.me/JB_U7"),
                ],[
                    InlineKeyboardButton(
                        "ძᥱ᥎ ᥲɦꪔᥱძ", url=f"https://t.me/A7_M3"),
                ],[
                    InlineKeyboardButton(text="𝐂𝐥𝐨𝐬𝐞", callback_data="close"),   
            ]
        ]
         ),
     )
  
