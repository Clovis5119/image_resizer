"""
See GUI sketch for reference.

Root window should have:
 ONE column
 FIVE rows

"""

import tkinter as tk
import ttkbootstrap as ttk
from tkinter import font

root = tk.Tk()
root.title('Image Resizer')
root.geometry('600x600')
root.minsize(600, 800)
root.maxsize(600, 1200)

default_font = font.nametofont("TkDefaultFont")
default_font.configure(family='Roboto', size=11)

# Configure the grid weights and sizes
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=0, minsize=50)
root.rowconfigure(1, weight=0, minsize=50)
root.rowconfigure(2, weight=5)
root.rowconfigure(3, weight=10)
root.rowconfigure(4, weight=0, minsize=50)

# Create five frames
frame1_path = ttk.Frame(root, borderwidth=1, relief='raised')
frame2_dims = ttk.Frame(root, borderwidth=1, relief='raised')
frame3_files = ttk.Frame(root, borderwidth=1, relief='raised')
frame4_preview = ttk.Frame(root, borderwidth=1, relief='raised')
frame5_save = ttk.Frame(root, borderwidth=1, relief='raised')

# Place each frame on the grid
frame1_path.grid(column=0, row=0, sticky='nsew')
frame2_dims.grid(column=0, row=1, sticky='nsew')
frame3_files.grid(column=0, row=2, sticky='nsew')
frame4_preview.grid(column=0, row=3, sticky='nsew')
frame5_save.grid(column=0, row=4, sticky='nsew')

# Create Frame 1 widgets
lbl_path = ttk.Label(frame1_path, text='Path:')
ent_path = ttk.Entry(frame1_path, width=40)
btn_path = ttk.Button(frame1_path, text='...', width=2)
check_ow = ttk.Radiobutton(frame1_path, text='Overwrite', value='overwrite')
check_copy = ttk.Radiobutton(frame1_path, text='Create Copy', value='copy')

# Place Frame 1 widgets
lbl_path.place(x=12, y=13)
ent_path.place(x=60, y=13)
btn_path.place(x=315, y=9)
check_ow.place(x=365, y=13)
check_copy.place(x=465, y=13)

# Place Frame 2 widgets
lbl_w = ttk.Label(frame2_dims, text='W:')
ent_w = ttk.Entry(frame2_dims, width=15)
lbl_h = ttk.Label(frame2_dims, text='H:')
ent_h = ttk.Entry(frame2_dims, width=15)
ratio_toggle = ttk.Checkbutton(frame2_dims, text='Keep Aspect Ratio')

# Place Frame 2 widgets
lbl_w.place(x=29, y=13)
ent_w.place(x=60, y=13)
lbl_h.place(x=180, y=13)
ent_h.place(x=210, y=13)
ratio_toggle.place(x=365, y=13)

# menu_options = ['Width', 'Height', 'Both']
# menu_var = StringVar()
# menu_var.set(menu_options[0])
# side_menu = OptionMenu(lbl_frame, menu_var, *menu_options)
# side_menu.pack()

root.mainloop()