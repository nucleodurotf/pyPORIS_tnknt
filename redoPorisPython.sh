#!/bin/bash

# Working directory clean
# Set the clean environment variable
export PORIS_CLEAN=1

# Execute the doPorisPython.sh
./doPorisPython.sh $1 || { echo 'doPorisPython.sh failed' ; exit 1; }
