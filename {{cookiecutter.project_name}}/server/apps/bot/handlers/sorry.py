from telegram import Update
from telegram.ext import CallbackContext


def handle_unknown_message(update: Update, context: CallbackContext):
    update.effective_chat.send_message("I'm sorry, but i do not understand you")
