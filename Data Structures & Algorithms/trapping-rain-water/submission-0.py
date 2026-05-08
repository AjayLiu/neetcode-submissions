class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0]
        for h in height:
            prefix.append(max(prefix[-1], h))
        del prefix[0]

        suffix = [0]
        for h in reversed(height):
            suffix.append(max(suffix[-1], h))
        del suffix[0]
        suffix.reverse()

        total = 0
        for i, h in enumerate(height):
            water = max(0, min(prefix[i], suffix[i]) - h)
            # print (water)
            total += water

        return total
