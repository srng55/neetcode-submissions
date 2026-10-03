class CountSquares:

    def __init__(self):
        self.points = [[0] * 1001 for _ in range(1001)]

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[x][y] += 1

    def count(self, point: List[int]) -> int:

        x, y = point
        result = 0

        for x2 in range(1001):

            if x2 == x:
                continue

            count = self.points[x2][y]

            if count == 0:
                continue

            side = abs(x2 - x)

            # Above
            if y + side <= 1000:
                result += (
                    count
                    * self.points[x][y + side]
                    * self.points[x2][y + side]
                )

            # Below
            if y - side >= 0:
                result += (
                    count
                    * self.points[x][y - side]
                    * self.points[x2][y - side]
                )

        return result