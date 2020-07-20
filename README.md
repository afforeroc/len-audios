# IBM Speech To Text Tools
Some tools to check elements of IBM STT service.

## System requeriments
* Ubuntu 20.04 LTS

## List of tools
* **len_audio.sh**: This Bash script calculate the length of all audios in seconds.
* **sec_to_min.py**: This Python script convert a certain number seconds to minutes.

## 1. len_audio.sh configuration
Install [ffmpeg](https://ffmpeg.org/) and [bc](https://www.gnu.org/software/bc/) software:
```
$ sudo apt-get install ffmpeg bc
```

## 2. len_audio.sh execution
```
$ sh len_audios.sh
```

## 3. sec_to_min.py configuration
Install the latest version of Python3 and verify their version.
```
$ sudo apt install python3
```
```
$ python3 --version
```

## 4. sec_to_min.py execution
e.g.
```
$ python3 sec_to_min.py 200.3
```
```
3.34 minutes
3 minutes 20.30 seconds
```

## References links
* [Stack Overflow - Bash - calculate length of all mp3 files in one folder](https://stackoverflow.com/questions/45535938/bash-calculate-length-of-all-mp3-files-in-one-folder)
