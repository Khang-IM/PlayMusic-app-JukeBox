import tkinter as tk
from tkinter import messagebox
import track_library as lib
import tkinter.scrolledtext as tkst
import track_library as lib

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class UpdateTrackWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Update Track")
        self.root.geometry("460x260")

        # Track Number Label and Entry
        self.label_track_number = tk.Label(root, text="Track Number")
        self.label_track_number.place(x=20, y=20)
        self.txt_track_number = tk.Entry(root, width=8)
        self.txt_track_number.place(x=130, y=20)

        # New Rating Label and Entry
        self.label_new_rating = tk.Label(root, text="New Rating")
        self.label_new_rating.place(x=200, y=20)
        self.txt_new_rating = tk.Entry(root, width=5)
        self.txt_new_rating.place(x=290, y=20)

        # Add a button to submit the update (optional)
        self.update_button = tk.Button(root, text="Update", command=self.update_rating)
        self.update_button.place(x=340, y=15)

        self.list_txt = tkst.ScrolledText(root, width=40, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=5, sticky="W", padx=50, pady=50)

        self.list_tracks_clicked()

    def update_rating(self):
        track_number = self.txt_track_number.get().strip()  # Get the track number input and remove leading/trailing spaces
        new_rating = self.txt_new_rating.get().strip()  # Get the new rating input and remove leading/trailing spaces

        # Check if both fields are filled
        if not track_number or not new_rating:
            messagebox.showerror("Error", "Please fill in both fields.")  # Show error if any field is empty
            return

        try:
            new_rating = int(new_rating)  # Attempt to convert the new rating to an integer
            if new_rating < 1 or new_rating > 10:  # Check if the rating is within the valid range (1-10)
                messagebox.showerror("Error",
                                     "Rating should be between 1 and 10.")  # Show error if rating is out of range
                return
        except ValueError:
            messagebox.showerror("Error", "Rating should be an integer.")  # Show error if conversion to integer fails
            return

        # Check if the track number exists in the library
        if track_number not in lib.library:
            messagebox.showerror("Error", f"Track {track_number} not found.")  # Show error if track is not found
            return

        play_count = lib.get_play_count(track_number)  # Get the current play count of the track

        lib.set_rating(track_number, new_rating)  # Update the rating of the track in the library

        track_name = lib.get_name(track_number)  # Get the track name from the library
        artist = lib.get_artist(track_number)  # Get the artist of the track from the library

        # Prepare the track details for displaying
        track_details = f"Track Name: {track_name}\nArtist: {artist}\nNew Rating: {new_rating}\nPlay Count: {play_count}"

        self.list_tracks_clicked()  # Refresh the track list after the update
        messagebox.showinfo("Track Updated", track_details)  # Show a message with the updated track details

    def list_tracks_clicked(self):
        track_list = lib.list_all()  # Get all tracks from the library
        set_text(self.list_txt, track_list)  # Display the track list in the text field (list_txt)

if __name__ == "__main__":
    root = tk.Tk()
    app = UpdateTrackWindow(root)
    root.mainloop()