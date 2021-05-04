from django.conf import settings
from telegram import Bot
from telegram.ext import Dispatcher
from telegram.ext.dispatcher import DEFAULT_GROUP

from server.apps.bot.handlers import CALLBACKS

bot = Bot(settings.TELEGRAM_TOKEN)

dispatcher = Dispatcher(bot, None, 0, use_context=True) # noqa
dispatcher.groups = [DEFAULT_GROUP]
dispatcher.handlers[DEFAULT_GROUP] = CALLBACKS
