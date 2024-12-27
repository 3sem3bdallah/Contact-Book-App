"""Main application window"""
import tkinter as tk
from tkinter import messagebox
from ..models.contact_book import ContactBook
from .styles import COLORS, FONTS, PADDING
from .components.entry_frame import EntryFrame
from .components.button_bar import ButtonBar
from .components.contact_list import ContactList

class ContactBookApp:
    def __init__(self, root):
        self.contact_book = ContactBook()
        self.setup_window(root)
        self.create_widgets(root)
        
    def setup_window(self, root):
        root.title("Contact Book")
        root.geometry("800x600")
        root.configure(bg=COLORS['background'])
        
        # Header
        header = tk.Label(root, text="Contact Book Manager", 
                        font=FONTS['header'], bg=COLORS['primary'], fg='white')
        header.pack(fill='x', pady=(0, PADDING['large']))
        
    def create_widgets(self, root):
        # Main container
        container = tk.Frame(root, bg=COLORS['background'])
        container.pack(fill='both', expand=True, padx=PADDING['large'])
        
        # Left panel (Entry form and buttons)
        left_panel = tk.Frame(container, bg=COLORS['background'])
        left_panel.pack(side='left', fill='y', padx=(0, PADDING['large']))
        
        self.entry_frame = EntryFrame(left_panel)
        self.entry_frame.pack(fill='x')
        
        self.button_bar = ButtonBar(left_panel, {
            'add': self.add_contact,
            'update': self.update_contact,
            'delete': self.delete_contact,
            'search': self.search_contact,
            'sort': self.sort_contacts
        })
        self.button_bar.pack(fill='x', pady=PADDING['medium'])
        
        # Right panel (Contact list)
        self.contact_list = ContactList(container)
        self.contact_list.pack(side='left', fill='both', expand=True)
        
    def add_contact(self):
        values = self.entry_frame.get_values()
        if all(values.values()):
            self.contact_book.add_contact(values['name'], values['phone'], values['email'])
            messagebox.showinfo("Success", "Contact added successfully!")
            self.entry_frame.clear()
            self.refresh_contacts()
        else:
            messagebox.showerror("Error", "All fields are required!")
            
    def update_contact(self):
        values = self.entry_frame.get_values()
        if self.contact_book.update_contact(values['name'], values['phone'], values['email']):
            messagebox.showinfo("Success", "Contact updated successfully!")
            self.entry_frame.clear()
            self.refresh_contacts()
        else:
            messagebox.showerror("Error", "Contact not found!")
            
    def delete_contact(self):
        name = self.entry_frame.get_values()['name']
        if self.contact_book.delete_contact(name):
            messagebox.showinfo("Success", "Contact deleted successfully!")
            self.entry_frame.clear()
            self.refresh_contacts()
        else:
            messagebox.showerror("Error", "Contact not found!")
            
    def search_contact(self):
        keyword = self.entry_frame.get_values()['name']
        results = self.contact_book.search_contact(keyword)
        if results:
            self.contact_list.update_contacts(results)
        else:
            messagebox.showinfo("Info", "No matching contacts found.")
            
    def sort_contacts(self):
        self.contact_book.sort_contacts_by_name()
        self.refresh_contacts()
        messagebox.showinfo("Success", "Contacts sorted by name!")
        
    def refresh_contacts(self):
        contacts = self.contact_book.display_contacts()
        self.contact_list.update_contacts(contacts if contacts else [])