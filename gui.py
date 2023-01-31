import tkinter as tk


def process():

    info = tk.Text(root, font="Helvetica")

    e1 = int(e_delay.get())
    e2 = int(e_total.get())
    e3 = int(e_shutter.get())

    text_info = "Recap:\n\n{} takes every {}s ({}s shutter speed)\n\nTotal Duration: {}s\n\nFinal video render:\n{}s movie @ 60fps\n{}s movie @ 30fps".format(e2, e1, e3, (e1+e3)*e2, e2/60, e2/30)

    info.insert(tk.END, text_info)
    info.grid(row=4)



root = tk.Tk()

tk.Label(root, text="Delay between two takes :").grid(row=0)
tk.Label(root, text="Total amount of takes :").grid(row=1)
tk.Label(root, text="Shutter speed :").grid(row=2)
tk.Label(root, text="sec").grid(row=0, column=2)
tk.Label(root, text="sec").grid(row=2, column=2)

process_button = tk.Button(root, text="PROCESS", command=process)

e_delay = tk.Entry(root, width=5, justify="center")
e_total = tk.Entry(root, width=7, justify="center")
e_shutter = tk.Entry(root, width=5, justify="center")

e_delay.grid(row=0, column=1)
e_total.grid(row=1, column=1)
e_shutter.grid(row=2, column=1)

process_button.grid(row=3, column=1)

root.mainloop()
