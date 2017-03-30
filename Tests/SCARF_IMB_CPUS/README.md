# Testing IMB on SCARF, locked to CPUs

After analysing the IMB results on SCARF, the results seems to be split into two sizes for each hostgroup when communicating over SHM. This was probably down to there being two CPUs in each host. This means that the job could be on one or both of the CPUs, with an effect on the time to send a message between the two processes. Additionally, the job could move from one CPU to another CPU at any point while it is running. This could cause it to jump from one set to another.

## Files
This `run_IMB_SCARF_CPUs.sh` is adapted from `run_IMB_SCARF.sh` but only runs the job over SHM on each hostgroup. Additionally, it runs the job once forcing it to be on the same CPU (using `numactl --cpunodebind=0 --`) and again forcing it to be on different CPUs (using `-cpu_bind=MAP_CPU:0,15`).


## Usage
The usage should be the same as in `SCARF_IMB`, replacing `run_IMB_SCARF.sh` with `run_IMB_SCARF_CPUs.sh`
