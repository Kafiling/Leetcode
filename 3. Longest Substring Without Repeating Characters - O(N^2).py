class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = deque()
        longest = 0
        for i in s:
            if i in queue :
                # pop char until i
                while True:
                    x = queue.popleft()
                    if x == i : break
            # add i to queue
            queue.append(i)
            # update longest
            if len(queue) > longest : 
                longest = len(queue)
        return longest


            
        
