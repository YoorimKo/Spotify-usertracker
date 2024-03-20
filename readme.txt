Assignment3

Create a Python Application, that

    Reads JSON from API
    Inserts into RedisJSON
    Does some processing (3 outputs) such as (matplotlib charts, aggregation,search,..)
    

The Python Application should be

- Using Python Classes (not plain scripting as shown in lecture notes)
- Should contain necessary DocString
- Should be aligned properly

#app idea
Utilize Spotify API.
Output the current track title - artist(album name) /store in json format
Based on the currently playing track information, store information about the last 20 tracks listened to (title, artist, album, genre) /store in json format
Information about the top 50 liked tracks (title, artist, album, genre) /store in json format


#Description
- tracklistupdate.py: Executable file that saves updated information to json
- redisjson.py : Executable file that uploads json files to redis
- visualization.py : File that analyzes liked_tracks_info and recent_tracks_info to display a bar graph of preferred genres
- userprefer.py: File that outputs information about the user's preferred genres

