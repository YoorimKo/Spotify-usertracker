import json
from collections import Counter

# Extracting genres from liked_tracks_info.json file
with open("liked_tracks_info.json", "r", encoding="utf-8") as file:
    liked_tracks_data = json.load(file)

# Extracting genres from recent_tracks_info.json file
with open("recent_tracks_info.json", "r", encoding="utf-8") as file:
    recent_tracks_data = json.load(file)

# Extracting genres from the genres part of current_track_info.json file
with open("current_track_info.json", "r", encoding="utf-8") as file:
    current_track_data = json.load(file)

# Function to extract genres
def extract_genres(tracks_data):
    genres = [genre for track in tracks_data for genre in track["genres"]]
    return genres

# Extracting top 5 most mentioned genres from each file
liked_genres_counter = Counter(extract_genres(liked_tracks_data))
recent_genres_counter = Counter(extract_genres(recent_tracks_data))

top_liked_genres = liked_genres_counter.most_common(5)
top_recent_genres = recent_genres_counter.most_common(5)

print("Top 5 genres from liked tracks:")
for genre, count in top_liked_genres:
    print(f"{genre}: {count} times")

print("\nTop 5 genres from recent tracks:")
for genre, count in top_recent_genres:
    print(f"{genre}: {count} times")

# Getting the genre of the currently playing track
current_playing_genre = current_track_data["genres"]

if current_playing_genre in [genre for genre, _ in top_liked_genres]:
    print("\nThe genre of the currently playing track is one of the most mentioned genres in the 'liked tracks list'.")
elif current_playing_genre in [genre for genre, _ in top_recent_genres]:
    print("\nThe genre of the currently playing track is one of the most listened genres among the 'recent tracks'.")
else:
    print("\nThe genre of the currently playing track does not belong to the top mentioned genres in both 'liked tracks list' and 'recent tracks'.")
