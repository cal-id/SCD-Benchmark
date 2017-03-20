#! /bin/bash
# remove empty error files
for errorFile in outputs/*.err; do
    if [ ! -s $errorFile ]; then
        echo "Removing $errorFile"
        rm -rf $errorFile
    fi
done
