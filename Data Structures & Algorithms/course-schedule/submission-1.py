class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0] * numCourses
        adjList = [[] for i in range(numCourses)]

        for src, dst in prerequisites:
            inDegree[dst] += 1
            adjList[src].append(dst)
        
        queue = deque()
        
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
        finished = 0
        while queue:
            src = queue.popleft()
            finished += 1
            for nei in adjList[src]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    queue.append(nei)
        return finished == numCourses
    
    
        