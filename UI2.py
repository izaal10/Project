import tkinter as tk
from PIL import Image, ImageTk
import threading
import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
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
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        audio_frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

def save_recorded_audio():
    global audio_frames
    wf = wave.open(OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pyaudio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(audio_frames))
    wf.close()

def analyze_emotion():
    # Implement your emotion analysis logic here based on the recorded audio data
    # and display the result on result_label and suggestion_label

    # Dummy result for demonstration purposes
    result_emotion = "Happy"
    accuracy = "80%"
    suggestion = "Keep up the good mood!"

    result_label.config(text=f"Emotion Result: {result_emotion} (Accuracy: {accuracy})")
    suggestion_label.config(text=f"Suggestion: {suggestion}")

# Create the main window
root = tk.Tk()
root.title("Emotion Analysis App")

# Set the window size (width x height)
root.geometry("800x600")

# Create a label to display the image
image_width = 200
image_height = 170
image_path = "microphone.png"  # Replace with your actual image filename
photo = resize_image(image_path, image_width, image_height)
image_label = tk.Label(root, image=photo)
image_label.pack(pady=10)

# Create a label to display the recording status
status_label = tk.Label(root, text="Not recording", font=("Arial", 14))
status_label.pack()

# Create buttons for Record, Stop Record, and Analyze Emotion
record_button = tk.Button(root, text="Record", command=start_recording, font=("Arial", 12))
record_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop Record", command=stop_recording, font=("Arial", 12))
stop_button.pack(pady=5)

analyze_button = tk.Button(root, text="Analyze Emotion", command=analyze_emotion, font=("Arial", 12))
analyze_button.pack(pady=5)

# Create labels to display the emotion analysis result and suggestion
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

suggestion_label = tk.Label(root, text="", font=("Arial", 12))
suggestion_label.pack(pady=5)

# Run the main event loop
root.mainloop()
