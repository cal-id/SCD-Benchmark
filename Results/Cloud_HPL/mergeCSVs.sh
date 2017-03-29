#! /bin/bash
oneHost=${1:-out.csv}
twoHost=${2:-out2.csv}
# Catch error if either file doesn't exist or is 0 length
if [ ! -s $oneHost -o ! -s $twoHost ]; then
    echo "Usage: mergeCSVs.sh <csv - one host (out.csv)> <csv - two hosts(out2.csv)>"
    exit 1
fi;

output=`mktemp`
echo "$(head -n 1 $oneHost),Number of Hosts" > $output
tail -n +2 $oneHost | sed -e 's/$/,1/' >> $output
tail -n +2 $twoHost | sed -e 's/$/,2/' >> $output
cat $output
