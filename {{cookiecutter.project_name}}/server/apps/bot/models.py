from django.db import models


class TelegramUser(models.Model):
    telegram_user_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=512)
    last_name = models.CharField(max_length=512, null=True, blank=True)
    username = models.CharField(max_length=32, null=True, blank=True)
    language_code = models.CharField(max_length=8, null=True, blank=True)

    registered_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username or f"{self.first_name} {self.last_name}".strip()
