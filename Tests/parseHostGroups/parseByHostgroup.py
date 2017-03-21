#! /usr/bin/python2.7
'''A script to call "bmgroup" to parse the hostgroups into json for information
on benchmarking
    No Input
    Output:
    - hostGroupsByHostname.json
'''

# ONLY TESTED ONLY ON PYTHON2.7

# ---------------------------------- IMPORTS ----------------------------------
from __future__ import print_function
from subprocess import check_output  # so that bhosts and bmgroup can be called
# import re  # to parse the output from bhosts etc
import os  # to correctly join paths
import json  # to dump into json

# --------------------------------- SETTINGS ----------------------------------
# The directory to save the files to.
OUTPUT_DIRECTORY = os.getcwd()  # for the moment use the current directory

# Ignore host if these any of these strings are in it
HOST_LIKE_IGNORE = ["gpu"]

# Ignore host group if any of these strings are in it
# By trial and error, excluding these hosts seem to helpfully
# map host -> hostgroup one to one
HG_LIKE_IGNORE = ['scarf_intel_hosts_7_isis', 'lotus241', 'lotus2', 'lotus3',
                  'lotusf10', 'lotus_newton', 'atsrrepro', 'lotus_highmem',
                  'lotustest']

# If any of these keys are in the host group then replace with the value
HG_LIKE_ALIAS = {
    "scarf_intel_hosts_4": "scarf10",
    "scarf_intel_hosts_5": "scarf11",
    "scarf_intel_hosts_6": "scarf12",
    "scarf_intel_hosts_7": "scarf13",
    "scarf_intel_hosts_8": "scarf14",
    "scarf_15_hosts": "scarf15"
}


# --------------------------------- FUNCTIONS ---------------------------------
def getHostGroups():
    '''A function to map host to the host groups that they are in.
    The function calls bmgroup to get this information.

    example return:
        {host100: "lotus lotus2", host201: "testHostGroup"}'''
    print("Getting host groups")
    # Get the binary output from bmgroup
    # -w for wide output (don't clip strings)
    bmgroupOutput = check_output(["bmgroup", "-w"])
    print("Called bmgroups")
    # Create an empty dictionary to fill with the results from the data
    toReturn = dict()
    for line in bmgroupOutput.splitlines()[1:]:
        # step through each line of ouput except the first lines (table header)
        # each line should be of the form:
        # host group host1 host2 host3 ...
        # split the line into a list of elements
        columnsInThisLine = line.split()
        hosts = columnsInThisLine[1:]
        hostGroup = columnsInThisLine[0]
        if any(ignoreString in hostGroup for ignoreString in HG_LIKE_IGNORE):
            # Ignore some host groups
            continue
        for initial, replacement in HG_LIKE_ALIAS.items():
            # Deal with the aliases
            if initial in hostGroup:
                hostGroup = replacement
                break
        for host in hosts:
            # Step through each host for this host group
            if any(ignoreString in host for ignoreString in HOST_LIKE_IGNORE):
                # Don't do anything with the hosts to ignore
                continue
            if host in toReturn:
                # If this host is already mapped to a list of host groups,
                # append this host group.
                toReturn[host] += " " + hostGroup
            else:
                # Otherwise append the first host group for this host
                toReturn[host] = hostGroup
    return toReturn


# ------------------------------------ RUNNING --------------------------------
def run():
    'A function to wrap everything together and collect errors'
    print("starting up!")
    try:
        dictionaryOfHostGroups = getHostGroups()
        filePath = os.path.join(OUTPUT_DIRECTORY, "hostGroupsByHostname.json")
        with open(filePath, "w") as f:
            f.write(json.dumps(dictionaryOfHostGroups))
        print("Written host groups to file")
    except BaseException as e:
        print("ERROR")
        raise


if __name__ == "__main__":
    # if this script isn't being imported, then run everything
    run()
