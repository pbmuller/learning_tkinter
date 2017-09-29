import tkinter as tk



def callback(event):
    print(event.__dict__)
root = tk.Tk()

button = tk.Button(root, text="Button Bound to:\nKeyboard Enter and Mouse Click")
button.pack()
button.bind("<Button-1>", callback)
button.bind("<Return>", callback, add='+')

label1 = tk.Label(root, text="Entry is Bound to Mouseclick")

root.mainloop()