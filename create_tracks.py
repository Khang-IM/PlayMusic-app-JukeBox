import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import messagebox
import font_manager as fonts
from tkinter import ttk
from get_tracks import fetch_top_tracks
import track_library as lib
from library_item import LibraryItem

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class CreateTrackApp:
    def __init__(self, root):
        root.title("Create Track")
        root.geometry("486x463")

        # Track Number
        self.label_track_number = tk.Label(root, text="Track number")
        self.label_track_number.place(x=10, y=40)
        self.txt_track_number = tk.Text(root, height=1, width=8)
        self.txt_track_number.place(x=120, y=40)

        # Name
        self.label_name = tk.Label(root, text="Name")
        self.label_name.place(x=260, y=40)
        self.txt_name = tk.Text(root, height=1, width=14)
        self.txt_name.place(x=310, y=40)

        # Rating
        self.label_rating = tk.Label(root, text="Rating")
        self.label_rating.place(x=50, y=80)
        self.txt_rating = tk.Text(root, height=1, width=8)
        self.txt_rating.place(x=120, y=80)

        # Artist
        self.label_artist = tk.Label(root, text="Artist")
        self.label_artist.place(x=260, y=80)
        self.txt_artist = tk.Text(root, height=1, width=14)
        self.txt_artist.place(x=310, y=80)

        self.list_txt = tkst.ScrolledText(root, width=40, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=100, pady=200)

        # Buttons
        self.btn_add_track = tk.Button(root, text="Add Track", command=self.add_track)
        self.btn_add_track.place(x=100, y=170)

        ##Buton play list
        self.btn_play_list  = tk.Button(root, text="Play List", command=self.play_list)
        self.btn_play_list.place(x=200, y=170)

        #Buton clear input
        self.btn_clear_input = tk.Button(root, text="Clear Input", command=self.clear_input)
        self.btn_clear_input.place(x=280, y=170)

        #Button reset
        self.btn_reset = tk.Button(root, text= "Reset", command=self.reset)
        self.btn_reset.place(x=380, y = 170)

        self.list_tracks_clicked()

        ##Combobox
        self.label = tk.Label(root, text="Select artist")
        self.label.place(x=10, y=130, width=91, height=16)

        self.comboBox = ttk.Combobox(root, state="readonly")
        self.comboBox.place(x=120, y=130, width=131, height=25)
        self.comboBox['values'] = [
            "Steve Dobrogosz",
            "George Michael & Aretha Franklin",
            "Beppe Wolgers",
            "Vanessa Williams & Bobby Caldwell",
            "Bruno Mars",
            "Adele"
        ]

        ##Button get top tracks
        self.btn_get_top_track = tk.Button(root, text = "Get Top Tracks", command=self.get_top_tracks)
        self.btn_get_top_track.place(x=260, y = 130, width = 125, height = 20 )

        ##Button reload
        self.btn_reload = tk.Button(root, text="Reload", command= self.reload)
        self.btn_reload.place(x=230, y= 420, width = 80, height = 20)

    def add_track(self):
        track_number = self.txt_track_number.get("1.0", "end-1c").strip()
        track_name = self.txt_name.get("1.0", "end-1c").strip()
        artist = self.txt_artist.get("1.0", "end-1c").strip()
        rating = self.txt_rating.get("1.0", "end-1c").strip()

        if not track_number or not track_name or not artist or not rating:
            messagebox.showwarning("Input Error", "Please fill in all fields!")
            return
        try:
            rating = int(rating)
        except ValueError:
            messagebox.showwarning("Input Error", "Rating must be a number!")
            return
        if track_number not in lib.library:
            new_track = LibraryItem(track_name, artist, rating)
            lib.library[track_number] = new_track
            self.list_tracks_clicked()
        else:
            messagebox.showerror("Error", f"Track number '{track_number}' already exists!")

    def clear_input(self):
        self.txt_track_number.delete("1.0", "end")
        self.txt_name.delete("1.0", "end")
        self.txt_rating.delete("1.0", "end")
        self.txt_artist.delete("1.0", "end")

    def list_tracks_clicked(self):
        track_list = lib.list_all()
        set_text(self.list_txt, track_list)

    def play_list(self):
        message = ""
        for key in lib.library:
            play_count = lib.get_play_count(key)
            message += f"Track {key}: Play count = {play_count}\n"

            lib.increment_play_count(key)
            updated_play_count = lib.get_play_count(key)
            message += f"Track {key}: Play count updated to = {updated_play_count}\n\n"
        messagebox.showinfo("Track Play Count", message)

    def reset(self):
        lib.clear_library()
        set_text(self.list_txt, "")
        messagebox.showinfo("Notification","Reset sucessfully !!")

    def reload(self):
        track_list = lib.list_all()
        set_text(self.list_txt, track_list)

    def get_top_tracks(self):
        selected_artist = self.comboBox.get()
        if selected_artist:
            top_track = fetch_top_tracks(self.comboBox.get())
            for track in top_track:
                track_number = str(track['track_number'])
                lib.library[track_number] = LibraryItem(track['track_name'], track['track_artist'],
                                                                 track['rating'])

            track_lists = lib.list_all()
            set_text(self.list_txt, track_lists)
        else:
            messagebox.showerror("Warning","Please select artis first !")

    def clear_tracks(self):
        lib.clear_library()
        set_text(self.list_txt, "")

if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    CreateTrackApp(window)
    window.mainloop()