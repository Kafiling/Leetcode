class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        #graph with no cycle?
        #build adj list -> check for cycle

        def cycle_helper(adj: List[List[int]],u:int,visited:List[bool],recur_stack:List[bool]) -> bool:
            if not visited[u]:
                visited[u] = True
                recur_stack[u] = True
            for x in adj[u]:
                if not visited[x] and cycle_helper(adj,x,visited,recur_stack) :
                    return True
                elif recur_stack[x]:
                    return True
            recur_stack[u] = False
            return False
        def is_cycle(adj,numCourses) -> bool :
            visited = [False] * numCourses
            recur_stack = [False] * numCourses

            for c in range(numCourses):
                if not visited[c] and cycle_helper(adj,c,visited,recur_stack) :
                    return True
            return False


        adj = [[] for _ in range(numCourses)]
        for course in prerequisites:
            adj[course[0]].append(course[1])
        if is_cycle(adj,numCourses):
            return False
        return True

        

