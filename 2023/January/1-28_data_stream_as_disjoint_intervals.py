class SummaryRanges:

    def __init__(self):
       self.start = {}
       self.end = {}
       self.seen = set() 

    # O(1) time
    def addNum(self, value: int) -> None:
        if value in self.seen:
            return
        self.seen.add(value)

        start = value
        end = value

        if value + 1 in self.start:
            end = self.start[value + 1][1]
            self.start.pop(value + 1)

        if value - 1 in self.end:
            start = self.end[value - 1][0]
            self.end.pop(value - 1)

        interval = [start, end] 
        self.start[start] = interval
        self.end[end] = interval 

    # O(nlogn) time
    def getIntervals(self) -> List[List[int]]:
        return sorted(self.start.values())
