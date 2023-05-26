import logging

from aiogram.utils.executor import start_webhook

from loader import bot, dp, session_manager
from handlers import dp
from utils import WebhookConfig


async def on_startup(dp):
    logging.debug("JobsSniperBot is running")
    session_manager.create_tables()
    session_manager.close_session()
    logging.debug("Setting webhook url")
    await bot.set_webhook(WebhookConfig.url)


async def on_shutdown(dp):
    logging.debug("JobsSniperBot is shutting down")
    logging.debug("Deleting webhook url")
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