#!/bin/bash

if [ $# -lt 1 ]; then
    echo "Usage: $0 <command> [arguments...]"
    exit 1
fi

# Check if any arguments are provided
if [ $# -lt 1 ]; then
    echo "No arguments provided for command "
    exit 1
fi

export PATH=$PATH:/usr/ensta/pack/simplescalar-3v0d/bin/:/usr/ensta/pack/simplescalar-3v0d/simplesim-3.0/

# Iterate over the remaining arguments and execute the command with each argument
for ARG in "$@"; do
    echo "Executing command with a cache IL1 and DL1 of '$ARG' KB"
    sim-outorder -redir:sim ./sim_dij_A7_"$ARG" -fetch:ifqsize 4 -decode:width 2 -issue:inorder false -issue:width 4 -commit:width 2 -ruu:size 2 -lsq:size 8 -res:imult 1 -res:ialu 1 -res:fpalu 1 -res:fpmult 1 -bpred:bimod 2048 -bpred:btb 256 2 -bpred:comb 1024 -fetch:mplat 8 -cache:dl1 dl1:"$ARG":32:2:l -cache:il1 il1:"$ARG":32:2:l -cache:dl2 ul2:512:32:8:l dijkstra_small.ss input.dat et bf.ss input_small.asc
    # Add any additional processing or commands here
done