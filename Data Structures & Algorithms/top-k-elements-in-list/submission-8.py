import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps = {}
        heap = []
        res = []
        for num in nums:
            maps[num] = maps.get(num, 0) + 1
        for key, val in maps.items():
            heapq.heappush(heap, (-val, key))  
        for _ in range(k):
            print(maps, heap)
            res.append(heapq.heappop(heap)[1])
        return res