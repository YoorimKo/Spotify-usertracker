from app import *
from config import *
# example
if __name__ == "__main__":
    client_id = SPOTIPY_CLIENT_ID
    client_secret = SPOTIPY_CLIENT_SECRET
    redirect_uri = SPOTIPY_REDIRECT_URI
    scope = SPOTIPY_SCOPE

    current_track_info_obj = CurrentTrackInfo(client_id, client_secret, redirect_uri, scope)
    current_track_info_obj.get_current_track_info()

    liked_tracks_info_obj = LikedTracksInfo(client_id, client_secret, redirect_uri, scope)
    liked_tracks_info_obj.get_liked_tracks_info()
