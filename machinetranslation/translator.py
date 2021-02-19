"""
A module used to interact with IBM Watson Language Translator API. Translates
from English to French and English to German.
"""
import os
import re
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

API_KEY = os.environ.get("API_KEY")
API_URL = os.environ.get("API_URL")

authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(
    version= "2018-05-01",
    authenticator = authenticator
)

language_translator.set_service_url(API_URL)


def english_to_french(text_to_translate):
    """
    Translates text from English to French
    """

    if text_to_translate:
        #check if numbers are in string, which causes odd errors.
        number = re.search(r'\d+', text_to_translate)
        if number:
            return "Please refrain from using numbers."

        #drop case of text to prevent erroneous translations
        text_lowercase = text_to_translate.lower()
        result = language_translator.translate(
            text = text_lowercase,
            model_id = 'en-fr'
        ).get_result()
    else:
        return "Lack of textual input."

    return result["translations"][0]["translation"]

def english_to_german(text_to_translate):
    """
    Translates text from English to German
    """

    if text_to_translate:
        #check if numbers are in string, which causes odd errors.
        number = re.search(r'\d+', text_to_translate)
        if number:
            return "Please refrain from using numbers."

        #drop case of text to prevent erroneous translations
        text_lowercase = text_to_translate.lower()
        result = language_translator.translate(
            text = text_lowercase,
            model_id = 'en-de'
        ).get_result()
    else:
        return "Lack of textual input."

    return result["translations"][0]["translation"]
    