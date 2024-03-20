import json
from collections import Counter

# liked_tracks_info.json 파일에서 장르 추출
with open("liked_tracks_info.json", "r", encoding="utf-8") as file:
    liked_tracks_data = json.load(file)

# recent_tracks_info.json 파일에서 장르 추출
with open("recent_tracks_info.json", "r", encoding="utf-8") as file:
    recent_tracks_data = json.load(file)

# 장르 추출 함수
def extract_genres(tracks_data):
    genres = [genre for track in tracks_data for genre in track["genres"]]
    return genres

# 각 파일에서 가장 많이 언급된 장르 3가지씩 추출
liked_genres_counter = Counter(extract_genres(liked_tracks_data))

top_liked_genres = liked_genres_counter.most_common(3)

print("liked_tracks_info.json에서 가장 많이 언급된 장르:")
for genre, count in top_liked_genres:
    print(f"{genre}: {count}회")

# 현재 재생 중인 노래의 장르 (임의로 지정)
current_playing_genre = "k-pop"

# 현재 재생 중인 노래의 장르가 가장 많이 언급된 장르인지 확인
if current_playing_genre in [genre for genre, _ in top_liked_genres]:
    print("\n현재 재생 중인 노래의 장르는 liked_tracks_info.json에서 가장 많이 언급된 장르 중 하나입니다.")
else:
    print("\n현재 재생 중인 노래의 장르는 liked_tracks_info.json에 속하지 않습니다.")


