import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Import the tcl file
root.tk.call('source', 'C:/Users/lutzr/OneDrive/Desktop/My-Projects/desktop_graph_vis/UI/tkinter_theme/forest-dark.tcl')

# Set the theme with the theme_use method
ttk.Style().theme_use('forest-dark')

# A themed (ttk) button
button = ttk.Button(root, text="I'm a themed button")
button.pack(pady=20)

root.mainloop()