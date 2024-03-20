import json
from db_config import get_redis_connection

r = get_redis_connection()

# current_track_info
# JSON 파일 데이터 읽기
with open("current_track_info.json", "r", encoding="utf-8") as file:
    json_data = json.load(file)

# JSON 데이터를 문자열로 직렬화하여 Redis에 저장
r.set('current_track_info', json.dumps(json_data))

# Redis에서 데이터 가져오기
json_data_redis = r.get('current_track_info')
data = json.loads(json_data_redis)

# 필요한 정보 출력
print("Current Track:")
print("Track Name:", data['track_name'])
print("Artist Name:", data['artist_name'])
print("Album Name:", data['album_name'])
print("Genres:", data['genres'])
print()

# liked_tracks_info.json 파일 데이터 읽기 (UTF-8 인코딩으로)
with open("liked_tracks_info.json", "r", encoding="utf-8") as file:
    liked_tracks_info = json.load(file)

# 전체 데이터를 Redis에 문자열로 저장
r.set("liked_tracks_info", json.dumps(liked_tracks_info))

# 전체 데이터 출력
print("Liked Tracks Information:")
print(json.dumps(liked_tracks_info, indent=2))