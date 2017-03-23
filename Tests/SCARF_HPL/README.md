# Running HPL on SCARF

## Files
* **run_HPL_SCARF.sh** - The script to submit the jobs to SCARF for each hostgroup, accross nodes and within nodes and for a number of repeats
* **toCSV.py** - A python script to parse the output files under `outputs/` to a CSV file with the useful information.

## Setup / Dependencies
1. Create a top directory in home and move to it eg `/home/cseg/scarf565/SCARF_HPL`
2. Run `bsub -m scarf10 "cp /apps/procspec/hpl/2.2/bin/Linux_Intel64/xhpl ."` to copy SCARF10's executable
3. Copy in `parseHostGroups/hostGroupsByHostname.json` - a json file mapping each host to its hostgroups
4. Copy in `HPL.dat` from `Configure_HPL` - the HPL config file
4. Run **run_HPL_SCARF.sh** from inside the top directory to submit the jobs
5. Run `python toCSV.py` to create a csv file of the output
