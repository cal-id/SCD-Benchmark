'''
Usage:
python3 parse_tex_bar_chart.py <some_bar_chart.tex>


Detail:
This script removes and lines after and including '\addplot' and upto but
not including lines starting with '\end{axis}'


Example (truncated) lines that are removed

\addplot [semithick, black]
table {%
-0.7875 70.8153333333333
0.2125 39.924
...
11.2125 295.25
};
\end{axis}
'''


def parse_tex_bar_chart(fName):
    """
    Parses the .tex bar chart plots and removes the line graph that
    matplotlib2tikz creates between the tops of each bar.
    """
    # A flag: is the current line one that should be ignored (within a plot)?
    withinPlot = False

    # The full content to be saved to the file after processing
    content = ""

    with open(fName, "r") as fHandle:
        for line in fHandle:
            if r"\addplot" == line[0:8]:
                withinPlot = True
            elif line[0:10] == r"\end{axis}":
                withinPlot = False
            if not withinPlot:
                content += line

    with open(fName, "w") as fHandle:
        fHandle.write(content)


if __name__ == "__main__":
    import sys
    assert len(sys.argv) == 2
    parse_tex_bar_chart(sys.argv[1])
