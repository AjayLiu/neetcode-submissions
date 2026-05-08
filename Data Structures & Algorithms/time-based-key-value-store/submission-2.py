import bisect
class TimeMap:
    def __init__(self):
        self.hmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hmap:
            self.hmap[key].append((timestamp, value))
        else:
            self.hmap[key] = [(0,""), (timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmap:
            return ""
        myList = self.hmap[key]
        idx = bisect.bisect_left(myList, (timestamp, ""))
        if idx < len(myList) and myList[idx][0] == timestamp:
            return myList[idx][1]
        return myList[idx-1][1]
        
