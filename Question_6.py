
import heapq


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        if not (0 <= u < self.vertices and 0 <= v < self.vertices):
            raise ValueError("Invalid vertex!")
        if u == v:
            raise ValueError("Self-loops are not allowed.")

        self.edges.append((weight, u, v))
        self.adj[u].append((weight, v))
        self.adj[v].append((weight, u))

    # Disjoint Set Union for Kruskal's Algorithm
    def find(self, parent, vertex):
        if parent[vertex] != vertex:
            parent[vertex] = self.find(parent, parent[vertex])
        return parent[vertex]

    def union(self, parent, rank, u, v):
        root_u = self.find(parent, u)
        root_v = self.find(parent, v)

        if root_u == root_v:
            return False

        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        elif rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

        return True

    # Kruskal's Minimum Spanning Tree
    def kruskal_mst(self):
        parent = list(range(self.vertices))
        rank = [0] * self.vertices
        mst = []

        for weight, u, v in sorted(self.edges):
            if self.union(parent, rank, u, v):
                mst.append((u, v, weight))

                if len(mst) == self.vertices - 1:
                    break

        if len(mst) != self.vertices - 1:
            raise ValueError("Graph is disconnected; MST does not exist.")

        return mst

    # Prim's Minimum Spanning Tree
    def prim_mst(self):
        if self.vertices == 0:
            return []

        visited = [False] * self.vertices
        min_heap = [(0, 0, -1)]
        mst = []

        while min_heap and len(mst) < self.vertices - 1:
            weight, vertex, parent = heapq.heappop(min_heap)

            if visited[vertex]:
                continue

            visited[vertex] = True

            if parent != -1:
                mst.append((parent, vertex, weight))

            for edge_weight, neighbor in self.adj[vertex]:
                if not visited[neighbor]:
                    heapq.heappush(
                        min_heap, (edge_weight, neighbor, vertex)
                    )

        if len(mst) != self.vertices - 1:
            raise ValueError("Graph is disconnected; MST does not exist.")

        return mst


def display_mst(name, mst):
    print(f"\n{name} Minimum Spanning Tree:")
    total_weight = 0

    for u, v, weight in mst:
        print(f"{u} -- {v} : {weight}")
        total_weight += weight

    print("Total MST Weight:", total_weight)


def main():
    vertices = int(input("Enter number of vertices: "))
    edges = int(input("Enter number of edges: "))

    graph = Graph(vertices)

    print("Enter edges (source destination weight):")
    for _ in range(edges):
        u, v, weight = map(int, input().split())
        graph.add_edge(u, v, weight)

    try:
        kruskal_result = graph.kruskal_mst()
        prim_result = graph.prim_mst()

        display_mst("Kruskal's Algorithm", kruskal_result)
        display_mst("Prim's Algorithm", prim_result)

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
