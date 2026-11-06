
class Knapsack:
    def __init__(self, weights, values, capacity):
        if len(weights) != len(values):
            raise ValueError("Weights and values must have equal length.")

        if capacity < 0 or any(w <= 0 for w in weights):
            raise ValueError("Capacity must be non-negative and weights positive.")

        if any(v < 0 for v in values):
            raise ValueError("Values cannot be negative.")

        self.weights = weights
        self.values = values
        self.capacity = capacity
        self.n = len(weights)

    # 2D Dynamic Programming Approach
    def knapsack_2d(self):
        dp = [[0] * (self.capacity + 1)
              for _ in range(self.n + 1)]

        for i in range(1, self.n + 1):
            weight = self.weights[i - 1]
            value = self.values[i - 1]

            for w in range(self.capacity + 1):
                dp[i][w] = dp[i - 1][w]

                if weight <= w:
                    dp[i][w] = max(
                        dp[i][w],
                        value + dp[i - 1][w - weight]
                    )

        return dp[self.n][self.capacity]

    # Space-Optimized 1D Dynamic Programming Approach
    def knapsack_01(self):
        dp = [0] * (self.capacity + 1)

        for i in range(self.n):
            weight = self.weights[i]
            value = self.values[i]

            # Reverse iteration prevents selecting an item twice
            for w in range(self.capacity, weight - 1, -1):
                dp[w] = max(
                    dp[w],
                    value + dp[w - weight]
                )

        return dp[self.capacity]


def main():
    try:
        n = int(input("Enter number of items: "))

        if n < 0:
            print("Number of items cannot be negative.")
            return

        weights = list(map(int, input("Enter item weights: ").split()))
        values = list(map(int, input("Enter item values: ").split()))
        capacity = int(input("Enter knapsack capacity: "))

        if len(weights) != n or len(values) != n:
            print("Error: Enter exactly", n, "weights and values.")
            return

        problem = Knapsack(weights, values, capacity)

        result_2d = problem.knapsack_2d()
        result_1d = problem.knapsack_01()

        print("\nMaximum Value (2D DP):", result_2d)
        print("Maximum Value (1D DP):", result_1d)

    except ValueError as error:
        print("Input Error:", error)


if __name__ == "__main__":
    main()
