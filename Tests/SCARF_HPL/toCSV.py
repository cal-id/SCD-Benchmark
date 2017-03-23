import os
import re
import json


# import the hostgroup information from a file
with open("parseHostGroups/hostGroupsByHostname.json", "r") as fHandle:
    hostGroupsFromHost = json.loads(fHandle.read())

# Set up the headers for the csv files
HPLOUTPUTS = ['T/V', 'N', 'NB', 'P', 'Q', 'Time', 'Gflops']

RESOURCEOUTPUTS = [
    ("CPU time", "sec."),
    ("Max Memory", "MB"),
    ("Average Memory", "MB"),
    ("Total Requested Memory", "MB"),
    ("Delta Memory", "MB"),
    ("Max Swap", "MB"),
    ("Max Processes", ""),
    ("Max Threads", ""),
    ("Run time", "sec."),
    ("Turnaround time", "sec.")
]

PROTOCOLHEADERS = ["Protocols Seen"]

HOSTHEADERS = ["Number of Hosts", "Hosts Used", "Host Groups"]

MISCHEADERS = ["Start Time", "Exclusive"]

HEADERS = (["File Name"] + HPLOUTPUTS +
           [metric if unit == "" else metric + " (" + unit + ")" for metric,
            unit in RESOURCEOUTPUTS] + PROTOCOLHEADERS + HOSTHEADERS +
           MISCHEADERS)
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
    for metric, unit in RESOURCEOUTPUTS:
        regEx = r'(?<=' + metric + ' : ).*(?=\n)'
        search = re.findall(regEx, content)
        if len(search) != 1:
            print(outputFile, regEx, metric, unit, search, len(search))
            raise Exception()
        thisRow.append(search[0].split()[0])

    # Do methods of communication
    for index, line in enumerate(lines):
        if re.search(" host \| 0", line) is not None:
            if re.search("======\|", lines[index + 1]) is not None:
                interestedLineIndexOffset = 2
                setOfMethods = set()
                while lines[index + interestedLineIndexOffset] != "":
                    thisLine = lines[index + interestedLineIndexOffset]
                    for meth in thisLine.split(":", 1)[1].split():
                        setOfMethods.add(meth)
                    interestedLineIndexOffset += 1
                thisRow.append("-".join(setOfMethods))
                break
    # Do number of hosts and hosts used
    hosts = re.findall("(?<=\<)\d+\*[A-Za-z0-9]+\..+\.rl\.ac\.uk(?=\>)",
                       content)
    thisRow.append(len(hosts))
    thisRow.append("-".join(hosts))
    thisRow.append("-".join(hostGroupsFromHost[host.split("*", 1)[1]]
                            for host in hosts))
    # Do start time
    search = re.findall(r"(?<=HPL_pdgesv\(\) start time ).*(?=\n)", content)
    try:
        assert len(search) == 1
    except:
        print(search, outputFile, len(search))
    thisRow.append(search[0])
    # Do exclusive
    search = re.search(r"(?<=\n)#BSUB -x", content)
    thisRow.append("1" if search is not None else "0")
    outputText += ",".join(str(el) for el in thisRow) + "\n"

with open("out.csv", "w") as fHandle:
    fHandle.write(outputText)
