import tkinter as tk

root = tk.Tk()

tk.Button(root, text="Hello").pack(fill=tk.X)
tk.Button(root, text="World").pack(fill=tk.X)
tk.Button(root, text="Again").pack(fill=tk.X)


# Left to Right Widgets
tk.Button(root, text="Left").pack(side=tk.LEFT)
tk.Button(root, text="to").pack(side=tk.LEFT)
tk.Button(root, text="Right").pack(side=tk.LEFT)

root.mainloop()
