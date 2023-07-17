from gtts import gTTS
import tkinter as tk
from tkinter import messagebox

def convert_text_to_speech():
    text = text_entry.get()
    if text:
        try:
            tts = gTTS(text=text, lang='en')
            tts.save('output.mp3')
            messagebox.showinfo('Success', 'Conversion complete!')
        except Exception as e:
            messagebox.showerror('Error', str(e))
    else:
        messagebox.showwarning('Warning', 'Please enter text.')

# Create the main window
window = tk.Tk()
window.title('Text to Speech Converter')

# Create a label and an entry field
label = tk.Label(window, text='Enter text:')
label.pack()
text_entry = tk.Entry(window, width=50)
text_entry.pack()

# Create a button to initiate conversion
convert_button = tk.Button(window, text='Convert', command=convert_text_to_speech)
convert_button.pack()

# Start the GUI event loop
window.mainloop()
