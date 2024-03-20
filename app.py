import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
from config import *
import matplotlib.pyplot as plt

class SpotifyInfoRetriever:
    """
    A class for retrieving information from Spotify API.
    """
    def __init__(self, client_id, client_secret, redirect_uri, scope):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                                            client_secret=SPOTIPY_CLIENT_SECRET,
                                                            redirect_uri=SPOTIPY_REDIRECT_URI,
                                                            scope=SPOTIPY_SCOPE))
        """
        Initializes the SpotifyInfoRetriever.

        Parameters:
        - client_id (str): Spotify API client ID.
        - client_secret (str): Spotify API client secret.
        - redirect_uri (str): Spotify API redirect URI.
        - scope (list): List of Spotify API scopes.
        """

    def save_to_json(self, data, filename):
        """
        Saves data to a JSON file.

        Parameters:
        - data (dict or list): Data to be saved.
        - filename (str): Name of the JSON file.
        """
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=2)

class CurrentTrackInfo(SpotifyInfoRetriever):
    """
    A class for retrieving information about the current playing track.
    """
    def get_current_track_info(self):
        """
        Retrieves information about the current playing track and saves it to a JSON file.
        """
        current_track_response = self.sp.current_playback()
        if current_track_response is not None and 'item' in current_track_response:
            current_track_info = current_track_response['item']
            track_name = current_track_info['name']
            artist_name = current_track_info['artists'][0]['name']
            album_name = current_track_info['album']['name']

            artist_id = current_track_info['artists'][0]['id']
            artist_info = self.sp.artist(artist_id)
            genres = artist_info['genres']

            output_data = {
                'track_name': track_name,
                'artist_name': artist_name,
                'album_name': album_name,
                'genres': genres
            }

            self.save_to_json(output_data, 'current_track_info.json')

            print(f"Now playing: {track_name} - {artist_name} ({album_name})")
            print(f"current_track_info saved completed.")
        else:
            print("Spotify에 연결되어 있지 않거나 현재 재생 중인 노래가 없습니다.")

class LikedTracksInfo(SpotifyInfoRetriever):
    """
    A class for retrieving information about Liked Tracks.
    """
    def get_liked_tracks_info(self, limit=50):
        """
        Retrieves information about liked tracks and saves it to a JSON file.

        Parameters:
        - limit (int): Number of liked tracks to retrieve.
        """
        liked_tracks_response = self.sp.current_user_saved_tracks(limit=limit)
        if 'items' in liked_tracks_response:
            liked_tracks_info = []

            for item in liked_tracks_response['items']:
                track_name = item['track']['name']
                artist_name = item['track']['artists'][0]['name']
                album_name = item['track']['album']['name']

                artist_id = item['track']['artists'][0]['id']
                artist_info = self.sp.artist(artist_id)
                genres = artist_info['genres']

                liked_tracks_info.append({
                    'track_name': track_name,
                    'artist_name': artist_name,
                    'album_name': album_name,
                    'genres': genres
                })

            self.save_to_json(liked_tracks_info, 'liked_tracks_info.json')

            print("liked_tracks_info saved completed.")

        else:
            print("좋아요한 노래가 없습니다.")

class RecentTracksInfo(SpotifyInfoRetriever):
    """
    A class for retrieving information about recently played tracks.
    """
    def get_recent_tracks_info(self, limit=20):
        """
        Retrieves information about recently played tracks and saves it to a JSON file.

        Parameters:
        - limit (int): Number of recently played tracks to retrieve.
        """
        recent_tracks_response = self.sp.current_user_recently_played(limit=limit)
        if 'items' in recent_tracks_response:
            recent_tracks_info = []

            for item in recent_tracks_response['items']:
                track_name = item['track']['name']
                artist_name = item['track']['artists'][0]['name']
                album_name = item['track']['album']['name']

                artist_id = item['track']['artists'][0]['id']
                artist_info = self.sp.artist(artist_id)
                genres = artist_info['genres']

                recent_tracks_info.append({
                    'track_name': track_name,
                    'artist_name': artist_name,
                    'album_name': album_name,
                    'genres': genres
                })

            self.save_to_json(recent_tracks_info, 'recent_tracks_info.json')
            
            print("recent_tracks_info saved completed.")
        else: 
            print("최근에 재생한 노래가 없습니다.")