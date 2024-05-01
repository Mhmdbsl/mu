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
    command(["محمد","حمو","المطور","مبرمج السورس","مطور السورس","الهكر","الهقر","مطور"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/95d22359f7f37bceab69b.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪𝗠𝗼𝗵𝗮𝗺𝗺𝗲𝗱❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @JB_U7 ❫
◉ 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 : ❪ [𝗦𝗼𝘂𝗥𝗰𝗲 𝗠𝗼𝗵𝗮𝗺𝗺𝗲𝗱](t.me/Y_U_U_9) ❫
◉ 𝙱𝙸𝙾    : ❪[#𝖱ꫀᥲ️ᥣᥣ𝗒,!Ꭵ ძ᥆ꪀ'𝗍 ᥴᥲ️𝗋ꫀ#ɪ'َᴍ 𓏺 𝗠𝗼𝗵𝗮𝗺𝗺𝗲𝗱.🦅🇪🇬](https://t.me/JB_U7) ❫""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "𝗠𝗼𝗵𝗮𝗺𝗺𝗲𝗱", url=f"https://t.me/JB_U7"),
            ]
        ]
         ),
     )
  
