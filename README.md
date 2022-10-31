# Convert BD TOPO roads into a directed graph

Download data from https://geoservices.ign.fr/bdtopo

```
time python3 bdtoporoads.py &&
time python3 cc.py &&
time python3 dedup.py &&
time python3 multibfs.py &&
time python3 colors.py &&
time python3 generate_input.py > inp.txt
```
