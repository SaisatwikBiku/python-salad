import qrcode
import tkinter as tk
from tkinter import filedialog

def generate_qrcode():
    url = url_entry.get()
    if url:
        myqr = qrcode.make(url)
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            myqr.save(file_path)
            result_label.config(text="QR Code saved successfully!")
        else:
            result_label.config(text="QR Code generation cancelled.")
    else:
        result_label.config(text="Please enter a URL.")

# Create main window
root = tk.Tk()
root.title("QR Code Generator")

# URL input
url_label = tk.Label(root, text="Enter the URL:")
url_label.pack()
url_entry = tk.Entry(root)
url_entry.pack()

# Generate button
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qrcode)
generate_button.pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
