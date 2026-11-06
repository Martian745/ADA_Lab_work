
INF = float('inf')


def floyd_warshall(graph: list[list[int]]) -> list[list[int]]:
    n = len(graph)

    if any(len(row) != n for row in graph):
        raise ValueError("Graph must be a square matrix.")

    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(
                        dist[i][j],
                        dist[i][k] + dist[k][j]
                    )

    # Detect negative-weight cycles
    if any(dist[i][i] < 0 for i in range(n)):
        raise ValueError("Negative-weight cycle detected!")

    return dist


def optimal_bst(keys: list[int], freq: list[int]) -> int:
    n = len(keys)

    if n != len(freq):
        raise ValueError("Keys and frequencies must have equal length.")

    if any(freq[i] < 0 for i in range(n)):
        raise ValueError("Frequencies cannot be negative.")

    if any(keys[i] >= keys[i + 1] for i in range(n - 1)):
        raise ValueError("Keys must be in strictly increasing order.")

    if n == 0:
        return 0

    # Prefix sums for efficient frequency calculation
    prefix = [0] * (n + 1)

    for i in range(n):
        prefix[i + 1] = prefix[i] + freq[i]

    # DP table: dp[i][j] = minimum cost for keys i to j
    dp = [[0] * n for _ in range(n)]

    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            total_freq = prefix[j + 1] - prefix[i]
            dp[i][j] = INF

            for root in range(i, j + 1):
                left = dp[i][root - 1] if root > i else 0
                right = dp[root + 1][j] if root < j else 0

                cost = left + right + total_freq
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]


def main():
    try:
        print("=== Floyd-Warshall Algorithm ===")

        n = int(input("Enter number of vertices: "))
        if n < 0:
            raise ValueError("Number of vertices cannot be negative.")

        print("Enter adjacency matrix (-1 for no edge):")
        graph = []

        for _ in range(n):
            row = list(map(int, input().split()))

            if len(row) != n:
                raise ValueError("Each row must contain exactly n values.")

            graph.append([
                INF if value == -1 else value
                for value in row
            ])

        # Set diagonal to zero
        for i in range(n):
            graph[i][i] = 0

        result = floyd_warshall(graph)

        print("\nAll-Pairs Shortest Distance Matrix:")
        for row in result:
            print([
                "INF" if value == INF else value
                for value in row
            ])

        print("\n=== Optimal Binary Search Tree ===")

        m = int(input("Enter number of keys: "))
        if m < 0:
            raise ValueError("Number of keys cannot be negative.")

        keys = list(map(int, input("Enter sorted keys: ").split()))
        freq = list(map(int, input("Enter frequencies: ").split()))

        if len(keys) != m or len(freq) != m:
            raise ValueError("Enter exactly m keys and frequencies.")

        print("Minimum Optimal BST Search Cost:",
              optimal_bst(keys, freq))

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
