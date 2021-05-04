from telegram.ext import CommandHandler

from . import start

CALLBACKS = [
    CommandHandler("start", start.handle_start),
]
