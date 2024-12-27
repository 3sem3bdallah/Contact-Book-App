"""Button bar component with action buttons"""
import tkinter as tk
from ..styles import COLORS, PADDING, BUTTON_STYLE

class ButtonBar(tk.Frame):
    def __init__(self, parent, commands):
        super().__init__(parent, bg=COLORS['surface'])
        
        buttons = [
            ('Add Contact', commands['add']),
            ('Update', commands['update']),
            ('Delete', commands['delete']),
            ('Search', commands['search']),
            ('Sort', commands['sort'])
        ]
        
        for text, command in buttons:
            btn = tk.Button(self, text=text, command=command, **BUTTON_STYLE)
            btn.pack(side='left', padx=PADDING['small'])