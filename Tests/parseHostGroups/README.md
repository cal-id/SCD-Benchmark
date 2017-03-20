# Parsing hostgroups

This is a python script for running on SCARF and JASMIN. It creates a json file mapping hosts to the hostgroups that they belong to. This is used by the **toCSV.py** scripts so that the hostname included in the output files can be mapped to a hostgroup in the CSV data which is recorded.

## Usage

This folder (or at least the output json file) needs to be copied into the top directory for each test on JASMIN and SCARF so that the python scripts can access it.

From **inside the folder** run: `python2.7 parseByHostgroup.py`


(for SCARF, it may be necessary to run `module load python/2.7` before)
