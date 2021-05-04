from django.conf import settings
from django.core.management import BaseCommand
from django.utils import autoreload
from telegram.ext import Updater

from server.apps.bot.dispatcher import dispatcher, bot


class Command(BaseCommand):
    def handle(self, *args, **options):
        updater = Updater(bot=bot, dispatcher=dispatcher)
        if settings.DEBUG:
            autoreload.run_with_reloader(updater.start_polling)
        else:
            updater.start_polling()
            updater.idle()
