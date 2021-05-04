from django.urls import path

from server.apps.bot.views import handle_webhook, handle_set_webhook

app_name = 'bot'

urlpatterns = [
    path('handle_webhook', handle_webhook, name='handle-webhook'),
    path('set_webhook', handle_set_webhook, name='set-webhook'),
]
