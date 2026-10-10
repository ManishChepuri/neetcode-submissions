from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)

        for prereq in prerequisites:
            adjList[prereq[0]].append(prereq[1])
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if adjList[course] == []:
                return True

            visited.add(course)
            
            for prereq in adjList[course]:
                if not dfs(prereq): return False
            
            visited.remove(course)
            adjList[course] = []
            return True

        for course in prerequisites:
            if not dfs(course[0]): return False
        return True
            