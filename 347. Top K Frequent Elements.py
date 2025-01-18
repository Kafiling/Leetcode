class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mem = {}
        ans = []
        for i in nums:
            if i in mem:
                mem[i] += 1
            else:
                mem[i] = 1
        for j in range(k):
            max = 0
            for i in mem: 
                if mem[i] > max:
                    max = mem[i]
                    temp = i
            ans.append(temp)
            mem[temp] = 0
        return ans
