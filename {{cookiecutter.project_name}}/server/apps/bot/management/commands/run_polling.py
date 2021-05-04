import logging

from django.conf import settings
from django.core.management import BaseCommand
from django.utils import autoreload
from telegram.ext import Updater
from telegram.ext.dispatcher import DEFAULT_GROUP

from server.apps.bot.handlers import CALLBACKS


class Command(BaseCommand):
    def handle(self, *args, **options):
        updater = Updater(settings.TELEGRAM_TOKEN)
        updater.dispatcher.groups = [DEFAULT_GROUP]
        updater.dispatcher.handlers[DEFAULT_GROUP] = CALLBACKS

        if settings.DEBUG:
            autoreload.run_with_reloader(updater.start_polling)
        else:
            updater.start_polling()
            updater.idle()
