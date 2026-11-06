
def solveNQueens(n: int) -> list[list[str]]:
    if n <= 0:
        raise ValueError("Board size must be positive.")

    results = []
    board = [["."] * n for _ in range(n)]

    def backtrack(row, columns, diagonal1, diagonal2):
        if row == n:
            results.append(["".join(r) for r in board])
            return

        # Find columns that are currently safe
        available = (
            ((1 << n) - 1)
            & ~(columns | diagonal1 | diagonal2)
        )

        while available:
            # Extract the rightmost available position
            position = available & -available
            available -= position

            col = position.bit_length() - 1
            board[row][col] = "Q"

            backtrack(
                row + 1,
                columns | position,
                (diagonal1 | position) << 1,
                (diagonal2 | position) >> 1
            )

            # Backtrack: remove the queen
            board[row][col] = "."

    backtrack(0, 0, 0, 0)

    return results


def main():
    try:
        n = int(input("Enter board size (N): "))

        solutions = solveNQueens(n)

        print("\nTotal Solutions:", len(solutions))

        for index, solution in enumerate(solutions, 1):
            print(f"\nSolution {index}:")
            for row in solution:
                print(row)

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
