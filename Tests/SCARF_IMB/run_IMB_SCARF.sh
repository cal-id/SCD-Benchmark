#! /bin/bash
hostgroups=(scarf10 scarf11 scarf12 scarf13 scarf14 scarf15 scarf16)
# Make the outputs directory if it doesn't exist
mkdir -p $PWD/outputs
for specificHost in ${hostgroups[@]}; do # For each hostgroup
    for perTile in 1 2; do # Span one node or two
        if [ $perTile -eq 1 ]; then
            # If going between nodes, specify different interconnect flags
            pFlagOptions=(-TCP -IBV)
        else
            # If not, there are no interconnect flags
            pFlagOptions=("")
        fi
        for pFlag in "${pFlagOptions[@]}"; do # Step through interconnect flags
            for repeat in 1 2 3 4 5; do # Repeat the benchmark

bsub << %EndOfInput%
#BSUB -x
#BSUB -n 2
#BSUB -R "span[ptile=$perTile]"
#BSUB -J PingPong
#BSUB -o $PWD/outputs/%J.out
#BSUB -e $PWD/outputs/%J.err
#BSUB -W 0:45
#BSUB -m "$specificHost"
mpirun -lsf -prot $pFlag $PWD/imb/imb/src/IMB-MPI1 -iter 1000 -time 200 -msglog 0:24 -iter_policy off PingPong
%EndOfInput%

            done
        done
    done
done
