import os
import json

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

"""
Engligh to French and French to English translator, using IBM Watson
"""

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def englishToFrench(englishText):
    """
    Engligh to French translator, using IBM Watson
    """
    #write the code here
    if englishText=='':
        return None
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )

    language_translator.set_service_url(url)

    translation = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
    french_text = ''
    response = json.loads(json.dumps(translation))['translations']
    for k in response:
        french_text = french_text + k['translation']
    return french_text

def frenchToEnglish(frenchText):
    """
    French to English translator, using IBM Watson
    """
    #write the code here
    if frenchText=='':
        return None
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )

    language_translator.set_service_url(url)

    translation = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()
    english_text = ''
    response = json.loads(json.dumps(translation))['translations']
    for k in response:
        english_text = english_text + k['translation']
    return english_text
