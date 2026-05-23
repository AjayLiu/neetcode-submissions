class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(reverse = True)
        endTime = []
        for i in range(len(position)):
            p, s = cars[i]
            time = (target - p) / s
            # print(p, s, time)
            if not endTime or endTime[-1] < time:
                endTime.append(time)
            # print(endTime)
        return len(endTime)
