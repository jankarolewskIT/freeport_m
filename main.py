from translator.translator import Translator
from user.advices import UserAdvices


def main(advice_url, trans_url):
    user_advice = UserAdvices()
    user_advice.validate_input()
    for _ in range(user_advice.number):
        user_advice.create_advices(advice_url)

    translator = Translator(user_advice.serialize_advice(), trans_url, "en", "pl")
    translated_advices = translator.translate()
    message = ""
    for key in user_advice.advices_dict:
        message += f"{user_advice.advices_dict.get(key)}  |  {translated_advices.get(key)}\n"

    print(message)


if __name__ == '__main__':
    ADVICE_URL = "https://api.adviceslip.com/advice"
    TRANS_URL = "https://libretranslate.de/translate"
    main(ADVICE_URL, TRANS_URL)
