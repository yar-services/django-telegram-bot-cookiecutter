from telegram import Update
from telegram.ext import CallbackContext

from server.apps.bot.selectors import get_user_by_update


def handle_start(update: Update, context: CallbackContext):
    user = get_user_by_update(update=update)
    update.effective_chat.send_message(f"Hi {user.first_name}!")
