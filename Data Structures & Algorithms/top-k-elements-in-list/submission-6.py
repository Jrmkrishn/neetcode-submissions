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
            reg_freq, num = heapq.heappop(max_heap)  # Pop the element with the smallest negative frequency
            res.append(num)
        return res