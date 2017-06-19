#! /bin/bash
TOP_DIR="$HOME/SCARF_Hardware"
mkdir -p $TOP_DIR
cd $TOP_DIR

if ! hwloc-1.11.7/utils/lstopo/lstopo ; then

    wget https://www.open-mpi.org/software/hwloc/v1.11/downloads/hwloc-1.11.7.tar.gz
    tar -xvf hwloc-1.11.7.tar.gz
    cd hwloc-1.11.7
    ./configure
    make
    cd $TOP_DIR
fi
mkdir -p "$TOP_DIR/outputs"

for specificHost in scarf10 scarf11 scarf12 scarf13 scarf14 scarf15 scarf16; do # For each hostgroup

bsub << %EndOfInput%
#BSUB -J lstopo
#BSUB -o $TOP_DIR/outputs/%J.out
#BSUB -e $TOP_DIR/outputs/%J.err
#BSUB -W 0:01
#BSUB -m "$specificHost"
hwloc-1.11.7/utils/lstopo/lstopo --of txt
%EndOfInput%

done
