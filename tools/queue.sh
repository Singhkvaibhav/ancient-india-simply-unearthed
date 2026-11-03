#!/usr/bin/env bash
# usage: bash tools/queue.sh 5 7 9 ...  -> for each episode, wait for episodes/epNN/ep.ready, then run tools/run_ep.sh (logs in queue.log)
cd "$(dirname "$0")/.."
for n in "$@"; do
  nn=$(printf %02d $n)
  until [ -f episodes/ep$nn/ep.ready ]; do sleep 10; done
  if bash tools/run_ep.sh $nn > episodes/ep$nn/run.log 2>&1; then echo "EP$nn ok" >> queue.log; else echo "EP$nn FAILED" >> queue.log; fi
done
