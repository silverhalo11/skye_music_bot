from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os
import sys
from threading import Thread
from pyrogram import idle, filters
from pyrogram.handlers import MessageHandler
from helpers.wrappers import errors, admins_only


@Client.on_message(
    filters.command("repo")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "**êvilẞø†:** if you want musicbot like me then click on repo button to get my repo and click on SESSION button for gernating session and click on heroku botton to deploy me🤍  \n**GO AND DEPLOY ❤️**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💙 REPO 💙", url="https://github.com/silverhalo11/skye_music_bot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💚 SESSION 💚", url="https://repl.it/@pawanjatt/evilmusicbot"
                    ),
                    InlineKeyboardButton(
                        "💜 HEROKU 💜", url="https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Fsilverhalo11%2Fskye_music_bot&template=https%3A%2F%2Fgithub.com%2Fsilverhalo11%2Fskye_music_bot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "❌ Close ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
    
@Client.on_message(
    filters.command("repo")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        "**êvilẞø†:** if you want musicbot like me then click on repo button to get my repo and click on SESSION button for gernating session and click on heroku botton to deploy me🤍  \n**GO AND DEPLOY ❤️**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💙 REPO 💙", url="https://github.com/silverhalo11/skye_music_bot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💚 SESSION 💚", url="https://repl.it/@pawanjatt/evilmusicbot"
                    ),
                    InlineKeyboardButton(
                        "💜 HEROKU 💜", url="https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Fsilverhalo11%2Fskye_music_bot&template=https%3A%2F%2Fgithub.com%2Fsilverhalo11%2Fskye_music_bot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "❌ Close ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
