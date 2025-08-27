class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # step 1 find what row are target might be in
        indexArr = []
        for list in matrix:
            indexArr.append(list[len(list)-1])
        print(indexArr)
        # 1.1 Linear search (indexArr is already sorted)
        if indexArr[-1] < target:
            return False
        i = 0
        while indexArr[i] < target:
            i += 1
        
        # Now target is in row index i
        # step 2 find if target exist within that row -> Binary search
        l,r = 0,len(matrix[i])-1
        while l <= r :
            mid = (l+r)//2
            
            if matrix[i][mid] > target:
                r = mid-1
            elif matrix[i][mid] < target:
                l = mid+1
            else:
                return True
        else:
            return False
