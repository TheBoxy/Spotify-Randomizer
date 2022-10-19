import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import secrets

os.environ['SPOTIPY_CLIENT_ID'] = '' # MAKE SURE TO ADD CLIENT ID HERE
os.environ['SPOTIPY_CLIENT_SECRET'] = '' # ADD CLIENT SECRET HERE
os.environ['SPOTIPY_REDIRECT_URI'] = '' # ADD REDIRECT URI HERE

spotifyBot = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="user-modify-playback-state"))

playlistInfo = spotifyBot.current_user_playlists()
playlistUriList = []

print("===========PlayLists===========")
while playlistInfo:
    for i, playlist in enumerate(playlistInfo['items']):
        playlistUriList.append(playlist['uri'])
        print("%4d %s" % (i + 1 + playlistInfo['offset'], playlist['name']))
    if playlistInfo['next']:
        playlistInfo = spotifyBot.next(playlistInfo)
    else:
        playlistInfo = None

playlistNumber = input("Enter the number that corresponds to the playist that you want to randomize: ")
selectedUri = playlistUriList[int(playlistNumber) - 1]

songUriList = []

selectedPlaylist = spotifyBot.playlist_items(selectedUri)
songs = selectedPlaylist['items']

while selectedPlaylist['next']:
    selectedPlaylist = spotifyBot.next(selectedPlaylist)
    songs.extend(selectedPlaylist['items'])

print("\tThere are ", len(songs), " songs.\n")

numSongs = input("Now enter number of songs you want to play: ")

for i in range(int(numSongs)):
    spotifyBot.add_to_queue(secrets.choice(songs)['track']['uri'])
print("=============FINISHED=============")
