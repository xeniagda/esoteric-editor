import tkinter as tk
import os
import tkinter.ttk as ttk

if __name__ == '__main__':
    root = tk.Tk()
    root.minsize(600,600)
    # editor = tk.Text(root)

    menu = tk.Menu(root)
    m_file = tk.Menu(menu,tearoff=0)
    menu.add_cascade(label="File", menu= m_file)
    m_file.add_command(label="Open File")
    m_file.add_command(label="Open Folder")
    m_file.add_command(label="Save")
    m_file.add_command(label="Save As")
    m_file.add_command(label="Open")
    m_file.add_separator()

    # config to render the menu bar
    root.config(menu=menu)
    root.mainloop()
