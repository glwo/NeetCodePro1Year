import heapq
import math
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            dist = math.sqrt((point[0])**2 + (point[1])**2)
            heapq.heappush(distances, (dist, point))

        res = []
        for i in range(k):
            curr = heapq.heappop(distances)
            res.append(curr[1])

        return res
