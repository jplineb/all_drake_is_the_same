import pydub
import numpy as np
import os
import random

def get_albums(artists):
    all_albums = []
    for artist in artists:
        for album in os.listdir(f'./Artists/{artist}'):
            if album.startswith('.'):
                None
            else:
                all_albums.append(f'./Artists/{artist}/{album}')
    
    return(all_albums)

def get_songs(albums):
    all_songs = []
    for album in albums:
        for song in os.listdir(album):
            if song.endswith('.mp3'):
                all_songs.append(f'{album}/{song}')
    
    return(all_songs)

def tape_music(songs, start_time = 0, clip_length = 5, random_start = False, seed = 42, debug = False):
    random.seed(seed)
    clip_length_ms = clip_length*1000
    start_time_ms = start_time*1000
    for song in songs:
        loaded_song = pydub.AudioSegment.from_mp3(song)
        song_length = len(loaded_song)

        if start_time >= song_length:
            print(f'Error, start time is later than endinging for {song}')
        else:
            if random_start:
                start_time_random_ms = random.randint(0, (song_length-clip_length_ms))
                song_segm = loaded_song[start_time_random_ms:start_time_random_ms+clip_length_ms]
            else:
                song_segm = loaded_song[start_time_ms:start_time_ms+clip_length_ms]
        
        if song == songs[0]:
            final_mix = song_segm
        else:
            final_mix = final_mix + song_segm

        if debug:
            print('---------')
            print(f'Song {song} successfully loaded')
            print('---------')
    
    return(final_mix)

# Testing Area
# albums = get_albums(["Kanye"])
# print(albums)
# songs = get_songs(albums)
# print(songs)
# final_song = tape_music(songs,
#                          start_time = 0,
#                          clip_length = 5,
#                          random_start = True,
#                          debug = True)
# final_song.export('final_song.mp3', format='mp3')





