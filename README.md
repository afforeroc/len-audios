# Length of audios
Scripts to calculate the length of all audios of a folder.

## System requeriments
* Ubuntu 20.04 LTS

## List of tools
* **len_audio.sh**: This Bash script calculate the length (seconds) of all audios using ffmpeg and bc.
* **sec_to_min.py**: This Python script calculate the length (minutes) of all audios using ffmpeg and sox.

## 1. len_audio.sh configuration
Install [ffmpeg](https://ffmpeg.org/) and [bc](https://www.gnu.org/software/bc/) software:
```
$ sudo apt-get install ffmpeg bc
```

## 2. len_audio.sh execution
```
$ sh len_audios.sh audios
```

## 3. len_audios.py configuration
Install the latest version of Python3 and verify their version.
```
$ sudo apt install python3
```
```
$ python3 --version
```

## 4. len_audios.py execution
```
$ python3 len_audios.py audios
```

### 5. Output
e.g.
```
Using ffprobe
70.93 minutes

Using sox
70.92 minutes
```

## References links
* [Stack Overflow - Bash - calculate length of all mp3 files in one folder](https://stackoverflow.com/questions/45535938/bash-calculate-length-of-all-mp3-files-in-one-folder)
