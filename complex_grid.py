import tkinter as tk

root = tk.Tk()
root.title('Find and Replace')

tk.Label(root, text="Find: ").grid(row=0, column=0, sticky=tk.E)
tk.Entry(root, width=60).grid(row=0, column=1, padx=2, pady=2, sticky=tk.W + tk.E, columnspan=9)

tk.Label(root, text="Replace: ").grid(row=1, column=0, sticky=tk.E)
tk.Entry(root, width=60).grid(row=1, column=1, padx=2, pady=2, sticky=tk.W + tk.E, columnspan=9)

tk.Button(root, text="Find").grid(row=0, column=10, sticky=tk.E+tk.W, padx=2, pady=2)
tk.Button(root, text="Find All").grid(row=1, column=10, sticky=tk.E+tk.W, padx=2, pady=2)
tk.Button(root, text="Replace").grid(row=2, column=10, sticky=tk.E+tk.W, padx=2, pady=2)
tk.Button(root, text="Replace All").grid(row=3, column=10, sticky=tk.E+tk.W, padx=2, pady=2)

tk.Checkbutton(root, text="Match Whole Word Only").grid(row=2, column=1, columnspan=4, sticky=tk.W)
tk.Checkbutton(root, text="Match Case").grid(row=3, column=1, columnspan=4, sticky=tk.W)
tk.Checkbutton(root, text="Wrap Around").grid(row=4, column=1, columnspan=4, sticky=tk.W)

tk.Label(root, text="Direction: ").grid(row=2, column=3, columnspan=4, sticky=tk.E)
tk.Radiobutton(root, text="up", value=1).grid(row=3, column=4, columnspan=4, sticky=tk.E)
tk.Radiobutton(root, text="down", value=2).grid(row=3, column=5, columnspan=2, sticky=tk.E)

root.mainloop()