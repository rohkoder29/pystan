from collections import Counter
import os
from pathlib import Path


def extension_count(origin=".", top=10):
    count = Counter()
    for root, dirs, files in os.walk(origin):
        for file in files:
            count[Path(file).suffix] += 1
    return count.most_common(top)


rsp = extension_count()
print(rsp)
