from google.cloud import translate_v2
import os

class Translator:
    def __init__(self, source_lang="en", target_lang="ru"):
        self.source_lang = source_lang
        self.target_lang = target_lang

        credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        if credentials_path and os.path.exists(credentials_path):
            self.client = translate_v2.Client()
        else:
            self.client = None
            print("Warning: Google Cloud credentials not found. Using fallback translation.")

    def translate(self, text):
        if not text:
            return None

        if self.client is None:
            return self._fallback_translate(text)

        try:
            result = self.client.translate_text(
                source_language=self.source_lang,
                target_language=self.target_lang,
                values=[text]
            )
            return result["translations"][0]["translatedText"]
        except Exception as e:
            print(f"Translation error: {e}")
            return self._fallback_translate(text)

    def _fallback_translate(self, text):
        try:
            from deep_translator import GoogleTranslator
            translated = GoogleTranslator(
                source_language=self.source_lang,
                target_language=self.target_lang
            ).translate(text)
            return translated
        except Exception as e:
            print(f"Fallback translation failed: {e}")
            return text
