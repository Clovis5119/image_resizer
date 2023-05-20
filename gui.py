"""
See GUI sketch for reference.

"""

import tkinter as tk
import ttkbootstrap as ttk
from tkinter import font
from tkinter import filedialog
from PIL import ImageTk
from image import Imager


def browse_folder():
    """Open the folder browser."""
    folder_selected = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_selected)


def toggle_frames(*args):
    if frame3.winfo_viewable():
        root.geometry(f'{WIDTH_MIN}x{HEIGHT_MIN}')
        frame3.grid_remove()
        frame4.grid_remove()
        collapse_label.config(text='+')
        root.minsize(WIDTH_MIN, HEIGHT_MIN)
        root.maxsize(WIDTH_MIN, HEIGHT_MIN)
        root.resizable(False, False)
    else:
        frame3.grid()
        frame4.grid()
        root.geometry(f'{WIDTH_MIN}x800')
        collapse_label.config(text='-')
        root.minsize(WIDTH_MIN, 800)
        root.maxsize(1200, HEIGHT_MAX)
        root.resizable(True, True)


def on_frame_enter(*args):
    """Change the appearance"""
    frame2.configure(style='Hover.TFrame')
    collapse_label.configure(style='Hover.TLabel')


def on_frame_leave(*args):
    frame2.configure(style='Collapse.TFrame')
    collapse_label.configure(style='Collapse.TLabel')


IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png']
WIDTH_MIN, HEIGHT_MIN = 600, 178
WIDTH_MAX, HEIGHT_MAX = 600, 1200

# Main window config
root = tk.Tk()
root.title('Image Resizer')

root.geometry(f'{WIDTH_MIN}x{HEIGHT_MIN}')
root.minsize(WIDTH_MIN, HEIGHT_MIN)
root.resizable(False, False)

# Styling config
style = ttk.Style()
style.configure("Small.TButton", font=("TkDefaultFont", 8), padding=4)
style.configure('Collapse.TFrame', background='#e5e5e5')
style.configure('Hover.TFrame', background='#d6d6d6')
style.configure('Collapse.TLabel', background='#e5e5e5')
style.configure('Hover.TLabel', background='#d6d6d6')
# style.configure('Custom.Treeview', background='white', fieldbackground='white', foreground='black')
# style.configure('Custom.Treeview.Heading', background='white', foreground='black', relief='raised')
# style.map('Custom.Treeview', background=[('selected', 'light gray')], foreground=[('selected', 'black')])

default_font = font.nametofont("TkDefaultFont")
default_font.configure(family='Roboto', size=10)
entry_font = ('Roboto Medium', 10)

# Main grid config
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=0)              # Frame 1 - Config
root.rowconfigure(1, weight=0)              # Frame 2 - Expand/Collapse
root.rowconfigure(2, weight=1)              # Frame 2 - List
root.rowconfigure(3, weight=2)              # Frame 3 - Image
root.rowconfigure(4, weight=0)              # Frame 4 - Save

# Create five frames
frame1 = ttk.Frame(root, width=600, height=100)
frame2 = ttk.Frame(root, width=600, height=30, cursor="hand2")
frame3 = ttk.Frame(root, width=600, height=300)
frame4 = ttk.Frame(root, width=600, height=350)
frame5 = ttk.Frame(root, width=600, height=50)

# Place each frame on the grid
frame1.grid(column=0, row=0, sticky='nsew', pady=10)
frame2.grid(column=0, row=1, sticky='nsew')
frame3.grid(column=0, row=2, sticky='nsew')
frame3.grid_propagate(False)
frame3.grid_remove()
frame3.columnconfigure(0, weight=0)
frame3.columnconfigure(1, weight=1)
frame3.rowconfigure(0, weight=1)

frame4.grid(column=0, row=3, sticky='nsew')
frame4.grid_propagate(False)
frame4.grid_remove()

frame5.grid(column=0, row=4, sticky='nsew', pady=10)
frame5.columnconfigure(0, weight=0)

frame2.bind("<Button-1>", toggle_frames)
frame2.bind("<Enter>", on_frame_enter)
frame2.bind("<Leave>", on_frame_leave)


"""     WIDGET CREATION     """

# Folder selection
folder_label = ttk.Label(frame1, text='Folder:')
folder_entry = ttk.Entry(frame1)
folder_button = ttk.Button(
    master=frame1,
    text='...',
    command=browse_folder,
    cursor="hand2")

# Overwrite or Copy
radio_var = tk.StringVar()
overwrite_radio = ttk.Radiobutton(
    master=frame1,
    text='Overwrite',
    value='overwrite',
    variable=radio_var,
    cursor="hand2")
copy_radio = ttk.Radiobutton(
    master=frame1,
    text='Create Copy',
    value='copy',
    variable=radio_var,
    cursor="hand2")

