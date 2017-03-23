#! /bin/bash

source /etc/profile.d/modules.sh
module load openmpi-1.10-x86_64

REPEATS=30
HOME_DIR=/home/tan49775  # should contain hpl-2.2 and Cloud_HPL
START_DIR=$HOME_DIR/Cloud_HPL
COUNT=$START_DIR/count


# Make the output directory if needed
mkdir -p $START_DIR/outputs

num=$(date +"%Y%m%d_%H%M%S")
outputFile=$START_DIR/outputs/$num.out
errorFile=$START_DIR/outputs/$num.err

# If the count file does not exist then initialise it
if [ ! -s $COUNT ]; then echo "1" > $COUNT; fi

# If done enough repeats then exit
if [ $(cat $COUNT) -gt $REPEATS ]; then exit 0; fi

# Run the benchmark
mpirun -np 4 $HOME_DIR/hpl-2.2/bin/Linux_SL6_Intel64/xhpl 2> $errorFile >> $outputFile

# Increment the count file
echo $(($(cat $COUNT) + 1)) > $COUNT
