from django.contrib import admin

from server.apps.bot.models import TelegramUser


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin[TelegramUser]):
    """Admin panel example for ``TelegramUser`` model."""
    list_display = [
        'first_name', 'last_name', 'username', 'telegram_user_id', 'registered_at'
    ]
