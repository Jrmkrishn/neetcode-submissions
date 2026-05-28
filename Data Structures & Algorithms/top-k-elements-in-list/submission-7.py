import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps = {}
        for num in nums:
            maps[num] = maps.get(num, 0) + 1
        max_heap = []
        for num, freq in maps.items():
            heapq.heappush(max_heap, (-freq, num))   
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res