class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-i for i in stones]
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            stone1 = heapq.heappop(maxheap)
            stone2 = heapq.heappop(maxheap)
            if stone1 != stone2:
                heapq.heappush(maxheap, -abs(stone1 - stone2))
        if len(maxheap) != 0:
            return abs(maxheap[0])
        return 0