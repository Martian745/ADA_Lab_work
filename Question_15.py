
class GraphBacktracker:
    def __init__(self, graph):
        self.graph = graph
        self.V = len(graph)

        if any(len(row) != self.V for row in graph):
            raise ValueError("Graph must be a square adjacency matrix.")

        if any(graph[i][i] != 0 for i in range(self.V)):
            raise ValueError("Self-loops are not allowed.")

        if any(graph[i][j] != graph[j][i]
               for i in range(self.V)
               for j in range(self.V)):
            raise ValueError("Graph must be undirected.")

    # Check whether a color can be assigned safely
    def is_safe_color(self, vertex, color, colors):
        for neighbor in range(self.V):
            if self.graph[vertex][neighbor] and colors[neighbor] == color:
                return False
        return True

    # Graph Coloring using Backtracking
    def graph_coloring(self, m):
        if m <= 0:
            raise ValueError("Number of colors must be positive.")

        colors = [0] * self.V

        def backtrack(vertex):
            if vertex == self.V:
                return True

            for color in range(1, m + 1):
                if self.is_safe_color(vertex, color, colors):
                    colors[vertex] = color

                    if backtrack(vertex + 1):
                        return True

                    colors[vertex] = 0

            return False

        if backtrack(0):
            return colors

        return []

    # Hamiltonian Cycle using Backtracking
    def hamiltonian_cycle(self):
        if self.V == 0:
            return []

        path = [0] + [-1] * (self.V - 1)

        def is_safe(vertex, position):
            if not self.graph[path[position - 1]][vertex]:
                return False

            if vertex in path[:position]:
                return False

            return True

        def backtrack(position):
            if position == self.V:
                return self.graph[path[position - 1]][path[0]] != 0

            for vertex in range(1, self.V):
                if is_safe(vertex, position):
                    path[position] = vertex

                    if backtrack(position + 1):
                        return True

                    path[position] = -1

            return False

        if backtrack(1):
            return path + [path[0]]

        return []


def main():
    try:
        n = int(input("Enter number of vertices: "))

        if n <= 0:
            raise ValueError("Number of vertices must be positive.")

        print("Enter adjacency matrix (0 or 1):")
        graph = []

        for _ in range(n):
            row = list(map(int, input().split()))

            if len(row) != n or any(x not in (0, 1) for x in row):
                raise ValueError("Enter a valid binary square matrix.")

            graph.append(row)

        solver = GraphBacktracker(graph)

        m = int(input("Enter number of colors: "))
        coloring = solver.graph_coloring(m)

        print("\nGraph Coloring:")
        if coloring:
            for vertex, color in enumerate(coloring):
                print(f"Vertex {vertex}: Color {color}")
        else:
            print("No valid coloring exists.")

        cycle = solver.hamiltonian_cycle()

        print("\nHamiltonian Cycle:")
        if cycle:
            print(" -> ".join(map(str, cycle)))
        else:
            print("No Hamiltonian cycle exists.")

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
