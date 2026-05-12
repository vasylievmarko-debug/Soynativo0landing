import whisper
import numpy as np
from queue import Queue
import threading

class SpeechToText:
    def __init__(self, model_size="base", language="ru"):
        self.model = whisper.load_model(model_size)
        self.language = language
        self.result_queue = Queue()

    def transcribe_audio(self, audio_data):
        if audio_data is None or len(audio_data) == 0:
            return None

        try:
            result = self.model.transcribe(
                audio_data,
                language=self.language,
                fp16=False,
                task="transcribe"
            )
            return result["text"].strip()
        except Exception as e:
            print(f"Transcription error: {e}")
            return None

    def transcribe_async(self, audio_data):
        def worker():
            text = self.transcribe_audio(audio_data)
            if text:
                self.result_queue.put(text)

        thread = threading.Thread(target=worker, daemon=True)
        thread.start()

    def get_result(self):
        try:
            return self.result_queue.get(block=False)
        except:
            return None
