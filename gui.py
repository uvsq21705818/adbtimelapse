import tkinter as tk


def process():

    e1 = int(e_delay.get())
    e2 = int(e_total.get())
    e3 = int(e_shutter.get())

    text_info = "Recap:\n\n{} takes every {}s ({}s shutter speed)\n\nTotal Duration: {}s\n\nFinal video render:\n{}s movie @ 60fps\n{}s movie @ 30fps".format(e2, e1, e3, (e1+e3)*e2, e2/60, e2/30)

    info.insert(tk.END, text_info)


BG_COLOR = "#1d1f29"
FG_COLOR = "white"
INPUT_COLOR = "#383b4d"

root = tk.Tk()

root.configure(bg="#1d1f29")

tk.Label(root, text="TIMELAPSE INTERVALOMETER", font=("Helvetica", 20), bg=BG_COLOR, foreground="#e0e5ff", justify="center", pady=30).grid(row=0, columnspan=10)
tk.Label(root, text="Delay between two takes :", bg=BG_COLOR, foreground=FG_COLOR, pady=20).grid(row=1, sticky="e")
tk.Label(root, text="Total amount of takes :", bg=BG_COLOR, foreground=FG_COLOR, pady=20).grid(row=2, sticky="e")
tk.Label(root, text="Shutter speed :", bg=BG_COLOR, foreground=FG_COLOR, pady=20).grid(row=3, sticky="e")
tk.Label(root, text="sec", bg=BG_COLOR, foreground=FG_COLOR).grid(row=1, column=2, sticky="w")
tk.Label(root, text="sec", bg=BG_COLOR, foreground=FG_COLOR).grid(row=3, column=2, sticky="w")

process_button = tk.Button(root, text="PROCESS", command=process, bg=INPUT_COLOR, foreground=FG_COLOR)

info = tk.Text(root, font="Helvetica", bg=BG_COLOR, foreground=FG_COLOR, height=10, width=45)
info.grid(row=5, columnspan=10)

e_delay = tk.Entry(root, width=5, justify="center", bg=INPUT_COLOR, foreground=FG_COLOR)
e_total = tk.Entry(root, width=6, justify="center", bg=INPUT_COLOR, foreground=FG_COLOR)
e_shutter = tk.Entry(root, width=5, justify="center", bg=INPUT_COLOR, foreground=FG_COLOR)

e_delay.grid(row=1, column=1)
e_total.grid(row=2, column=1)
e_shutter.grid(row=3, column=1)

process_button.grid(row=2, column=6)

root.mainloop()
