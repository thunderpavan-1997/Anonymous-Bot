import logging
from pyrogram import Client
from vars import var

logging.basicConfig(level=logging.INFO)

AnonyBot = Client('Anonymous-Sender',
                  bot_token=var.BOT_TOKEN,
                  plugins=dict(root="plugins"))

AnonyBot.run()
