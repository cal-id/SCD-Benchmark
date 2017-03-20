#! /bin/bash
# westmere48G doesn't work, removed it
hostgroups=(haswell256G ivybridge128G broadwell256G ivybridge128G ivybridge512G ivybridge128G ivybridge2000G broadwell256G)
# Make the outputs directory if it doesn't exist
mkdir -p $PWD/outputs
for specificHost in ${hostgroups[@]}; do
    for i in 1 2; do
        for repeat in 1 2 3 4 5; do

bsub << %EndOfInput%
#BSUB -x
#BSUB -q par-multi
#BSUB -n 2
#BSUB -R "span[ptile=$i]"
#BSUB -J PingPong
#BSUB -o $PWD/outputs/%J.out
#BSUB -e $PWD/outputs/%J.err
#BSUB -W 0:13
#BSUB -m "$specificHost"
mpirun.lotus -prot $PWD/imb/imb/src/IMB-MPI1 -iter 1000 -msglog 0:24 -iter_policy off PingPong
%EndOfInput%

        done
    done
done
