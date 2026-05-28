class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] *  len(temperatures) 

        for idx, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, index = stack.pop()
                result[index] = (idx - index)
            
            stack.append((t, idx))
        return result