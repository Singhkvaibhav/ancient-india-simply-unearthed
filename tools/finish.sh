#!/usr/bin/env bash
# usage: bash tools/finish.sh NN -> deliver an episode whose final.mp4 is already built (copy, metadata, thumbnail, cleanup)
nn=$(printf %02d $((10#$1))); cd "$(dirname "$0")/.."
NAME=$(python3 -c "import sys;sys.path.insert(0,'.');from engine import plan;print(plan.BY_EP[int('$nn')][2])")
cp episodes/ep$nn/final.mp4 output/Anc${nn}_$NAME.mp4 && cp episodes/ep$nn/ep$nn.srt output/Anc$nn.srt && python3 tools/yt.py $((10#$nn)) && python3 tools/thumb.py $((10#$nn)) && \
rm -rf episodes/ep$nn/parts episodes/ep$nn/vo/*.wav episodes/ep$nn/mix.wav episodes/ep$nn/video.mp4 episodes/ep$nn/final.mp4 && echo "EP$nn delivered"
