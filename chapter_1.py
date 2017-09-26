import tkinter as tk


root = tk.Tk()
root.title('I am a Top Level Widget, parent to the other widgets')
# Create frame widget for placing the menu
menu_bar = tk.Frame(root, relief=tk.RAISED, bd=2)
menu_bar.pack(fill=tk.X)

# Create Menu widget 1 and sub menu 1
menu_button = tk.Menubutton(menu_bar, text="Menu Button Widget 0")
menu_button.pack(side=tk.LEFT)
# menu widget
menu = tk.Menu(menu_button, tearoff=0)
menu_button['menu'] = menu
menu.add('command', label='Menu Widget 1')

# Create Menu 2 and submenu 2
menu_button_2 = tk.Menubutton(menu_bar, text='Menu 2')
menu_button_2.pack(side=tk.LEFT)
menu_2 = tk.Menu(menu_button_2, tearoff=0)
menu_button_2['menu'] = menu_2
menu_2.add('command', label='Sub Menu 2')

#
#
# frame_1 and its contents
#

# Creating a Frame
frame_1 = tk.Frame(root, bd=2, relief=tk.SUNKEN)
frame_1.pack(side=tk.LEFT)

# add label to frame_1
tk.Label(frame_1, text='I am a Label widget').pack()

# add Entry widget to frame_1
tv = tk.StringVar()
tk.Entry(frame_1, textvariable=tv).pack()
tv.set('I am an entry widget')

# add button widget to frame_1
tk.Button(frame_1, text='Button widget').pack()

# add check button widget to frame_1
tk.Checkbutton(frame_1, text='CheckButton Widget').pack()

# Add radio buttons  to frame_1
tk.Radiobutton(frame_1, text='Radio button un', value=1).pack()
tk.Radiobutton(frame_1, text='Radio button dos', value=2).pack()
tk.Radiobutton(frame_1, text='Radio button tres', value=3).pack()

# add OptionMenu Widget
tk.Label(frame_1, text='Example of OptionMenu Widget:').pack()
tk.OptionMenu(frame_1, '', 'Option A', 'Option B', 'Option C').pack()

# adding image
tk.Label(frame_1, text='Image Fun with Bitmap Class:').pack()
image = tk.BitmapImage(file='gir.xbm')
label = tk.Label(frame_1, image=image)
label.image = image
label.pack()

#
#
# frame_2 and widgets it contains

# create another frame(frame_2) to hold a list box, spinbox widget, scale Widget:
frame_2 = tk.Frame(root, bd=2, relief=tk.GROOVE)
frame_2.pack(side=tk.RIGHT)

# add photoimage Class Widget to frame_2
tk.Label(frame_2, text='Image displayed with \nPhotoImage Class Widget:').pack()
dance_photo = tk.PhotoImage(file='dance.gif')
dance_photo_label = tk.Label(frame_2, image=dance_photo)
dance_photo_label.image = dance_photo
dance_photo_label.pack()

# add Listbox Class Widget to frame_2
tk.Label(frame_2, text='Below is an example of listbox widget:').pack()
listbox = tk.Listbox(frame_2, height=4)
for line in ['Listbox Choice 1', 'Choice 2', 'Choice 3', 'Choice 4']:
    listbox.insert(tk.END, line)
listbox.pack()

# spinbox widget
tk.Label(frame_2, text='Below is an example of spinbox:').pack()
tk.Spinbox(frame_2, values=(1, 2, 4, 8, 10)).pack()

# scale widget
tk.Scale(frame_2, from_=0.0, to=100.0, label='Scale Widget', orient=tk.HORIZONTAL).pack()

# LabelFrame
label_frame = tk.LabelFrame(frame_2, text='LabelFrame', padx=10, pady=10)
label_frame.pack(padx=10, pady=10)
tk.Entry(label_frame).pack()

tk.Message(frame_2, text='I am a Message widget').pack()

#
#
# Frame 3
#

frame_3 = tk.Frame(root, bd=2, relief=tk.SUNKEN)

# text widget and associated Scrollbar widget
text = tk.Text(frame_3, height=10, width=40)
file_object = open('textcontent.txt')
file_content = file_object.read()
file_object.close()
text.insert(tk.END, file_content)
text.pack(side=tk.LEFT, fill=tk.X, padx=5)

# add Scrollbar widget to the text widget
scrollbar = tk.Scrollbar(frame_3, orient=tk.VERTICAL, command=text.yview)
scrollbar.pack()
text.configure(yscrollcommand=scrollbar.set)
frame_3.pack()

#
#
# Frame 4
#

frame_4 = tk.Frame(root).pack()

canvas = tk.Canvas(frame_4, bg='white', width=340, height=80)
canvas.pack()
canvas.create_oval(20, 15, 60, 60, fill='red')
canvas.create_oval(40, 15, 60, 60, fill='grey')
canvas.create_text(130, 38, text='I am a Canvas Widget', font=('arial', 8, 'bold'))

#
#
# A paned window widget
#

tk.Label(root, text='Below is an example of Paned Window Widget:').pack()
tk.Label(root, text='Notice you can adjust the size of each pane by dragging it').pack()
paned_window_1 = tk.PanedWindow()
paned_window_1.pack(fill=tk.BOTH, expand=2)
left_pane_text = tk.Text(paned_window_1, height=6, width=15)
paned_window_1.add(left_pane_text)
paned_window_2 = tk.PanedWindow(paned_window_1, orient=tk.VERTICAL)
paned_window_1.add(paned_window_2)
top_pane_text = tk.Text(paned_window_2, height=3, width=3)
paned_window_2.add(top_pane_text)
bottom_pane_text = tk.Text(paned_window_2, height=3, width=3)
paned_window_2.add(bottom_pane_text)

root.mainloop()
