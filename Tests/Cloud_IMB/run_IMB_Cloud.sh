#! /bin/bash

source /etc/profile.d/modules.sh
module load openmpi-1.10-x86_64

REPEATS_FOR_EACH=30
HOME_DIR=/home/tan49775  # should contain imb/imb/src.. and Cloud_IMB
START_DIR=$HOME_DIR/Cloud_IMB
COUNT=$START_DIR/count


# Make the output directory if needed
mkdir -p $START_DIR/outputs

num=$(date +"%Y%m%d_%H%M%S")
outputFile=$START_DIR/outputs/$num.out
errorFile=$START_DIR/outputs/$num.err

# If the count file does not exist then initialise it
if [ ! -s $COUNT ]; then echo "1" > $COUNT; fi

# If done enough repeats of one host and two hosts then exit
if [ $(cat $COUNT) -gt $((2 * $REPEATS_FOR_EACH)) ]; then exit 0; fi

# If done enough repeats for one host then use two hosts
if [ $(cat $COUNT) -gt $REPEATS_FOR_EACH ]; then
    echo "#HOSTS=2" > $outputFile
    multiHostFlags="--prefix /usr/lib64/openmpi-1.10/ --map-by node  --rank-by node --host vm275.nubes.stfc.ac.uk,vm15.nubes.stfc.ac.uk"
else # Otherwise only use this host
    echo "#HOSTS=1" > $outputFile
    multiHostFlags=""
fi



# Run the benchmark
mpirun -np 2 $multiHostFlags $HOME_DIR/imb/imb/src/IMB-MPI1 -iter 1000 -msglog 0:24 -iter_policy off -time 200 PingPong 2> $errorFile >> $outputFile

# Increment the count file
echo $(($(cat $COUNT) + 1)) > $COUNT
