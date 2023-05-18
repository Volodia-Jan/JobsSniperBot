from dotenv import load_dotenv
# from utils import BotResponses
import os

from utils.text_responses import BotResponses

load_dotenv()
botResponses = BotResponses.get_instance()


class BotConfig:
    token = os.getenv("BOT_TOKEN")
    admins_ids = os.getenv("ADMINS_IDS").split(',')


class BotResponsesConfig:
    startResponse = botResponses.get_response("startResponse")
    helpResponse = botResponses.get_response("helpResponse")
    # filterResponse = botResponses.get_response("filterResponse")
    # jobResponse = botResponses.get_response("jobResponse")


class WebhookConfig:
    path = os.getenv("WEBHOOK_PATH")
    url = os.getenv("WEBHOOK_URL")
    host = os.getenv("WEBAPP_HOST")
    port = int(os.getenv("WEBAPP_PORT"))


class DbConfig:
    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_NAME")
