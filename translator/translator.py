import time

import requests

from errors.validators import ResponseError


class Translator:
    def __init__(self, data, url, source, target):
        self.data = data
        self.url = url
        self.source = source
        self.target = target

    def translate(self) -> dict:
        """
        Method for creating a dictionary with translated advices pulled from UserAdvices class.
        If there is more advices to translate then 10. Wait 1 min. This is done due to API response 429 Slow down
        :return: dict of translated advices
        """
        translated_dict = {}

        for index, (_id, advice) in enumerate(self.data.items(), start=1):
            if index % 10 == 0:
                time.sleep(60)
            pload = {
                "q": advice,
                "source": self.source,
                "target": self.target,
            }
            res = requests.post(self.url, params=pload)
            if not res.ok:
                raise ResponseError(f"{res.text}")

            translated_dict[_id] = res.json().get("translatedText")

        return translated_dict
