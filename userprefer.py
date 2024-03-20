import json
from collections import Counter

# Extracting genres from liked_tracks_info.json file
with open("liked_tracks_info.json", "r", encoding="utf-8") as file:
    liked_tracks_data = json.load(file)

# Extracting genres from recent_tracks_info.json file
with open("recent_tracks_info.json", "r", encoding="utf-8") as file:
    recent_tracks_data = json.load(file)

# Function to extract genres
def extract_genres(tracks_data):
    genres = [genre for track in tracks_data for genre in track["genres"]]
    return genres

# Extracting top 3 most mentioned genres from each file
liked_genres_counter = Counter(extract_genres(liked_tracks_data))
recent_genres_counter = Counter(extract_genres(recent_tracks_data))

top_liked_genres = liked_genres_counter.most_common(3)
top_recent_genres = recent_genres_counter.most_common(3)

print("Top genres from liked tracks:")
for genre, count in top_liked_genres:
    print(f"{genre}: {count} times")

print("\nTop genres from recent tracks:")
for genre, count in top_recent_genres:
    print(f"{genre}: {count} times")

# Checking if the genre of the currently playing track is among the top mentioned genres
current_playing_genre = "k-pop"

if current_playing_genre in [genre for genre, _ in top_liked_genres]:
    print("\nThe genre of the currently playing track is one of the most mentioned genres in the liked tracks list.")
elif current_playing_genre in [genre for genre, _ in top_recent_genres]:
    print("\nThe genre of the currently playing track is one of the most listened genres among the recent tracks.")
else:
    print("\nThe genre of the currently playing track does not belong to the top mentioned genres in both liked tracks list and recent tracks.")
