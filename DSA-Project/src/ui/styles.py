"""UI styling constants and configurations"""

COLORS = {
    'primary': '#2563eb',    # Blue
    'secondary': '#1e40af',  # Darker Blue
    'background': '#f8fafc', # Light Gray
    'surface': '#ffffff',    # White
    'text': '#1e293b',      # Dark Gray
    'error': '#ef4444',     # Red
    'success': '#22c55e'    # Green
}

FONTS = {
    'header': ('Helvetica', 24, 'bold'),
    'title': ('Helvetica', 18, 'bold'),
    'body': ('Helvetica', 12),
    'button': ('Helvetica', 11, 'bold')
}

PADDING = {
    'small': 5,
    'medium': 10,
    'large': 20
}

BUTTON_STYLE = {
    'bg': COLORS['primary'],
    'fg': 'white',
    'font': FONTS['button'],
    'relief': 'flat',
    'padx': 15,
    'pady': 8,
    'cursor': 'hand2'
}