class LibraryItem:
    # Constructor to initialize a library item with name, artist, rating, and play count
    def __init__(self, name, artist, rating=0):
        self.name = name  # The name of the item
        self.artist = artist  # The artist associated with the item
        self.rating = rating  # The rating of the item (default is 0)
        self.play_count = 0  # Initializing play count to 0

    # Method to return information about the item
    def info(self):
        return f"{self.name} - {self.artist} {self.stars()}"  # Returns name, artist, and star rating as a string

    # Method to return a string of stars based on the rating
    def stars(self):
        stars = ""  # Initialize an empty string for stars
        for i in range(self.rating):  # Loop through the number of stars based on the rating
            stars += "*"  # Add a star to the string for each rating point
        return stars  # Return the constructed star string
