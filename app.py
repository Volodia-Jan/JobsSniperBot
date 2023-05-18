from aiogram.utils.executor import start_webhook

from loader import bot, dp
from handlers import dp
from utils import WebhookConfig


async def on_startup(dp):
    await bot.set_webhook(WebhookConfig.url)


async def on_shutdown(dp):
    await bot.delete_webhook()


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WebhookConfig.path,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WebhookConfig.host,
        port=WebhookConfig.port,
    )