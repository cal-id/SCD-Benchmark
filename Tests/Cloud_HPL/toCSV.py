import os
import re
import json


# import the hostgroup information from a file
with open("parseHostGroups/hostGroupsByHostname.json", "r") as fHandle:
    hostGroupsFromHost = json.loads(fHandle.read())

# Set up the headers for the csv files
HPLOUTPUTS = ['T/V', 'N', 'NB', 'P', 'Q', 'Time', 'Gflops']


HEADERS = (["File Name"] + HPLOUTPUTS)
outputText = ",".join(HEADERS) + "\n"


# Go through each output file
for outputFile in os.listdir("outputs"):
    # Setup a list of elements in this row starting with the output file name
    thisRow = [outputFile]
    # Open the file and read it into a variable
    with open(os.path.join("outputs", outputFile), "r") as fHandle:
        content = fHandle.read()
    # CountDown is negative if we haven't found the line two lines before the
    # line we want
    # If countDown is positive then it is literally counting down until the
    # line we want
    lines = content.splitlines()
    countDown = -1
    for line in lines:
        # Go through each line in the file
        if tuple(line.split()) == tuple(HPLOUTPUTS):  # If we are at this line
            # then we are 2 lines from the one that we want
            countDown = 2
        if countDown == 0:
            # If we are at the line we want add to the list
            thisRow += line.split()
            break
        countDown -= 1


with open("out.csv", "w") as fHandle:
    fHandle.write(outputText)
