class CountSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        for (x, y) in self.ptsCount.keys():
            if (abs(x-px) != abs(y-py)) or x == px or y == py:
                continue
            count= self.ptsCount.get((x, y), 0)
            res += count * self.ptsCount.get((x, py), 0) * self.ptsCount.get((px, y), 0)
        return res
        
