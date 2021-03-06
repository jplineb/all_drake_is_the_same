import os
from pytube import YouTube, Playlist
import argparse
import time

def main(playlist, artist, album):
    # Get current working directory
    wrking_dir = os.getcwd()

    # Check or create save directory
    save_dir = f'../../Artists/{artist}/{album}'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    print(f'Files will be saved at {save_dir}')

    # Initialize the playlist object
    yt_playlist = Playlist(playlist)

    # State the playlist name and description to user
    print(f'Title of Playlist: {yt_playlist.title}')
    print(f'Description of playlist: {yt_playlist.description}')

    # Loop over to download from links
    for yt_song, yt_url in zip(yt_playlist.videos, yt_playlist.video_urls):
        # Put process to sleep so youtube doesn't ip ban you
        time.sleep(5)
        try:
            save_file_path = yt_song.streams.get_audio_only().download(output_path = save_dir)
            print('--------')
            print(f'Successfully Downloaded {save_file_path}')
        except:
            print(f'Failure to download {yt_song}')
    
    # Convert mp4 files to mp3
    mp4_files = os.listdir(save_dir)
    for file in mp4_files:
        if file.endswith('.mp4'):
            # Create a save path based on the original name
            mp3_save_path = file.split('.mp4')[0]
            mp3_save_path = mp3_save_path + '.mp3'
            # Join the paths for command line
            file = os.path.join(save_dir, file)
            mp3_save_path = os.path.join(save_dir, mp3_save_path)
            try:
                cmd = "ffmpeg -i {} -vn {}".format(repr(file),
                                                    repr(mp3_save_path))
                os.system(cmd)
                print('--------')
                print(f'File successfully converted: {mp3_save_path}')
            except:
                print('--------')
                print(f'Warning: {file} not converted')
    
    print("FINISHED")

    return(None)



if __name__ == '__main__':
    '''
    This function will greatly differ from the original youtube_video_grab.py
    Since youtube links are often non-unix terminal friendly, we will as the user to
    input information into the terminal
    '''
    parser = argparse.ArgumentParser(prog='youtube_video_grab.py',
                                    description='Grab audio of youtube videos in a playlist')
    # parser.add_argument('--Playlist', type=str,
    #                     help='Playlist containing youtube links', required=True)
    # parser.add_argument('--Artist', type=str, default='NotLabeled',
    #                     help='Artist whos songs you are downloading (archiving purposes)')
    # parser.add_argument('--Album', type=str, default='NotLabeled',
    #                     help='Album that you are downloading (archiving purposes)')
    # args = parser.parse_args()
    # main(args.File, args.Artist, args.Album)

    # Ask the user for the youtube url
    playlist = input('Enter the Youtube URL for your playlist: ')
    if playlist is None:
        print('No playlist url given. Please restart the script')

    # Ask the user for the name of the artist
    artist = input('Enter the name of the artist for archiving: ')
    if artist is None:
        artist = 'NotLabeled'
    
    # Ask the user for the name of the album
    album = input('Enter the name of the album for archiving: ')
    if album is None:
        album = 'Not labeled'
    
    main(playlist, artist, album)

    
    