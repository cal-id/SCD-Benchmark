#! /bin/bash
hostgroups=(ivybridge512G ivybridge2000G haswell256G ivybridge128G broadwell256G)
# Make the outputs directory if it doesn't exist
mkdir -p $PWD/outputs
for specificHost in ${hostgroups[@]}; do # For each hostgroup
    for repeat in $(seq 5); do # repeat the benchmark
        cmds=("-cpu_bind=MAP_CPU:0,15" "numactl --cpunodebind=0 --")
        for cmd in "${cmds[@]}"; do

bsub << %EndOfInput%
#BSUB -x
#BSUB -q par-multi
#BSUB -n 2
#BSUB -R "span[ptile=2]"
#BSUB -J PingPong
#BSUB -o $PWD/outputs/%J.out
#BSUB -e $PWD/outputs/%J.err
#BSUB -W 0:45
#BSUB -m "$specificHost"
mpirun.lotus -prot $cmd $PWD/imb/imb/src/IMB-MPI1 -iter 1000 -time 200 -msglog 0:24 -iter_policy off PingPong
%EndOfInput%

        done
    done
done
