class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        inDegree = [0] * numCourses
        adjList = [[] for i in range(numCourses)]

        for src, dst in prerequisites:
            inDegree[dst] += 1
            adjList[src].append(dst)
        
        queue = deque()
        result = []
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
        finished = 0
        while queue:
            src = queue.popleft()
            result.append(src)
            finished += 1
            for nei in adjList[src]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    queue.append(nei)
        return result[::-1] if finished == numCourses else []