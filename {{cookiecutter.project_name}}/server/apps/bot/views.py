import json

from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from telegram import Update

from server.apps.bot.dispatcher import dispatcher, bot


@csrf_exempt
def handle_webhook(request: HttpRequest) -> HttpResponse:
    """
    Python-telegram-bot request handler view.

    Used by Telegram to deliver post updates
    """
    if request.GET.get("secret") != settings.TELEGRAM_WEBHOOK_SECRET:
        return HttpResponse("Access Denied", status=403)

    update_json = json.loads(request.body)
    update = Update.de_json(update_json, bot)
    dispatcher.process_update(update)

    return HttpResponse("OK")


# TODO: add POST form to this endpoint
@csrf_exempt
def handle_set_webhook(request: HttpRequest) -> HttpResponse:
    """
    Set webhook endpoint view

    Used manually to set webhook. This implemented as endpoint,
    because with command we can't get current domain.
    """

    webhook_url = request.build_absolute_uri(reverse("bot:handle-webhook"))
    webhook_url_with_secret = f"%s?secret=%s" % (
        webhook_url, settings.TELEGRAM_WEBHOOK_SECRET
    )

    try:
        bot.set_webhook(webhook_url_with_secret)
    except Exception as e:
        return HttpResponse(f"Error: {e}", status=500)

    return HttpResponse(f"Webhook set is ok", status=200)
