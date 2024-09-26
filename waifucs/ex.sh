#!/bin/bash

# 要处理的视频目录
VID_DIR="/home/pbox/snake/data/video/gf/song/qpy"

# # 处理目录下的每一个文件
# for FILE in "$VID_DIR"/*; do
#   # 检查文件是否是视频（这只是一个简单的检查，可能需要根据具体情况进行修改）
#   if [[ $FILE == *.mkv ]]; then
#     # 为每个视频文件创建一个新的目录
#     NEW_DIR="${FILE%.*}_frames"
#     mkdir -p "$NEW_DIR"

#     # 使用ffmpeg抽取关键帧，将输出目录设置为新创建的目录
#     ffmpeg -ss 1:40 -i "$FILE" -to 42:30 -vf "select=eq(pict_type\,I),crop=in_w:in_h-260:0:130" -vsync vfr "$NEW_DIR/${FILE%.*}"_output_%03d.png
#   fi
# done




# 要处理的视频目录
# VID_DIR="/mnt/e/video/qyn2"

# 处理目录下的每一个文件
for FULL_FILE_PATH in "$VID_DIR"/*; do
  FILE="$(basename -- $FULL_FILE_PATH)"
  # 检查文件是否是视频（这只是一个简单的检查，可能需要根据具体情况进行修改）
  if [[ $FILE == *.mkv ]]; then
    # 为每个视频文件创建一个新的目录
    NEW_DIR="$VID_DIR/${FILE%.*}_frames"
    mkdir -p "$NEW_DIR"

    # 使用ffmpeg抽取关键帧，将输出目录设置为新创建的目录
    # ffmpeg -ss 1:33 -i "$FULL_FILE_PATH" -to 41:30 -vf "select=eq(pict_type\,I),crop=in_w:in_h-260:0:130" -vsync vfr "$NEW_DIR/${FILE%.*}"_output_%03d.png
# 1:50  42:50 qyn2
# 1:47  42:00 chanan
# 1:38  42:15
    # ffmpeg -ss 00:00 -i "$FULL_FILE_PATH" -to 41:15 -vf "select=eq(pict_type\,I),crop=in_w:in_h-260:0:130" -vsync vfr "$NEW_DIR/${FILE%.*}"_output_%03d.png
    ffmpeg -ss 1:40 -i "$FULL_FILE_PATH" -to 42:15 -vf "select=eq(pict_type\,I)" -vsync vfr "$NEW_DIR/${FILE%.*}"_output_%03d.png
    # ffmpeg -ss 00:00 -i "$FULL_FILE_PATH" -to 36:20 -vf "select=eq(pict_type\,I),crop=in_w:in_h-270:0:135" -vsync vfr "$NEW_DIR/${FILE%.*}"_output_%03d.png
  fi
done
