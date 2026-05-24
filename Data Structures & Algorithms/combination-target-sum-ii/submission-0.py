class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(soFar: List[int], idx: int, remainder: int):
            if remainder == 0:
                ans.append(soFar)
                return
                
            if remainder < 0 or idx >= len(candidates):
                return
            
            
            c = candidates[idx]
            dfs(soFar + [c], idx + 1, remainder - c)

            new_idx = idx + 1
            while new_idx < len(candidates) and candidates[new_idx] == c:
                new_idx += 1
            dfs(soFar, new_idx, remainder)

        candidates.sort()
        dfs([], 0, target)
        return ans