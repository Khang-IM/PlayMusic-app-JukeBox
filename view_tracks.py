import tkinter as tk
import tkinter.scrolledtext as tkst
import webbrowser
import track_library as lib
import font_manager as fonts


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class TrackViewer():
    def __init__(self, window):
        # Set up the main window geometry and title
        window.geometry("750x350")
        window.title("View Tracks")

        # Create a button to list all tracks, call the list_tracks_clicked method when clicked
        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        # Label prompting the user to enter a track number
        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        # Create an input field to enter a track number
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # Create a button to view a specific track based on the input
        check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked)
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)

        # Create a scrolled text area to list all tracks
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Create a text box to display details of the selected track
        self.track_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        # Create a button to listen to the track online (using Last.fm)
        self.btn_load_track = tk.Button(window, text="Listen Online", command=self.view_track_in_lastfm)
        self.btn_load_track.place(x=480, y=140, width=120, height=30)

        # Create a status label to display the current action
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        # Call list_tracks_clicked to populate the initial list of tracks
        self.list_tracks_clicked()

    def view_tracks_clicked(self):
        # Call list_all to ensure the library is up-to-date
        lib.list_all()

        # Get the track number from the input field
        key = self.input_txt.get()

        # Try to retrieve the track details using the track number
        name = lib.get_name(key)
        if name is not None:
            # If the track exists, fetch details like artist, rating, and play count
            artist = lib.get_artist(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)

            # Format the track details for display
            track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}"

            # Display the track details in the text box
            set_text(self.track_txt, track_details)

            # Enable the "Listen Online" button
            self.btn_load_track.config(state=tk.NORMAL)
        else:
            # If the track is not found, display an error message
            set_text(self.track_txt, f"Track {key} not found")

            # Disable the "Listen Online" button
            self.btn_load_track.config(state=tk.DISABLED)

        # Update the status label to indicate the action
        self.status_lbl.configure(text="View Track button was clicked!")

    def list_tracks_clicked(self):
        # Get the list of all tracks from the library
        track_list = lib.list_all()

        # Display the list of all tracks in the text area
        set_text(self.list_txt, track_list)

        # Update the status label to indicate the action
        self.status_lbl.configure(text="List Tracks button was clicked!")

    def view_track_in_lastfm(self):
        # Get the content of the track details text box
        content = self.track_txt.get("1.0", tk.END)

        # Split the content into lines
        lines = content.strip().split("\n")

        # Extract the track name (first line)
        track_name = lines[0] if len(lines) > 0 else None

        # If a track name is found, open the corresponding Last.fm page
        if track_name:
            print(track_name)  # Print the track name to the console (for debugging)
            url = f"https://www.last.fm/music/{track_name}"  # Construct the Last.fm URL
            webbrowser.open(url)  # Open the URL in the default web browser

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    TrackViewer(window)     # open the TrackViewer GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
