#!/bin/bash
# Calculate the length of all audios in seconds."""
echo "Reading all audio files...";
TOTAL_LENGTH=0;
for audio_file in ./*.mp3;
do
    LENGTH="$(ffprobe -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$audio_file" 2>/dev/null)";
    echo "$audio_file, $LENGTH";
    TOTAL_LENGTH="$TOTAL_LENGTH+$LENGTH"
done;
echo "$TOTAL_LENGTH" | bc