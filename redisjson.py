import json
from db_config import get_redis_connection

r = get_redis_connection()

# current_track_info
# JSON 파일 데이터 읽기
with open("current_track_info.json", "r") as file:
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
    liked_tracks_data = json.load(file)

print("Liked tracks list:")

# 각 항목을 Redis에 문자열로 저장
for index, track_data in enumerate(liked_tracks_data, start=1):
    key = f"Liked track:{index}"
    value = json.dumps(track_data)
    r.set(key, value)

    # 출력
    print(f"{index}.")
    print("Track Name:", track_data["track_name"])
    print("Artist Name:", track_data["artist_name"])
    print("Album Name:", track_data["album_name"])
    print("Genres:", track_data["genres"])
    print()

