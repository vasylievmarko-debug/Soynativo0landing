#!/usr/bin/env python3
import sys
import os
import time
import threading
from dotenv import load_dotenv

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from audio_capture import AudioCapture
from speech_to_text import SpeechToText
from translator import Translator
from ui import SubtitleWindow

load_dotenv()

class AudioSubtitleTranslator:
    def __init__(self):
        self.audio_capture = AudioCapture(sample_rate=16000, chunk_duration=1.0)
        self.stt = SpeechToText(model_size="base", language="en")
        self.translator = Translator(source_lang="en", target_lang="ru")
        self.ui = SubtitleWindow("Audio Subtitle Translator (EN → РУ)")

        self.is_running = False
        self.last_english_text = ""
        self.last_russian_text = ""

    def process_audio(self):
        silence_counter = 0
        silence_threshold = 5

        while self.is_running:
            audio_chunk = self.audio_capture.get_audio_chunk()

            if audio_chunk is not None and len(audio_chunk) > 0:
                silence_counter = 0
                self.ui.update_status("Processing audio...")

                english_text = self.stt.transcribe_audio(audio_chunk)

                if english_text and english_text != self.last_english_text:
                    self.last_english_text = english_text
                    self.ui.update_status("Translating...")

                    russian_text = self.translator.translate(english_text)
                    self.last_russian_text = russian_text or english_text

                    self.ui.update_subtitles(english_text, self.last_russian_text)
                    self.ui.update_status("Listening...")
            else:
                silence_counter += 1
                if silence_counter > silence_threshold:
                    self.ui.update_status("Waiting for speech...")

            time.sleep(0.1)

    def start(self):
        self.is_running = True
        self.audio_capture.start()

        processing_thread = threading.Thread(target=self.process_audio, daemon=True)
        processing_thread.start()

        try:
            self.ui.run()
        except KeyboardInterrupt:
            print("\nShutting down...")
        finally:
            self.stop()

    def stop(self):
        self.is_running = False
        self.audio_capture.stop()
        self.ui.close()

if __name__ == "__main__":
    translator = AudioSubtitleTranslator()
    translator.start()
