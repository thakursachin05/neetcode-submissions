class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()  # Sorting helps avoid equivalent combinations in different orders
        res = set()
        subset = []

        def dfs(i, currSum):
            if currSum == target:
                res.add(tuple(subset))
                return
            if i >= len(candidates) or currSum > target:
                return

            # Include candidates[i]
            subset.append(candidates[i])
            dfs(i + 1, currSum + candidates[i])
            subset.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            # Exclude candidates[i]
            dfs(i + 1, currSum)

        dfs(0, 0)
        return [list(item) for item in res]