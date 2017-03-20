#! /bin/bash
hostgroups=(scarf10 scarf11 scarf12 scarf13 scarf14 scarf15 scarf16)
# Make the outputs directory if it doesn't exist
mkdir -p $PWD/outputs
for specificHost in ${hostgroups[@]}; do
    for i in 1 2; do
        for repeat in 1 2 3 4 5; do

bsub << %EndOfInput%
#BSUB -x
#BSUB -n 2
#BSUB -R "span[ptile=$i]"
#BSUB -J PingPong
#BSUB -o $PWD/outputs/%J.out
#BSUB -e $PWD/outputs/%J.err
#BSUB -W 0:13
#BSUB -m "$specificHost"
mpirun -lsf -prot $PWD/imb/imb/src/IMB-MPI1 -iter 1000 -msglog 0:24 -iter_policy off PingPong
%EndOfInput%

        done
    done
done
