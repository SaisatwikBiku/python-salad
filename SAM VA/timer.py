import tkinter as tk
import time

def set_timer():
    minutes = int(minutes_entry.get())
    seconds = int(seconds_entry.get())
    total_seconds = minutes*60 + seconds
    end_time = time.time() + total_seconds
    while time.time() < end_time:
        time_left = end_time - time.time()
        time_display.config(text=f"{int(time_left//60)}:{int(time_left%60):02d}")
        time_display.update()
    time_display.config(text="Time's up!")

window = tk.Tk()
window.title("Timer")
window.geometry("300x200")

minutes_label = tk.Label(window, text="Minutes:")
minutes_label.pack()
minutes_entry = tk.Entry(window)
minutes_entry.pack()

seconds_label = tk.Label(window, text="Seconds:")
seconds_label.pack()
seconds_entry = tk.Entry(window)
seconds_entry.pack()

start_button = tk.Button(window, text="Start", command=set_timer)
start_button.pack()

time_display = tk.Label(window, font=("Arial", 30))
time_display.pack()

window.mainloop()
