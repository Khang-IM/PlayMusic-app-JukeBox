import tkinter as tk  # Import the tkinter library for GUI creation

# Import custom modules for managing fonts and track-related operations
import font_manager as fonts  # Module for configuring fonts
from view_tracks import TrackViewer  # Module to view tracks
from create_tracks import CreateTrackApp  # Module to create tracks
from update_track import UpdateTrackWindow  # Module to update tracks

# Function to handle the "View Tracks" button click
def view_tracks_clicked():
    status_lbl.configure(text="View Tracks button was clicked!")  # Update the status label with a message
    TrackViewer(tk.Toplevel(window))  # Open a new TrackViewer window

# Function to handle the "Create Track List" button click
def view_create_track_clicked():
    status_lbl.configure(text="Create Tracks List button was clicked!")  # Update the status label with a message
    CreateTrackApp(tk.Toplevel(window))  # Open a new CreateTrackApp window

# Function to handle the "Update Tracks" button click
def view_update_track_clicked():
    status_lbl.configure(text="Update Tracks button was clicked!")  # Update the status label with a message
    UpdateTrackWindow(tk.Toplevel(window))  # Open a new UpdateTrackWindow

# Create the main application window
window = tk.Tk()
window.geometry("420x180")  # Set the window size
window.title("JukeBox")  # Set the window title
window.configure(bg="grey")  # Set the background color of the window

fonts.configure()  # Call the font configuration function from the font_manager module

# Create a header label with instructions for the user
header_lbl = tk.Label(window, text="Select an option by clicking one of the buttons below")
header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)  # Position the label in the grid layout

# Create the "View Tracks" button and assign the click handler
view_tracks_btn = tk.Button(window, text="View Tracks", command=view_tracks_clicked)
view_tracks_btn.grid(row=1, column=0, padx=10, pady=10)  # Position the button in the grid layout

# Create the "Create Track List" button and assign the click handler
create_track_list_btn = tk.Button(window, text="Create Track List", command=view_create_track_clicked)
create_track_list_btn.grid(row=1, column=1, padx=10, pady=10)  # Position the button in the grid layout

# Create the "Update Tracks" button and assign the click handler
update_tracks_btn = tk.Button(window, text="Update Tracks", command=view_update_track_clicked)
update_tracks_btn.grid(row=1, column=2, padx=10, pady=10)  # Position the button in the grid layout

# Create a status label to display messages to the user
status_lbl = tk.Label(window, bg='gray', text="", font=("Helvetica", 10))
status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)  # Position the label in the grid layout

# Start the main event loop to run the application
window.mainloop()