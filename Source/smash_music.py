import os
import pydub
from utils import get_albums, get_songs, tape_music
import argparse


def main(artists, start_time, clip_length, random_start, seed):
    smashed_songs = f'./Smashed_Songs/'
    save_file = f'{artists}_{start_time}_{clip_length}_{str(random_start)}_{seed}.mp3'
    save_path = os.path.join(smashed_songs, save_file)
    print(f'Final song will be saved in: {save_file}')
    if not os.path.exists(smashed_songs):
        os.makedirs(smashed_songs)
    albums = get_albums(artists)
    songs = get_songs(albums)
    final_song = tape_music(songs,
                            start_time=start_time,
                            clip_length=clip_length,
                            random_start=random_start,
                            debug = True)
    final_song.export(save_path, format='mp3')
    print("FINISHED")
    
    return(None)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='smash_music.py',
                        description='Create a new song from many songs')
    parser.add_argument('--Artists', nargs='+',
                         help='List the artists you want with a space inbetween them')
    parser.add_argument('--Start_Time', type=int, default=0,
                        help='Time to start from in each song')
    parser.add_argument('--Clip_Length', type=int, default=5,
                        help='Length of a clip from a song')
    parser.add_argument('--Random_Start', type=bool, default=False,
                        help='If True, clips will be grabbed from random parts of songs')
    parser.add_argument('--Seed', type=int, default=42,
                        help='Seed for Random')

    args = parser.parse_args()
    # print(args)
    print(args.Artists)

    main(args.Artists, args.Start_Time, args.Clip_Length, args.Random_Start, args.Seed)
