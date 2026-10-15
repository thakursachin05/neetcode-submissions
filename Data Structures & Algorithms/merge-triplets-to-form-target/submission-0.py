class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid = []        
        for pair in triplets:
            a,b,c = pair
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            else:
                valid.append(pair)
        a1,b1,c1 = 0,0,0
        for v in valid:
            a1= max(a1, v[0])
            b1 = max(b1, v[1])
            c1 = max(c1, v[2])
        
        return [a1,b1,c1] == target

        