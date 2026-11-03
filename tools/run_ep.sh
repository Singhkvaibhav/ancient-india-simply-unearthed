#!/usr/bin/env bash
# usage: bash tools/run_ep.sh NN  -> tts, check, render (2 workers), audio, mux, copy to output/ (no git)
set -e
nn=$(printf %02d $((10#$1)))
cd "$(dirname "$0")/../episodes/ep$nn"
CLI="python3 ../../engine/cli.py"
mkdir -p vo; $CLI tts ../../voice/en-us-lessac-medium.onnx > tts.log 2>&1
$CLI check > check.log 2>&1 || { cat check.log; exit 2; }
n=$($CLI tl | grep -c '^[0-9]')
rm -rf parts; mkdir -p parts
# balance by duration: greedy split of beats over 2 workers
A=$($CLI tl | python3 -c "
import sys
rows=[l.split() for l in sys.stdin if l[0].isdigit() and len(l.split())==4]
a=b=0; la=[]; lb=[]
for r in sorted(rows,key=lambda r:-float(r[3])):
    if a<=b: la.append(r[0]); a+=float(r[3])
    else: lb.append(r[0]); b+=float(r[3])
print(','.join(sorted(la,key=int))+' '+','.join(sorted(lb,key=int)))")
set -- $A
$CLI render $1 > parts_w0.log 2>&1 &
[ -n "$2" ] && $CLI render $2 > parts_w1.log 2>&1 &
wait
[ $(ls parts/[0-9]*.mp4 | wc -l) -eq $n ] || { echo "missing parts"; exit 3; }
ls parts/[0-9]*.mp4 | sed "s|^|file '$PWD/|;s|$|'|" > parts/list.txt
ffmpeg -y -loglevel error -f concat -safe 0 -i parts/list.txt -c copy video.mp4
$CLI audio > audio.log 2>&1
ffmpeg -y -loglevel error -i video.mp4 -i mix.wav -c:v copy -c:a aac -b:a 192k -movflags +faststart -shortest final.mp4
NAME=$(python3 -c "import sys;sys.path.insert(0,'../..');from engine import plan;print(plan.BY_EP[$((10#$nn))][2])")
cd ../..
cp episodes/ep$nn/final.mp4 output/Anc${nn}_$NAME.mp4; cp episodes/ep$nn/ep$nn.srt output/Anc$nn.srt
python3 tools/yt.py $((10#$nn)); python3 tools/thumb.py $((10#$nn))
echo "EP$nn done"
rm -rf episodes/ep$nn/parts episodes/ep$nn/vo/*.wav episodes/ep$nn/mix.wav episodes/ep$nn/video.mp4 episodes/ep$nn/final.mp4
