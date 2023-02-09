import tkinter as tk
import time
from ppadb.client import Client as AdbClient

client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()

def process():

    e1 = float(e_delay.get())
    e2 = int(e_total.get())
    e3 = float(e_shutter.get())

    text_info = "Recap:\n\n{} takes every {}s ({}s shutter speed)\n\nTotal Duration: {}s\n\nFinal video render:\n{}s movie @ 60fps\n{}s movie @ 30fps".format(e2, e1+e3, e3, (e1+e3)*e2, e2/60, e2/30)

    info.insert(tk.END, text_info)


    devices = client.devices()

    if len(devices) != 0:

        start_button.configure(state="normal", borderwidth=5)
    
    else:

        start_button.configure(state="disabled", borderwidth=2)


def connect():

    devices = client.devices()

    if len(devices) == 0:
        
        status_text.configure(text="No devices found")
        canvas.itemconfig(status_light, fill="red")

        device = "<NaN>"

    else:
        
        device = devices[0]
        status_text.configure(text=f"Connected to {device}")
        canvas.itemconfig(status_light, fill="green")

        if e_delay.get() != "" and e_total.get() != "" and e_shutter.get() != "":

            start_button.configure(state="normal", borderwidth=5)



def start():
    
    device = devices[0]
    total_amount_of_takes = int(e_total.get())
    shutter_speed = float(e_shutter.get())
    delay_between_takes = float(e_delay.get())

    for i in range(total_amount_of_takes):
        device.shell('input keyevent 25')
        time.sleep(shutter_speed+delay_between_takes)


BG_COLOR = "#1d1f29"
FG_COLOR = "white"
INPUT_COLOR = "#383b4d"

root = tk.Tk()

root.configure(bg="#1d1f29")

tk.Label(root, text="TL INTERVALOMETER", font=("Helvetica", 25), bg=BG_COLOR, foreground="#e0e5ff", justify="center", pady=30).grid(row=0, columnspan=10)
tk.Label(root, text="Delay between two takes :", bg=BG_COLOR, foreground=FG_COLOR, pady=20).grid(row=1, sticky="e")
tk.Label(root, text="Total amount of takes :", bg=BG_COLOR, foreground=FG_COLOR, pady=20).grid(row=2, sticky="e")
tk.Label(root, text="Shutter speed :", bg=BG_COLOR, foreground=FG_COLOR, pady=20).grid(row=3, sticky="e")
tk.Label(root, text="sec", bg=BG_COLOR, foreground=FG_COLOR).grid(row=1, column=2, sticky="w")
tk.Label(root, text="sec", bg=BG_COLOR, foreground=FG_COLOR).grid(row=3, column=2, sticky="w")

process_button = tk.Button(root, text="PROCESS", command=process, bg=INPUT_COLOR, foreground=FG_COLOR)
connect_button = tk.Button(root, text="CONNECT", command=connect, bg=INPUT_COLOR, foreground=FG_COLOR)
start_button = tk.Button(root, text="START", font=("Helvetica", 12, "bold"), command=start, bg=INPUT_COLOR, foreground=FG_COLOR, state="disabled", height=2, width= 12)

info = tk.Text(root, font="Helvetica", bg=BG_COLOR, foreground=FG_COLOR, height=10, width=45)
info.grid(row=5, columnspan=10)

e_delay = tk.Entry(root, width=5, justify="center", bg=INPUT_COLOR, foreground=FG_COLOR)
e_total = tk.Entry(root, width=6, justify="center", bg=INPUT_COLOR, foreground=FG_COLOR)
e_shutter = tk.Entry(root, width=5, justify="center", bg=INPUT_COLOR, foreground=FG_COLOR)

canvas = tk.Canvas(root, height=11, width=11, bg=BG_COLOR, highlightthickness=0)
status_light = canvas.create_oval(0, 0, 10, 10, fill="gray", outline="")
status_text = tk.Label(root, text="Not connected", font=("Helvetica", 10), bg=BG_COLOR, foreground=FG_COLOR, width=50, anchor="w")

canvas.grid(row=6, column=0, sticky="e", padx=5)

e_delay.grid(row=1, column=1)
e_total.grid(row=2, column=1)
e_shutter.grid(row=3, column=1)

status_text.grid(row=6, column=1, sticky="w", columnspan=9)

process_button.grid(row=2, column=4)
start_button.grid(row=2, column=8)
connect_button.grid(row=6, pady=20)

root.mainloop()
