import json
import matplotlib.pyplot as plt
from collections import Counter

# liked_tracks_info.json 파일에서 장르 추출
with open("liked_tracks_info.json", "r", encoding="utf-8") as file:
    liked_tracks_data = json.load(file)

# 장르 추출 함수
def extract_genres(tracks_data):
    genres = [genre for track in tracks_data for genre in track["genres"]]
    return genres

#가장 많이 언급된 장르 5개씩 추출
liked_genres_counter = Counter(extract_genres(liked_tracks_data))
top_liked_genres = liked_genres_counter.most_common(5)

# 그래프 그리기
plt.figure(figsize=(10, 6))

# liked_tracks_info.json에서 가장 많이 언급된 장르 그래프
plt.bar([genre for genre, _ in top_liked_genres], [count for _, count in top_liked_genres], color='skyblue')
plt.title('Top 5 Genres in liked_tracks_info.json')
plt.xlabel('Genres')
plt.ylabel('Frequency')

# 그래프 출력
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()