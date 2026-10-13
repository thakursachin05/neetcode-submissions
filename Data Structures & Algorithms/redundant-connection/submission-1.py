class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        rank = [0] * (n+1)
        par = [i for i in range(n+1)]
        
        def find(u):
            if u == par[u]:
                return u
            par[u] = find(par[u])
            return par[u]

        def union(u,v):
            pu = find(u)
            pv = find(v)
            if pu == pv:
                return True

            if rank[pu] > rank[pv]:
                rank[pu] += rank[pv]
                par[pv] = pu
            else:
                rank[pv] += rank[pu]
                par[pu] = pv
            return False
        
        for u,v in edges:
            if union(u,v):
                return [u,v]
        print(par)
        return []


