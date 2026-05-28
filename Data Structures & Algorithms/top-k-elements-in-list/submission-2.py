class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps = {}
        for num in nums:
            maps[num] = 1 + maps.get(num, 0)
        arr = []
        for num, val in maps.items():
            arr.append([val, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
        