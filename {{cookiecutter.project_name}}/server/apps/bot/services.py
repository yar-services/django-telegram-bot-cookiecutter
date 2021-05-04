from telegram import Update

from server.apps.bot.models import TelegramUser


def create_user(*, update: Update) -> TelegramUser:
    telegram_user = TelegramUser.objects.create(
        first_name=update.effective_user.first_name,
        last_name=update.effective_user.last_name,
        username=update.effective_user.username,
        language_code=update.effective_user.language_code,
        telegram_user_id=update.effective_user.id,
    )

    return telegram_user


def update_user(*, update: Update) -> TelegramUser:
    telegram_user = TelegramUser.objects.get(telegram_user_id=update.effective_user.id)

    telegram_user.first_name = update.effective_user.first_name
    telegram_user.last_name = update.effective_user.last_name
    telegram_user.username = update.effective_user.username
    telegram_user.language_code = update.effective_user.language_code
    telegram_user.telegram_user_id = update.effective_user.id
    telegram_user.save()

    return telegram_user
