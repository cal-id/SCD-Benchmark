'''
Usage:
python3 parse_tex_units.py <file> <key> <siunitx_to_append>

Note: use quotes eg "\micro\second" to keep siunitx_to_append
'''


def parse_tex_units(fName, key, siunitx):
    '''
    Deals with matplotlib2tikz not accepting mpl's latex units using
    \mathregular by adding siunitx units.

    Parameters:
        fName
            The .tex file path to be parsed
        key
            The start of the line <key>={}, which you want to add the units to.
            Usually this is 'ylabel'
        siunitx
            The input to siunitx eg \micro\second. There is no need to wrap
            this with \si{...}!

    '''

    # The full content to be saved to the file after processing
    content = ""

    with open(fName, "r") as fHandle:
        for line in fHandle:
            if key == line[0:len(key)]:
                assert line[-3:] == "},\n"  # check correct ending
                assert "\si" not in line    # check not already done this line
                newLine = (line[:-3] +
                           " \si{{{}}}".format(siunitx) +
                           line[-3:])
                print("Editing ({}) -to-> ({})".format(line, newLine))
                line = newLine
            content += line

    with open(fName, "w") as fHandle:
        fHandle.write(content)

if __name__ == "__main__":
    import sys
    assert len(sys.argv) == 4
    parse_tex_units(*sys.argv[1:])
