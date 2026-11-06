
from functools import lru_cache


class TSPSolver:
    def solve_tsp(self, dist_matrix: list[list[int]]) -> int:
        n = len(dist_matrix)

        if n == 0:
            raise ValueError("Distance matrix cannot be empty.")

        if any(len(row) != n for row in dist_matrix):
            raise ValueError("Distance matrix must be square.")

        if any(dist_matrix[i][j] < 0
               for i in range(n) for j in range(n)):
            raise ValueError("Distances cannot be negative.")

        if n == 1:
            return 0

        INF = float('inf')
        ALL_VISITED = (1 << n) - 1

        @lru_cache(maxsize=None)
        def tsp(city, visited):
            # All cities visited: return to starting city
            if visited == ALL_VISITED:
                return dist_matrix[city][0]

            minimum_cost = INF

            for next_city in range(n):
                if not (visited & (1 << next_city)):
                    cost = (
                        dist_matrix[city][next_city]
                        + tsp(
                            next_city,
                            visited | (1 << next_city)
                        )
                    )

                    minimum_cost = min(minimum_cost, cost)

            return minimum_cost

        result = tsp(0, 1)

        if result == INF:
            raise ValueError("No complete tour exists.")

        return result


def main():
    try:
        n = int(input("Enter number of cities: "))

        if n <= 0:
            raise ValueError("Number of cities must be positive.")

        print("Enter distance matrix (use -1 for no direct route):")

        dist_matrix = []

        for _ in range(n):
            row = list(map(int, input().split()))

            if len(row) != n:
                raise ValueError("Each row must contain n values.")

            dist_matrix.append([
                float('inf') if value == -1 else value
                for value in row
            ])

        solver = TSPSolver()
        result = solver.solve_tsp(dist_matrix)

        print("\nMinimum Travelling Salesperson Tour Cost:", result)

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
