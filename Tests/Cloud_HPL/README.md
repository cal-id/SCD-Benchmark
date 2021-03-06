# Running IMB on Cloud

## Files
* **run_HPL_Cloud_1Node.sh** - The script to load the mpi modules and run HPL on one VM.
* **run_HPL_Cloud_2Nodes.sh** - The script to load the mpi modules and run HPL accross two VMs.
* **toCSV.py** - A script to parse the output for files under `outputs/` to a CSV file with the userful information

## Setup / Dependencies
###
NOTE: The SCD cloud limits a maximum of 20GB of RAM at a time. So I did the tests accross two VMs (10GB each) then deleted the VMs and did the tests over one VM (20GB)


### 1 Node
This requires one cloud VM with at least 4 CPUs and 20GB of RAM

1. Create a top directory under the main VM eg `/home/tan49775/Cloud_HPL`
2. Install HPL in the home directory of both VMs using **build.sh** (note that it depends on `openmpi-devel` and sourcing the modules in the IMB section (making it easier to follow the whole script rather than just the HPL section))
3. Copy in the `HPL.dat` from `Configure_HPL`
4. Change `HOME_DIR` and `START_DIR` in **run_HPL_Cloud_1Node.sh**
5. Make script executable `chmod 755 run_HPL_Cloud_1Node.sh`
6. If it isn't the first time running these tests, delete the previous count file `rm -f count`
7. Setup a crontab to run the script `crontab -e` eg.
    ```bash
    50 * * * * /home/tan49775/Cloud_HPL/run_HPL_Cloud_1Node.sh
    ```
8. Run `python toCSV.py` to create a csv file of the output

### 2 Nodes
This requires 2 cloud VMs with at least 10GB of RAM and 2 CPUs each

1. Do steps 1, 2, 3, 4, 5, 6 as above
2. Change the host address on line 27 in **run_HPL_Cloud_2Nodes.sh**
3. Setup a similar crontab with `crontab -e` eg.
    ```bash
    50 * * * * /home/tan49775/Cloud_HPL/run_HPL_Cloud_2Nodes.sh
    ```
4. Run the python script as above (step 8)

### Combining
The script `mergeCSVs.sh` can be used to join the two csv files and include the number of hosts. The first csv file provided (default `out1.csv`) is the results for one host. The second provided (default `out2.csv`) is the csv file for two hosts. It outputs to standard out.

A typical use, sending the merged csv to `out.csv`:

```bash
./mergeCSVs.sh outputsOneHost.csv outputsTwoHost.csv > out.csv
```
