for f in scarf* *G; do
    echo $f
    for c in L1 L2 L3; do
        grep $c $f | sed "s/│//g;s/\s\s//g;s/).*/)/"
    done | sort | uniq;
echo ----
done
