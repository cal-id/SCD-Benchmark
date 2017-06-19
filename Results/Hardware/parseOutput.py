import os
import re


for fName in os.listdir("outputs"):
    with open(os.path.join("outputs", fName), "r") as fh:
            content = fh.read()
    boxes = content.split("The output (if any) follows:", 1)[1].split("PS")[0]
    hostgroupSearch = re.findall(r'#BSUB\s+-m\s+"(.*)"', content)
    assert len(hostgroupSearch) == 1
    hostgroup = hostgroupSearch[0]
    with open(os.path.join("outputs", hostgroup), "w") as fh:
        fh.write(boxes)
