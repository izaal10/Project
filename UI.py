import tkinter as tk
from PIL import Image, ImageTk

def resize_image(image_path, width, height):
    # Mengubah ukuran gambar sesuai lebar (width) dan tinggi (height) yang diinginkan
    image = Image.open(image_path)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(resized_image)

def start_recording():
    status_label.config(text="Recording...")

def stop_recording():
    status_label.config(text="Record Selesai")

def analyze_emotion():
    # Fungsi ini akan dijalankan ketika tombol "Ambil Hasil Emosi" ditekan
    # Di sini Anda dapat menambahkan kode untuk menganalisis hasil emosi
    # dan menampilkan hasilnya pada label "result_label" dan "suggestion_label"

    # Contoh hasil emosi dan akurasinya
    result_emotion = "Senang"
    accuracy = "80%"

    # Contoh saran atas hasil emosi
    suggestion = "Cobalah untuk tetap bahagia!"

    result_label.config(text=f"Hasil Emosi: {result_emotion} (Akurasi: {accuracy})")
    suggestion_label.config(text=f"Saran: {suggestion}")

# Membuat jendela utama
root = tk.Tk()
root.title("YourEmo")

# Mengatur ukuran jendela (lebar x tinggi)
root.geometry("800x600")

# Membuat label untuk menampilkan gambar
# Ganti "nama_gambar.png" dengan nama berkas gambar Anda dan pastikan berkas gambar ada dalam direktori yang sama dengan skrip Python Anda.
image_width = 200
image_height = 170
image_path = "microphone.png"
photo = resize_image(image_path, image_width, image_height)
image_label = tk.Label(root, image=photo)
image_label.pack(pady=10)

# Membuat label untuk menampilkan status rekaman
status_label = tk.Label(root, text="Tidak merekam", font=("Arial", 14))
status_label.pack()

# Membuat tombol "Record" dan "Ambil Hasil Emosi"
record_button = tk.Button(root, text="Record", command=start_recording, font=("Arial", 12))
record_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop Record", command=stop_recording, font=("Arial", 12))
stop_button.pack(pady=5)

analyze_button = tk.Button(root, text="Ambil Hasil Emosi", command=analyze_emotion, font=("Arial", 12))
analyze_button.pack(pady=5)

# Membuat label untuk menampilkan hasil emosi dan saran atas hasil emosi
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

suggestion_label = tk.Label(root, text="", font=("Arial", 12))
suggestion_label.pack(pady=5)

# Menjalankan program
root.mainloop()
