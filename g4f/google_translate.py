from googletrans import Translator

def translate_text_to_kazakh(text):
    translator = Translator()
    translated = translator.translate(text, src='auto', dest='kk')
    return translated.text
