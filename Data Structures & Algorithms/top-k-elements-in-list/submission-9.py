import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        maps = {}
        res = []
        for num in nums:
            maps[num] = maps.get(num, 0) + 1
        
        for num in maps:
            heapq.heappush(heap, (-maps[num], num))
        
        for _ in range(k):
            _ , num = heapq.heappop(heap) 
            res.append(num)
        return res