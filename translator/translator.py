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

        translated_dict = {}

        for index, (_id, advice) in enumerate(self.data.items()):
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
