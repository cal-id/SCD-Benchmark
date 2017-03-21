# Running IMB on Cloud

## Files
* **run_IMB_Cloud.sh** - The script to load the mpi modules and run IMB on either one vm or two.
* **toCSV.py** - A script to parse the output for files under `outputs/` to a CSV file with the userful information

## Setup / Dependencies
This requires two cloud VMs, the main one needs at least two CPUs (to run PingPong on its own).

1. Create a top directory under the main VM eg `/home/tan49775/Cloud_IMB`
2. Setup ssh between the two VMs following **setupSSH.sh**
3. Install IMB in the home directory of both VMs using **build.sh**
4. Change `HOME_DIR` and `START_DIR` in **run_IMB_Cloud.sh**
5. If it isn't the first time running these tests, delete the previous count file `rm -f count`
6. Setup a crontab to run the script `crontab -e` eg.
    ```bash
    05,25,45 * * * * /home/tan49775/Cloud_IMB/run_IMB_Cloud.sh
    ```
7. Run `python toCSV.py` to create a csv file of the output
