"""Contact entry form component"""
import tkinter as tk
from ..styles import COLORS, FONTS, PADDING

class EntryFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=COLORS['surface'], padx=PADDING['large'], pady=PADDING['medium'])
        
        # Title
        title = tk.Label(self, text="Contact Information", font=FONTS['title'], 
                        bg=COLORS['surface'], fg=COLORS['text'])
        title.pack(pady=(0, PADDING['medium']))
        
        # Create entries
        self.entries = {}
        fields = [('name', 'Full Name'), ('phone', 'Phone Number'), ('email', 'Email Address')]
        
        for field_id, label in fields:
            frame = tk.Frame(self, bg=COLORS['surface'])
            frame.pack(fill='x', pady=PADDING['small'])
            
            tk.Label(frame, text=label, font=FONTS['body'], 
                    bg=COLORS['surface'], fg=COLORS['text']).pack(anchor='w')
            
            entry = tk.Entry(frame, font=FONTS['body'], width=30)
            entry.pack(fill='x', pady=(2, 0))
            self.entries[field_id] = entry
            
    def get_values(self):
        return {
            'name': self.entries['name'].get(),
            'phone': self.entries['phone'].get(),
            'email': self.entries['email'].get()
        }
        
    def clear(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)