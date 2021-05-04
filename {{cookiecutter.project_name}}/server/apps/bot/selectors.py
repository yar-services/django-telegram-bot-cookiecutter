from telegram import Update

from server.apps.bot.models import TelegramUser
from server.apps.bot.services import update_user, create_user


def get_user_by_update(*, update: Update) -> TelegramUser:
    if TelegramUser.objects.get(telegram_user_id=update.effective_user.id).exists():
        user = update_user(update=update)
    else:
        user = create_user(update=update)

    return user
