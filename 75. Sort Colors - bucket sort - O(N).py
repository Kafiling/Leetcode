class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #implementing Bucket sort
        colorCount = [0,0,0]

        for i in nums :
            colorCount[i] += 1
        
        #Overwrite the input arr
        n=0
        p=0
        for i in range(3):
            for j in range(colorCount[i]) :
                nums[p] = n
                p +=1
            n += 1
          
                
