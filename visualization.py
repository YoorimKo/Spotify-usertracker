import json
import matplotlib.pyplot as plt
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

# 각 파일에서 가장 많이 언급된 장르 5개씩 추출
liked_genres_counter = Counter(extract_genres(liked_tracks_data))
recent_genres_counter = Counter(extract_genres(recent_tracks_data))

top_liked_genres = liked_genres_counter.most_common(5)
top_recent_genres = recent_genres_counter.most_common(5)

# 그래프 그리기
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# liked_tracks_info.json에서 가장 많이 언급된 장르 그래프
axes[0].bar([genre for genre, _ in top_liked_genres], [count for _, count in top_liked_genres], color='skyblue')
axes[0].set_title('Top 5 Genres in liked_tracks_info.json')
axes[0].set_xlabel('Genres')
axes[0].set_ylabel('Frequency')

# recent_tracks_info.json에서 가장 많이 언급된 장르 그래프
axes[1].bar([genre for genre, _ in top_recent_genres], [count for _, count in top_recent_genres], color='salmon')
axes[1].set_title('Top 5 Genres in recent_tracks_info.json')
axes[1].set_xlabel('Genres')
axes[1].set_ylabel('Frequency')

# 그래프 출력
plt.tight_layout()
plt.show()