from dotenv import load_dotenv
load_dotenv()

import os

#Authenticate api
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

API_KEY = os.environ.get("API_KEY")
API_URL = os.environ.get("API_URL")

authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(
    version= "2018-05-01",
    authenticator = authenticator
)

language_translator.set_service_url(API_URL)


def englishToFrench():
    print("Please enter English text to be translated to French.")
    initial_text = input()

    result = language_translator.translate(
        text = initial_text,
        model_id = 'en-fr'
    ).get_result()
    print(result["translations"][0]["translation"])
    return result["translations"][0]["translation"]

if __name__ == "__main__":
    englishToFrench()