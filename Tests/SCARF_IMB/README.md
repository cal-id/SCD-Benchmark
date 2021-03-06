# Running IMB on SCARF

## Files

* **run_IMB_SCARF.sh** - The script to submit the jobs to SCARF for each hostgroup, accross nodes and within nodes and for a number of repeats
* **toCSV.py** - A python script to parse the output files under `outputs/` to a CSV file with the useful information.

## Setup / Dependencies
1. Create a top directory in home eg `/home/cseg/scarf565/SCARF_IMB`
2. Run **buildIMB.sh** (from the builds section) to create `imb/imb/src/IMB-MPI1`
3. Copy in `parseHostGroups/hostGroupsByHostname.json` - a json file mapping each host to its hostgroups
4. Run **run_IMB_SCARF.sh** from inside the top directory to submit the jobs
5. Run `python toCSV.py` to create a csv file of the output
