# HPL.dat

Sources [1](http://www.netlib.org/benchmark/hpl/tuning.html#tips) [2](http://www.netlib.org/benchmark/hpl/faqs.html)

## Lines:
1. Title
2. Title
3. The output file name (not used)
4. Specify `stout`
5. Only giving one problem size
6. `20GB` is avaliable as RAM on the cloud (minimum accross SCARF, Cloud and JASMIN). This is `2.50x10^9` double precision elements. 90% of this number is `2.25x10^9`. The square root is `47434` so this is a rough value for N. [2] The actual value should be the nearest multiple of NB [2] so 47520
7. Only giving one NB
8. NB should be in the range `[32 ... 256]` from initial testing, `180` was chosen
9. Row-major is recommended [1]
10. Only giving one process grid
11. P and Q should be approximately equal with PxQ = number of nodes. With 4 nodes, `2` `2` is the best option [1]
12. See 11.
13. `16.0` will cover most cases [1]
14. Only giving one panel fact
15. 'A good start' [1]
16. Only giving one
17. 'A good start' [1] - opted for 4 didn't seem to make a difference
18. Only giving one
19. 'A good start' [1]
20. Only giving one
21. 'A good start' [1]
22. Only giving one
23. One most likely want to use `1` [1]
24. Only giving one
25. Use `1` if you do not know better [1]
26. For large problem sizes 2 is likely to be more efficient [1]
27. Swapping threshold should be of the order of block size **NB**
28. Line 28 doesn't matter [1]
29. No doubt `0` is better [1]
30. Same as in [1]
31. To be safe use `8`
