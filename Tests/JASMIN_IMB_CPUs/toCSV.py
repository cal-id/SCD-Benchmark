import os
import re
import json


# import the hostgroup information from a file
with open("parseHostGroups/hostGroupsByHostname.json", "r") as fHandle:
    hostGroupsFromHost = json.loads(fHandle.read())

# set up the headers for the csv files

RESOURCEOUTPUTS = [
    ("CPU time", "sec."),
    ("Max Memory", "MB"),
    ("Average Memory", "MB"),
    ("Total Requested Memory", "MB"),
    ("Delta Memory", "MB"),
    ("Max Swap", "MB"),
    ("Max Processes", ""),
    ("Max Threads", "")
]

PROTOCOLHEADERS = ["Protocols Seen"]

HOSTHEADERS = ["Number of Hosts", "Hosts Used", "Host Groups"]

MISCHEADERS = ["Exclusive", "CPUs"]

HEADERS = (["File Name", "Latency"] +
           [metric if unit == "" else metric + " (" + unit + ")" for metric,
            unit in RESOURCEOUTPUTS] + PROTOCOLHEADERS + HOSTHEADERS +
           MISCHEADERS)


outputFiles = os.listdir("outputs")
fileData = []  # [[name, latency, ...], [...], ...]
fileBandwidths = []  # [[0, 23, 26, 75, ...], [...], ...]

# read the content
for outputFile in outputFiles:
    with open(os.path.join("outputs", outputFile), "r") as fHandle:
        thisFileData = [outputFile]  # the list to add to thisFileData
        thisFileBandwidths = []
        start = False  # a flag to set True after reading the table header
        content = fHandle.read()
        lines = content.splitlines()

        # Deal with data from output table
        for line in lines:
            if start is True:
                # if reading the table of data
                basicLine = line.strip()  # parse this line into words

                # IF FINISHED
                if basicLine == "":  # if the data is over
                    break
                elements = basicLine.split()

                # DO LATENCY
                if len(thisFileData) < 2:  # if no latency then append it
                    thisFileData.append(elements[2])

                # DO BANDWIDTHS
                thisFileBandwidths.append(elements[3])

                # DO MESSAGESIZE
                if len(fileData) < 1:
                    # if the first file then use the messageSizes that it used
                    HEADERS.append(elements[0])

            # WATCH FOR THE BEGINING OF THE TABLE
            if "       #bytes #repetitions      t[usec]   Mbytes/sec" in line:
                start = True

        # Do LSF data
        for metric, unit in RESOURCEOUTPUTS:
            regEx = r'(?<=' + metric + ' : ).*(?=\n)'
            search = re.findall(regEx, content)
            if len(search) != 1:
                print(outputFile, regEx, metric, unit, search, len(search))
                raise Exception()
            thisFileData.append(search[0].split()[0])

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
                    thisFileData.append("-".join(setOfMethods))
                    break

        # Do number of hosts and hosts used
        hosts = re.findall("(?<=\<)\d+\*[A-Za-z0-9]+\..+\.rl\.ac\.uk(?=\>)",
                           content)
        thisFileData.append(str(len(hosts)))
        thisFileData.append("-".join(hosts))
        thisFileData.append("-".join(hostGroupsFromHost[host.split("*", 1)[1]]
                                     for host in hosts))

        # Do exclusive
        search = re.search(r"(?<=\n)#BSUB -x", content)
        thisFileData.append("1" if search is not None else "0")

        # Do number of CPUs
        if "-cpu_bind=MAP_CPU" in content:
            thisFileData.append("2")
        elif "numactl --cpunodebind=0" in content:
            thisFileData.append("1")
        else:
            raise ValueError("Should have used one or two CPUs, didn't find"
                             "either of the flags")

        # Append everything for this file
        fileData.append(thisFileData)
        fileBandwidths.append(thisFileBandwidths)


with open("out.csv", "w") as fHandle:
    # write headers
    fHandle.write(",".join(HEADERS) + "\n")

    # write content
    for data, band in zip(fileData, fileBandwidths):
        fHandle.write(",".join(data) + "," + ",".join(band) + "\n")
