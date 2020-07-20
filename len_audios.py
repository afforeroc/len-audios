#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Convert a certain number seconds to minutes."""
# sudo apt-get install sox
# sudo apt-get install lame
# sudo apt-get install libsox-fmt-mp3

import os
import subprocess


def ffprobe_obtain_length(audio_pathfile):
    """Return audio file length in seconds."""
    cmnd = [
        'ffprobe', '-show_entries', 'format=duration', '-of',
        'default=noprint_wrappers=1:nokey=1', audio_pathfile
    ]
    output_sub = subprocess.Popen(cmnd,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)
    output, _ = output_sub.communicate()
    output = str(output)
    output = output[2:-1]  # remove (b', ')
    output = output.replace("\\n", " ")
    return float(output)


def sox_obtain_length(audio_pathfile):
    """Return audio file length in seconds."""
    cmnd = ['sox', audio_pathfile, '-n', 'stat']
    output_sub = subprocess.Popen(cmnd,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)
    _, output = output_sub.communicate()
    output = str(output)
    output = output[2:-1]  # remove (b', ')
    output = output.split("\\n")
    seconds_line = output[1]
    seconds = seconds_line.replace('Length (seconds):', '')
    return float(seconds)

def add_mp3_ext(audio_pathfile):
    """Add '.mp3' extension on audio file if don't have it."""
    flag = 0
    if not audio_pathfile.endswith('.mp3'):
        flag = 1
        new_audio_pathfile = f'{audio_pathfile}.mp3'
        os.rename(audio_pathfile, new_audio_pathfile)
        audio_pathfile = new_audio_pathfile
    return audio_pathfile, flag

def del_mp3_ext(audio_pathfile, flag_mp3):
    """Delete '.mp3' extension on audio file if didn't have it."""
    if flag_mp3:
        old_audio_pathfile = audio_pathfile.replace('.mp3', '')
        os.rename(audio_pathfile, old_audio_pathfile)


def obtain_total_seconds(audios_folder):
    """Obtain total length in seconds of all audios of 'audios_folder'."""
    ffprobe_seconds = 0
    sox_seconds = 0
    for audio_file in os.listdir(audios_folder):
        audio_pathfile = os.path.join(audios_folder, audio_file)
        audio_pathfile, flag_mp3 = add_mp3_ext(audio_pathfile)
        ffprobe_seconds += ffprobe_obtain_length(audio_pathfile)
        sox_seconds += sox_obtain_length(audio_pathfile)
        del_mp3_ext(audio_pathfile, flag_mp3)
    return ffprobe_seconds, sox_seconds


def seconds_to_min_sec(total_seconds):
    """Convert a certain number seconds to minutes + seconds."""
    minutes = int(total_seconds // 60)
    seconds = total_seconds - 60 * minutes
    seconds = round(seconds, 2)
    return minutes, seconds


def seconds_to_dec_minutes(total_seconds):
    """Convert a certain number seconds to minutes using decimal format."""
    minutes_dec = total_seconds / 60
    return round(minutes_dec, 2)


def main():
    """Convert a certain number seconds to minutes."""
    ffprobe_seconds, sox_seconds = obtain_total_seconds('audios')
    ffprobe_minutes = seconds_to_dec_minutes(ffprobe_seconds)
    sox_minutes = seconds_to_dec_minutes(sox_seconds)
    print('Using ffprobe')
    #print(f'{ffprobe_seconds} seconds')
    print(f'{ffprobe_minutes} minutes\n')
    print('Using sox')
    #print(f'{sox_seconds} seconds')
    print(f'{sox_minutes} minutes')


if __name__ == '__main__':
    main()