# Width + Height
width_label = ttk.Label(master=frame1, text='W:')
height_label = ttk.Label(master=frame1, text='H:')
width_entry = ttk.Entry(master=frame1)
height_entry = ttk.Entry(master=frame1)

# Aspect ratio
ratio_var = tk.BooleanVar()
ratio_check = ttk.Checkbutton(
    master=frame1,
    text='Keep Aspect Ratio',
    onvalue=True,
    offvalue=False,
    variable=ratio_var,
    cursor="hand2")

# Expand/Collapse label
collapse_label = ttk.Label(frame2, text="+", cursor="hand2")

# Toggle the frames when the label is clicked
collapse_label.bind("<Button-1>", lambda event: toggle_frames())

# Image file viewer
file_view = ttk.Treeview(frame3, columns='Size')
file_view.heading('#0', text='Image')
file_view.column('#0', width=400)
file_view.heading('Size', text='Size')
file_view.column('Size', width=185)

# Scrollbar
file_view_scroll = ttk.Scrollbar(
    master=frame3,
    orient='vertical',
    command=file_view.yview)
file_view.configure(yscrollcommand=file_view_scroll.set)

# Image display
image_path = 'test.jpg'
image = Imager(image_path)
if frame4.winfo_reqheight() < image.height:
    image.resize_height(frame4.winfo_reqheight())
elif frame4.winfo_reqwidth() < image.width:
    image.resize_width(frame4.winfo_reqwidth())
photo = ImageTk.PhotoImage(image.img)
image.close()
image_label = ttk.Label(frame4, image=photo)

# Format selection
format_label = ttk.Label(frame5, text='Format:')
format_var = tk.StringVar()
format_var.set('JPG')
format_menu = ttk.Combobox(
    frame5,
    values=[item.upper()[1:] for item in IMAGE_EXTENSIONS],
    textvariable=format_var,
    state='readonly')

# Quality selection
quality_label = ttk.Label(frame5, text='Quality:')
quality_var = tk.IntVar()
quality_var.set(90)
quality_menu = ttk.Spinbox(
    frame5,
    from_=10,
    to=100,
    increment=10,
    textvariable=quality_var)

# Execute button
execute_button = ttk.Button(frame5, text='Execute', cursor="hand2")

test_frm = ttk.LabelFrame(frame1, text='New Dims', labelanchor='s')
test_frm.grid(row=1, column=0, columnspan=5)

"""     WIDGET STYLING      """

frame2.configure(style='Collapse.TFrame')
folder_button.configure(style='Small.TButton', width=2)
folder_entry.configure(font=entry_font, width=23)
width_entry.configure(font=entry_font, width=13)
height_entry.configure(font=entry_font, width=13)
collapse_label.configure(style='Collapse.TLabel')
format_menu.configure(width=5)
quality_menu.configure(width=5)

"""     WIDGET PLACEMENT    """

frm1_pady = (5, 5)            # Gap above and below widgets on Frame 1

# Row 1
folder_label.grid(
    row=0, column=0, sticky='ew', pady=frm1_pady, padx=(20, 10))
folder_entry.grid(
    row=0, column=1, sticky='ew', pady=frm1_pady, columnspan=3)
folder_button.grid(
    row=0, column=4, sticky='ew', pady=frm1_pady, padx=10)
overwrite_radio.grid(
    row=0, column=5, sticky='ew', pady=frm1_pady, padx=(20, 10))
copy_radio.grid(
    row=0, column=6, sticky='ew', pady=frm1_pady, padx=10)

# Row 2
width_label.grid(
    row=1, column=0, sticky='e', pady=frm1_pady, padx=10)
width_entry.grid(
    row=1, column=1, sticky='ew', pady=frm1_pady)
height_label.grid(
    row=1, column=2, sticky='e', pady=frm1_pady, padx=10)
height_entry.grid(
    row=1, column=3, sticky='ew', pady=frm1_pady)
ratio_check.grid(
    row=1, column=5, sticky='ew', pady=frm1_pady, padx=(20, 10), columnspan=2)

# Row 3
collapse_label.pack(pady=5)

# Row 4
file_view.grid(row=0, column=0, sticky='nsew', padx=0, pady=0)
file_view_scroll.grid(row=0, column=1, sticky='nse')

# Row 5
image_label.grid(row=0, column=0)

# Row 6
format_label.grid(
    row=0, column=0, sticky='ew', pady=0, padx=(15, 10))
format_menu.grid(
    row=0, column=1, sticky='ew', pady=0)
quality_label.grid(
    row=0, column=2, sticky='ew', pady=0, padx=(66, 10))
quality_menu.grid(
    row=0, column=3, sticky='ew', pady=0)
execute_button.grid(
    row=0, column=4, sticky='ew', pady=0, padx=(197, 0))

root.mainloop()
