import os
from pytube import YouTube
import argparse

def main(path_to_file, artist, album):
    # Get current working directory
    wrking_dir = os.getcwd()
    # Check or create save directory
    save_dir = f'../../Artists/{artist}/{album}'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    print(f'Files will be saved at {save_dir}')

    # Read text file to get youtube links
    with open(path_to_file) as f:
        yt_songs = f.read().splitlines()
    
    # Loop over to download from links
    for yt_song in yt_songs:
        try:
            save_file_path = YouTube(yt_song).streams.get_audio_only().download(output_path = save_dir)
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
    parser = argparse.ArgumentParser(prog='youtube_video_grab.py',
                                    description='Create a new song from many songs')
    parser.add_argument('--File', type=str,
                        help='Text file containing youtube links')
    parser.add_argument('--Artist', type=str, default='NotLabeled',
                        help='Artist whos songs you are downloading (archiving purposes)')
    parser.add_argument('--Album', type=str, default='NotLabeled',
                        help='Album that you are downloading (archiving purposes)')
    args = parser.parse_args()
    main(args.File, args.Artist, args.Album)
