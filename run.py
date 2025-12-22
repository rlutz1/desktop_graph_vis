from PyQt5.QtWidgets import QApplication, QWidget

# Only needed for access to command line arguments
import sys

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = QWidget()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event
# loop has stopped.

# ======================================================
# tkinter window below
# ======================================================

# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()

# # Import the tcl file
# root.tk.call('source', 'UI/tkinter_theme/forest-dark.tcl')

# # Set the theme with the theme_use method
# ttk.Style().theme_use('forest-dark')

# # set some meta about the application
# # https://tkdocs.com/pyref/tk.html
# root.title("Graph Algorithm Visualizer")
# # root.resizable(width=False, height=False)
# root.minsize(width=1000, height=500)
# mainframe = ttk.Frame(root, padding=(3, 3, 12, 12), width=500, height=500)
# # mainframe.grid(column=0, row=0)

# # A themed (ttk) button
# button = ttk.Button(root, text="I'm a themed button")
# button.pack(pady=20)

# root.mainloop()