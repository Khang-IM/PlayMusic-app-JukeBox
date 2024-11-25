import requests
import random

# API key for accessing the Last.fm API
api_key = "0422bbe02a46188162bc223eabc1ff10"


# Function to generate a random rating between 1 and 10
def generate_random_rating():
    return random.randint(1, 10)

# Function to fetch the top tracks of a given artist from the Last.fm API
def fetch_top_tracks(artist_name):
    # Construct the API URL with the artist name and API key
    url = f"http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={artist_name}&api_key={api_key}&format=json"
    response = requests.get(url)  # Send a GET request to the API
    top_tracks_data = response.json()  # Parse the API response as JSON

    track_list = []  # Initialize an empty list to store track details
    top_tracks = top_tracks_data['toptracks']['track'][:10]  # Get the top 10 tracks from the API response

    # Check if the response contains the 'toptracks' and 'track' keys
    if 'toptracks' in top_tracks_data and 'track' in top_tracks_data['toptracks']:
        # Generate a list of unique random IDs for the tracks
        unique_ids = random.sample(range(100, 1000), len(top_tracks_data['toptracks']['track']))

        # Iterate over the top tracks and build a dictionary for each track
        for index, track in enumerate(top_tracks):
            track_number = unique_ids[index]  # Assign a unique ID to the track
            track_name = track['name']  # Get the track name from the API response
            track_artist = artist_name  # Use the provided artist name
            rating = generate_random_rating()  # Generate a random rating for the track

            # Append the track details as a dictionary to the track list
            track_list.append({
                "track_number": track_number,  # Unique ID for the track
                "track_name": track_name,  # Name of the track
                "track_artist": track_artist,  # Artist name
                "rating": rating,  # Random rating between 1 and 10
            })
    return track_list  # Return the list of tracks with their details