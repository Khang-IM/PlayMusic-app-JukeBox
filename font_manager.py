import tkinter.font as tkfont


def configure():
    # Define the font family to be used (uncomment to switch between fonts)
    # family = "Segoe UI"  # Alternate font family option (commented out)
    family = "Helvetica"  # Selected font family

    # Configure the default font used by tkinter widgets
    default_font = tkfont.nametofont("TkDefaultFont")  # Get the default font configuration
    default_font.configure(size=12, family=family)  # Set size and family for the default font

    # Configure the font used by tkinter Text widgets
    text_font = tkfont.nametofont("TkTextFont")  # Get the text font configuration
    text_font.configure(size=12, family=family)  # Set size and family for the text font

    # Configure the font used by tkinter fixed-width widgets (e.g., Text with monospace)
    fixed_font = tkfont.nametofont("TkFixedFont")  # Get the fixed font configuration
    fixed_font.configure(size=12, family=family)  # Set size and family for the fixed font
