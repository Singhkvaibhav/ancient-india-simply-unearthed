#!/usr/bin/env bash
# usage: bash tools/regallery.sh NN [beat-name] -> re-render one beat (default: gallery) and splice it into the delivered video; audio is unchanged
set -e
nn=$(printf %02d $((10#$1))); beat=${2:-gallery}; cd "$(dirname "$0")/.."
f=$(ls output/Anc${nn}_*.mp4); d=episodes/ep$nn; CLI="python3 ../../engine/cli.py"
cd $d; mkdir -p vo parts; [ -f vo/durs.json ] || $CLI tts ../../voice/en-us-lessac-medium.onnx > tts.log 2>&1
row=$($CLI tl | awk -v b=$beat '$2==b{print $1, $3}'); idx=${row% *}; start=${row#* }
rm -f parts/$(printf %02d $idx).mp4; $CLI render $idx > /dev/null
cd ../..
ffmpeg -y -loglevel error -i $f -t $start -c copy -an episodes/ep$nn/head.mp4
printf "file '%s'\nfile '%s'\n" "$PWD/episodes/ep$nn/head.mp4" "$PWD/episodes/ep$nn/parts/$(printf %02d $idx).mp4" > episodes/ep$nn/list2.txt
ffmpeg -y -loglevel error -f concat -safe 0 -i episodes/ep$nn/list2.txt -c copy episodes/ep$nn/video2.mp4
ffmpeg -y -loglevel error -i episodes/ep$nn/video2.mp4 -i $f -map 0:v -map 1:a -c copy -movflags +faststart -shortest episodes/ep$nn/final2.mp4
dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 episodes/ep$nn/final2.mp4); echo "EP$nn spliced $dur"
mv episodes/ep$nn/final2.mp4 $f
rm -rf episodes/ep$nn/parts episodes/ep$nn/head.mp4 episodes/ep$nn/list2.txt episodes/ep$nn/video2.mp4 episodes/ep$nn/vo/*.wav
