class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        hp = [f for f in freq.values()]
        heapq.heapify_max(hp)

        q = []
        t = 0
        while hp or q:

            # Time skip
            if not hp:
                next_available, fr = q.pop()
                t = next_available
                hp.append(fr)
            else:
                while q:
                    next_available, fr = q[-1]
                    if t >= next_available:
                        q.pop()
                        heapq.heappush_max(hp, fr)
                    else:
                        break


            fr = heapq.heappop_max(hp)                
            if fr - 1 > 0:
                q.insert(0, (t + n + 1, fr - 1))
            t += 1

            # print("hp", hp)
            # print("q", q)
            # print("*******")
            # print("t", t)
        return t