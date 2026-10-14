class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = { src: [] for src, dst in trust}

        for src, dst in trust:
            adj[src].append(dst)
        townJudge = -1
        for i in range(1,n+1):
            if i not in adj:
                townJudge = i
                break
        print(adj)
        for src, childs in adj.items():
            if townJudge not in childs:
                return -1
        return townJudge