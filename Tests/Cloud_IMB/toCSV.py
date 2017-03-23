import os
import re

# set up the headers for the csv files

HEADERS = ["File Name", "Number of Hosts", "Latency"]


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

        # Deal with the number of hosts
        strings = re.findall("(?<=#HOSTS=)\d", content)
        assert len(strings) == 1
        thisFileData.append(strings[0])

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
                if len(thisFileData) < 3:  # if no latency then append it
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

        # Append everything for this file
        fileData.append(thisFileData)
        fileBandwidths.append(thisFileBandwidths)


with open("out.csv", "w") as fHandle:
    # write headers
    fHandle.write(",".join(HEADERS) + "\n")

    # write content
    for data, band in zip(fileData, fileBandwidths):
        fHandle.write(",".join(data) + "," + ",".join(band) + "\n")
