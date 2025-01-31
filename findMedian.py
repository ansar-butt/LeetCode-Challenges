# 295. Find Median from Data Stream
"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.
For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:
MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
"""


# Space Complexity: 99th Percentile
class MedianFinder:

    def __init__(self):
        self.l = []

    def addNum(self, num: int) -> None:
        if not self.l:
            self.l.append(num)
            return

        if num >= self.l[-1]:
            self.l.append(num)
            return

        for i in range(0, len(self.l)):
            if self.l[i] > num:
                self.l.insert(i, num)
                break

    def findMedian(self) -> float:
        n = len(self.l)
        if n % 2 == 1:
            return self.l[n // 2]
        return (self.l[n // 2] + self.l[n // 2 - 1]) / 2
