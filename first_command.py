import tkinter as tk


def callback():
    print("you pressed the button")


def other_callback(event):
    print("You pressed the other button")

root = tk.Tk()
tk.Button(root, text="Press the Button", command=callback).grid(row=0, column=0)
button = tk.Button(root, text="Press this other Button")
button.bind("<Button-1>", other_callback)
button.grid(row=0, column=1)

root.mainloop()

