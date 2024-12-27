"""Contact list display component"""
import tkinter as tk
from tkinter import ttk
from ..styles import COLORS, FONTS, PADDING

class ContactList(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=COLORS['surface'])
        
        # Title
        title = tk.Label(self, text="Contacts", font=FONTS['title'],
                        bg=COLORS['surface'], fg=COLORS['text'])
        title.pack(pady=PADDING['medium'])
        
        # Create Treeview
        self.tree = ttk.Treeview(self, columns=('Name', 'Phone', 'Email'), show='headings')
        
        # Configure columns
        self.tree.heading('Name', text='Name')
        self.tree.heading('Phone', text='Phone')
        self.tree.heading('Email', text='Email')
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Pack widgets
        self.tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
    def update_contacts(self, contacts):
        self.tree.delete(*self.tree.get_children())
        for contact in contacts:
            name, phone, email = contact.split(' | ')
            self.tree.insert('', 'end', values=(name, phone, email))