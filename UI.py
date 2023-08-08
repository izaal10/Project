import tkinter as tk
from PIL import Image, ImageTk

def resize_image(image_path, width, height):
    image = Image.open(image_path)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(resized_image)

def start_recording():
    status_label.config(text="Recording...")

def stop_recording():
    status_label.config(text="Record Selesai")

def analyze_emotion():
    # Your existing code for analyzing emotions
    result_emotion = "Senang"
    accuracy = "80%"

    # Contoh saran atas hasil emosi
    suggestion = "Cobalah untuk tetap bahagia!"

    result_label.config(text=f"Hasil Emosi: {result_emotion} (Akurasi: {accuracy})")
    suggestion_label.config(text=f"Saran: {suggestion}")

root = tk.Tk()
root.title("YourEmo")
root.geometry("800x600")

# Load the background image
background_image = Image.open("bg.png")  # Replace with your background image
background_photo = ImageTk.PhotoImage(background_image)

# Create a Canvas for the background
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

# Display the background image on the Canvas
canvas.create_image(0, 0, anchor=tk.NW, image=background_photo)

# Your other widgets
image_width = 200
image_height = 170
image_path = "record button.png"
photo = resize_image(image_path, image_width, image_height)
image_label = tk.Label(canvas, image=photo)
image_label.place(x=300, y=50)

status_label = tk.Label(canvas, text="Tidak merekam", font=("Arial", 14))
status_label.place(x=330, y=250)

record_button_image = Image.open("ANALYZE BUTTON.png")  # Replace with your transparent button image
record_button_photo = ImageTk.PhotoImage(record_button_image)
record_button = tk.Button(canvas, image=record_button_photo, command=start_recording, bd=0)
record_button.place(x=300, y=300)

# Load the transparent image for the "Stop Record" button
stop_button_image = Image.open("STOP BUTTON.png")  # Replace with your transparent button image
stop_button_photo = ImageTk.PhotoImage(stop_button_image)
stop_button = tk.Button(canvas, image=stop_button_photo, command=stop_recording, bd=0)
stop_button.place(x=400, y=300)

# Load the transparent image for the "Analyze" button
analyze_button_image = Image.open("find BUTTON.png")  # Replace with your transparent button image
analyze_button_photo = ImageTk.PhotoImage(analyze_button_image)
analyze_button = tk.Button(canvas, image=analyze_button_photo, command=analyze_emotion, bd=0)
analyze_button.place(x=300, y=380)

result_label = tk.Label(canvas, text="", font=("Arial", 12))
result_label.place(x=330, y=470)

suggestion_label = tk.Label(canvas, text="", font=("Arial", 12))
suggestion_label.place(x=330, y=500)

root.mainloop()
