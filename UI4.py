import tkinter as tk
from PIL import Image, ImageTk
import threading
import struct
import wave
from pvrecorder import PvRecorder

CHUNK = 1024
# FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
OUTPUT_FILENAME = "recorded_audio.wav"

def resize_image(image_path, width, height):
    image = Image.open(image_path)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(resized_image)

def start_recording():
    global audio_frames
    audio_frames = []
    status_label.config(text="Recording...")
    threading.Thread(target=record_audio).start()

def stop_recording():
    status_label.config(text="Record Selesai")
    save_recorded_audio()

def record_audio():
    global audio_frames
    recorder = PvRecorder(device_index=2, frame_length=512)
    recorder.start()

    try:
        while True:
            frame = recorder.read()
            audio_frames.extend(frame)
    except KeyboardInterrupt:
        recorder.stop()
    finally:
        recorder.delete()

def save_recorded_audio():
    global audio_frames
    with wave.open(OUTPUT_FILENAME, 'wb') as f:
        f.setnchannels(CHANNELS)
        f.setsampwidth(pyaudio.get_sample_size(FORMAT))
        f.setframerate(RATE)
        f.writeframes(b''.join(audio_frames))

def analyze_emotion():
    # Implement your emotion analysis logic here based on the recorded audio data
    # and display the result on result_label and suggestion_label

    # Dummy result for demonstration purposes
    result_emotion = "Happy"
    accuracy = "80%"
    suggestion = "Keep up the good mood!"

    result_label.config(text=f"Emotion Result: {result_emotion} (Accuracy: {accuracy})")
    suggestion_label.config(text=f"Suggestion: {suggestion}")

# ... (rest of the code remains unchanged)
