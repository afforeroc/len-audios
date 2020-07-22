# Total lenght of all mp3 audios in minutes
Python script to calculate total length of all mp3 audios in minutes.

## System requeriments
* Ubuntu 20.04 LTS

## 1. Install Python3
Install the latest version of `Python3` and verify their version.
```
$ sudo apt install python3
```
```
$ python3 --version
```

## 2. Install neccessary software
Install `ffmpeg`, `sox`, and `libsox-fmt-mp3` packages:
```
$ sudo apt-get install ffmpeg sox libsox-fmt-mp3
```

## 3. Run the script
Delete the `deleteme` file. Put the script outside the folder that contains audio files. Run the script adding as argument the mentioned folder.
```
$ python3 len_audios.sh audios/
```

### 4. Output
e.g.
```
Reading all audio files from audios/ folder ...
audios/06 How Intensitive.mp3
audios/12 I Can't Believe You're In Love With Me.mp3
audios/11 Hallelujah.mp3
audios/05 My Baby Just Cares For Me.mp3
audios/08 Body & Soul.mp3
audios/07 Dizzy Atmosphere.mp3
audios/01 Our Love Is Here To Stay.mp3
audios/04 Twenty Four Hours A Day.mp3
audios/02 Desafinado.mp3
audios/10 Lullaby Of Birdland.mp3
audios/09 Crazy He Calls Me.mp3
audios/03 Someday My Prince Will Come.mp3
Using ffprobe: 47.43 minutes
Using sox: 47.44 minutes
```

## References links
* [Stack Overflow - Calculate length of all mp3 files in one folder](https://stackoverflow.com/questions/45535938/bash-calculate-length-of-all-mp3-files-in-one-folder)
* [Stack Overflow - How to get the real, actual duration of an MP3 file (VBR or CBR) server-side](https://stackoverflow.com/questions/10437750/how-to-get-the-real-actual-duration-of-an-mp3-file-vbr-or-cbr-server-side/10571671)
* [Stack Overflow - Getting FFProbe Information With Python](https://stackoverflow.com/questions/9896644/getting-ffprobe-information-with-python)
* [Super User - How to add a mp3 handler to sox?](https://superuser.com/questions/421153/how-to-add-a-mp3-handler-to-sox)


## Documentation links
* [FFmpeg](https://ffmpeg.org/)
* [SoX - Sound eXchange | HomePage](http://sox.sourceforge.net/)
* [Ubuntu Packages - libsox-fmt-mp3](https://packages.ubuntu.com/xenial/amd64/libsox-fmt-mp3)
