#! /bin/bash
# westmere48G doesn't work, removed it
hostgroups=(ivybridge512G ivybridge2000G haswell256G ivybridge128G broadwell256G)
# Make the outputs directory if it doesn't exist
mkdir -p $PWD/outputs
for specificHost in ${hostgroups[@]}; do # For each hostgroup
    for perTile in 2 4; do # Span one or two nodes
        for repeat in 1 2 3 4 5; do # Repeat the benchmark

bsub << %EndOfInput%
#BSUB -x
#BSUB -q par-multi
#BSUB -n 4
#BSUB -R "span[ptile=$perTile]"
#BSUB -J HPL
#BSUB -o $PWD/outputs/%J.out
#BSUB -e $PWD/outputs/%J.err
#BSUB -W 1:00
#BSUB -m "$specificHost"
. /etc/profile.modules
module load intel/15.1
module load intel/mkl/11.3.1.150
mpirun.lotus -e LD_LIBRARY_PATH=$LD_LIBRARY_PATH -prot /apps/src/hpl/hpl-2.2/bin/Linux_Intel64/xhpl
%EndOfInput%

        done
    done
done
