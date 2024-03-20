import json
import matplotlib.pyplot as plt
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

# Extracting top 5 most mentioned genres from each file
liked_genres_counter = Counter(extract_genres(liked_tracks_data))
recent_genres_counter = Counter(extract_genres(recent_tracks_data))

top_liked_genres = liked_genres_counter.most_common(5)
top_recent_genres = recent_genres_counter.most_common(5)

# Plotting the graphs
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Graph for top mentioned genres in liked_tracks_info.json
axes[0].bar([genre for genre, _ in top_liked_genres], [count for _, count in top_liked_genres], color='skyblue')
axes[0].set_title('Top 5 Genres in liked tracks')
axes[0].set_xlabel('Genres')
axes[0].set_ylabel('Frequency')
axes[0].tick_params(axis='y', labelsize=10)  # Setting y-axis tick size
axes[0].get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))  # Formatting y-axis ticks as integers

# Graph for top mentioned genres in recent_tracks_info.json
axes[1].bar([genre for genre, _ in top_recent_genres], [count for _, count in top_recent_genres], color='salmon')
axes[1].set_title('Top 5 Genres in recent tracks')
axes[1].set_xlabel('Genres')
axes[1].set_ylabel('Frequency')
axes[1].tick_params(axis='y', labelsize=10)  # Setting y-axis tick size
axes[1].get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))  # Formatting y-axis ticks as integers

# Displaying the graphs
plt.tight_layout()
plt.show()
