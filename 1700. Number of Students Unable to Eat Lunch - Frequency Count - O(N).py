class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(sandwiches)
        count = {0:0,1:0}
        for s in students:
            count[s] += 1
        for i in sandwiches:
            if count[i] > 0 :
                res -= 1
                count[i] -= 1
            else: return res
        return res

