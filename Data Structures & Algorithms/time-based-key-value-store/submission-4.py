import bisect
from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmap:
            return ""

        vals = self.hmap[key]
        idx = bisect.bisect_left(vals, timestamp, key=lambda x: x[0])
        if idx < len(vals) and vals[idx][0] <= timestamp:
            return vals[idx][1]
        if idx > 0 and vals[idx-1][0] <= timestamp:
            return vals[idx-1][1]
        return ""
        

        
