from library_item import LibraryItem  # Importing the LibraryItem class from library_item module

# Initialize a dictionary to store library items
library = {}
# Adding predefined library items with unique keys
library["01"] = LibraryItem("Another Brick in the Wall", "Pink Floyd", 4)  # Pink Floyd's song with rating 4
library["02"] = LibraryItem("Stayin' Alive", "Bee Gees", 5)  # Bee Gees' song with rating 5
library["03"] = LibraryItem("Highway to Hell ", "AC/DC", 2)  # AC/DC's song with rating 2
library["04"] = LibraryItem("Shape of You", "Ed Sheeran", 1)  # Ed Sheeran's song with rating 1
library["05"] = LibraryItem("Someone Like You", "Adele", 3)  # Adele's song with rating 3

# Function to list all items in the library
def list_all():
    output = ""  # Initialize an empty string for the output
    for key in library:  # Iterate over all keys in the library dictionary
        item = library[key]  # Get the library item associated with the key
        output += f"{key} {item.info()}\n"  # Append the key and item info to the output
    return output  # Return the formatted list of items

# Function to get the name of a library item by its key
def get_name(key):
    try:
        item = library[key]  # Attempt to get the library item by key
        return item.name  # Return the name of the item
    except KeyError:  # Handle the case where the key does not exist
        return None  # Return None if the key is not found

# Function to get the artist of a library item by its key
def get_artist(key):
    try:
        item = library[key]  # Attempt to get the library item by key
        return item.artist  # Return the artist of the item
    except KeyError:  # Handle the case where the key does not exist
        return None  # Return None if the key is not found

# Function to get the rating of a library item by its key
def get_rating(key):
    try:
        item = library[key]  # Attempt to get the library item by key
        return item.rating  # Return the rating of the item
    except KeyError:  # Handle the case where the key does not exist
        return -1  # Return -1 if the key is not found

# Function to set a new rating for a library item by its key
def set_rating(key, rating):
    try:
        item = library[key]  # Attempt to get the library item by key
        item.rating = rating  # Update the rating of the item
    except KeyError:  # Handle the case where the key does not exist
        return  # Do nothing if the key is not found

# Function to get the play count of a library item by its key
def get_play_count(key):
    try:
        item = library[key]  # Attempt to get the library item by key
        return item.play_count  # Return the play count of the item
    except KeyError:  # Handle the case where the key does not exist
        return -1  # Return -1 if the key is not found

# Function to increment the play count of a library item by its key
def increment_play_count(key):
    try:
        item = library[key]  # Attempt to get the library item by key
        item.play_count += 1  # Increment the play count of the item
    except KeyError:  # Handle the case where the key does not exist
        return  # Do nothing if the key is not found

# Function to clear all items from the library
def clear_library():
    library.clear()  # Clear the library dictionary