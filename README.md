# All Drake sounds the same

## About
This github was a project to originaly  create tools that would randomly sample drake songs and combine them together into a new one. Then end product is to see if the new song has continuity.

I ended up developing tools to mash together music into one big song. My experiments are in the form of ipython notebooks.

## Requirements
- pyaudio
- pyTube
- Numpy

## Usage
To create a song mash up pass the following arugments
- Artists : List of Artists wanted (Required)
- Albums: Albums from artists wanted (Default: All)
- Start_Time: Time to start the grab inside of songs (Default: 0)
- Clip_Length: Length of a song slice (Default: 5)
- Random_Start: If True, song slice will be grabbed from random points in the song (Default: False)

```
$ python3 Source/smash_music.py --Artists Drake --Albums CLB --Start_Time 0 --Clip_Length 5 --Random_Start False
```
