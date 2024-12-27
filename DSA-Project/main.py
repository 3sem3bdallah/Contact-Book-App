import tkinter as tk
from src.ui.contact_book_app import ContactBookApp

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()