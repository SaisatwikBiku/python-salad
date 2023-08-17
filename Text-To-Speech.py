import pyttsx3
import tkinter as tk
from tkinter import messagebox

def text_to_speech():
    input_text = text_entry.get()
    if not input_text:
        messagebox.showerror("Error", "Please enter some text.")
        return

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    # You can change the voice, rate, and volume if needed.
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Using the default voice
    engine.setProperty('rate', 150)  # Speed of speech (words per minute)
    engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)

    # Convert text to speech
    engine.say(input_text)

    # Wait for the speech to finish
    engine.runAndWait()

# Create the main application window
app = tk.Tk()
app.title("Text-to-Speech Converter")

# Create and configure widgets
text_entry = tk.Entry(app, width=50)
text_entry.pack(pady=10)

convert_button = tk.Button(app, text="Convert to Speech", command=text_to_speech)
convert_button.pack(pady=5)

# Start the main event loop
app.mainloop()
