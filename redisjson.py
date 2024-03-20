import json
from db_config import get_redis_connection

r = get_redis_connection()

# current_track_info
# Read JSON file data
with open("current_track_info.json", "r", encoding="utf-8") as file:
    json_data = json.load(file)

# Serialize JSON data to a string and store it in Redis
r.set('current_track_info', json.dumps(json_data))

# Retrieve data from Redis
json_data_redis = r.get('current_track_info')
data = json.loads(json_data_redis)

# Print necessary information
print("Current Track:")
print("Track Name:", data['track_name'])
print("Artist Name:", data['artist_name'])
print("Album Name:", data['album_name'])
print("Genres:", data['genres'])
print()

# liked_tracks_info.json
# Read JSON file data (UTF-8 encoding)
with open("liked_tracks_info.json", "r", encoding="utf-8") as file:
    liked_tracks_info = json.load(file)

# Serialize JSON data to a string and store it in Redis
r.set("liked_tracks_info", json.dumps(liked_tracks_info))

# recent_tracks_info.json
# Read JSON file data (UTF-8 encoding)
with open("recent_tracks_info.json", "r", encoding="utf-8") as file:
    recent_tracks_info = json.load(file)

# Serialize JSON data to a string and store it in Redis
r.set("recent_tracks_info", json.dumps(recent_tracks_info))
