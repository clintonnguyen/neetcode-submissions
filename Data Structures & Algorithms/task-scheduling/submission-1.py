class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = defaultdict(int)
        for task in tasks:
            count[task] += 1

        res = 0
        # heap (next_time_can_be_used, left_tasks)
        heap = [(0, c) for c in count.values()]

        while heap:
            # if can run current task
            if heap[0][0] <= res:
                t, c = heapq.heappop(heap)
                if c - 1:
                    heapq.heappush(heap, (t + n + 1, c - 1))
                res += 1
            else:
                res = heap[0][0]

        return res