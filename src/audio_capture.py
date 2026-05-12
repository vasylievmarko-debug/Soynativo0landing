import sounddevice as sd
import numpy as np
from collections import deque
import threading
import time

class AudioCapture:
    def __init__(self, sample_rate=16000, chunk_duration=0.5):
        self.sample_rate = sample_rate
        self.chunk_size = int(sample_rate * chunk_duration)
        self.audio_buffer = deque(maxlen=self.chunk_size * 10)
        self.is_recording = False
        self.stream = None

    def audio_callback(self, indata, frames, time_info, status):
        if status:
            print(f"Audio stream error: {status}")
        self.audio_buffer.extend(indata[:, 0])

    def start(self):
        self.is_recording = True
        self.stream = sd.InputStream(
            samplerate=self.sample_rate,
            channels=1,
            blocksize=self.chunk_size,
            callback=self.audio_callback
        )
        self.stream.start()
        print("Audio capture started")

    def stop(self):
        self.is_recording = False
        if self.stream:
            self.stream.stop()
            self.stream.close()
        print("Audio capture stopped")

    def get_audio_chunk(self):
        if len(self.audio_buffer) >= self.chunk_size:
            chunk = np.array(list(self.audio_buffer))[-self.chunk_size:]
            return chunk.astype(np.float32)
        return None
