import json

# liked_tracks_info.json 파일에서 데이터 읽기
with open("liked_tracks_info.json", "r", encoding="utf-8") as file:
    liked_tracks_data = json.load(file)

# recent_tracks_info.json 파일에서 데이터 읽기
with open("recent_tracks_info.json", "r", encoding="utf-8") as file:
    recent_tracks_data = json.load(file)

# liked_tracks_info.json와 recent_tracks_info.json을 비교하여 완벽하게 일치하는 항목 찾기
matched_tracks = [track for track in liked_tracks_data if track in recent_tracks_data]

# 완벽하게 일치하는 항목이 5개 이상인 경우 메시지 출력
if len(matched_tracks) >= 5:
    print("현재 이용자는 '좋아요를 표시한 곡' 플레이 리스트를 듣는 중입니다.")