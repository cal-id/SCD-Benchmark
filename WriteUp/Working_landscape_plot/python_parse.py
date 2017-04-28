import sys
assert len(sys.argv) == 2

withinPlot = False

content = ""

with open(sys.argv[1], "r") as fHandle:
    for line in fHandle:
        if r"\addplot" == line[0:8]:
            withinPlot = True
        elif line[0:10] == r"\end{axis}":
            withinPlot = False
        if not withinPlot:
            content += line

with open(sys.argv[1], "w") as fHandle:
    fHandle.write(content)
