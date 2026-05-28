class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        max_count = 0
        for num in nums:
            if num - 1 in nums:
                seen.add(num)
            else:
                count = 1
                while num+1 in nums:
                    count+=1
                    num += 1
                max_count = max(count, max_count)
        return max_count