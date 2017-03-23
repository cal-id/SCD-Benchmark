#! /bin/bash
hostgroups=(scarf10 scarf11 scarf12 scarf13 scarf14 scarf15 scarf16)
# Make the outputs directory if it doesn't exist
mkdir -p $PWD/outputs
for specificHost in ${hostgroups[@]}; do # For each hostgroup
    for perTile in 2 4; do # Span one node or two
        if [ $perTile -eq 2 ]; then
            # If going between nodes, specify different interconnect flags
            pFlagOptions=(-TCP -IBV)
        else
            # If not, there are no interconnect flags
            pFlagOptions=("")
        fi
	    for pFlag in "${pFlagOptions[@]}"; do # Step through interconnect flags
            for repeat in 1 2 3 4 5; do # repeat the benchmark

bsub << %EndOfInput%
#BSUB -x
#BSUB -n 4
#BSUB -R "span[ptile=$perTile]"
#BSUB -J HPL
#BSUB -o $PWD/outputs/%J.out
#BSUB -e $PWD/outputs/%J.err
#BSUB -W 1:00
#BSUB -m "$specificHost"
module load intel/15.3
module load intel/mkl/11.3.1.150
mpirun -lsf -prot $pFlag $PWD/xhpl
%EndOfInput%

            done
        done
    done
done
