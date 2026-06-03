class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-s for s in stones]
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            stone1 = heapq.heappop(maxheap)
            stone2 = heapq.heappop(maxheap)
            if stone1 != stone2:
                heapq.heappush(maxheap, (stone1 - stone2))
        if len(maxheap) == 1:
            return abs(maxheap[0])
        else:
            return 0