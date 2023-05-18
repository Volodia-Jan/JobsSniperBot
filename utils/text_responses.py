import json
import os


class BotResponses:
    _instance = None

    def __init__(self):
        self.responses = self._load_responses()

    @staticmethod
    def get_instance():
        if BotResponses._instance is None:
            BotResponses._instance = BotResponses()
        return BotResponses._instance

    @staticmethod
    def _load_responses():
        with open("responses.json", 'r', encoding='utf-8') as file:
            return json.load(file)

    def get_response(self, key):
        return self.responses.get(key, 'Вибачте, відповідь не знайдена.')
