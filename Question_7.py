
import heapq


class ShortestPath:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj = [[] for _ in range(vertices)]
        self.edges = []

    def add_edge(self, u, v, weight):
        if not (0 <= u < self.vertices and 0 <= v < self.vertices):
            raise ValueError("Invalid vertex!")

        self.adj[u].append((v, weight))
        self.edges.append((u, v, weight))

    # Dijkstra's Shortest Path Algorithm
    def dijkstra(self, src):
        if not 0 <= src < self.vertices:
            raise ValueError("Invalid source vertex!")

        if any(weight < 0 for _, _, weight in self.edges):
            raise ValueError("Dijkstra cannot process negative weights.")

        dist = [float('inf')] * self.vertices
        dist[src] = 0

        min_heap = [(0, src)]

        while min_heap:
            current_dist, u = heapq.heappop(min_heap)

            if current_dist > dist[u]:
                continue

            for v, weight in self.adj[u]:
                new_dist = current_dist + weight

                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(min_heap, (new_dist, v))

        return dist

    # Bellman-Ford Shortest Path Algorithm
    def bellman_ford(self, src):
        if not 0 <= src < self.vertices:
            raise ValueError("Invalid source vertex!")

        dist = [float('inf')] * self.vertices
        dist[src] = 0

        # Relax all edges V-1 times
        for _ in range(self.vertices - 1):
            updated = False

            for u, v, weight in self.edges:
                if dist[u] != float('inf'):
                    if dist[u] + weight < dist[v]:
                        dist[v] = dist[u] + weight
                        updated = True

            if not updated:
                break

        # Detect reachable negative-weight cycles
        for u, v, weight in self.edges:
            if dist[u] != float('inf'):
                if dist[u] + weight < dist[v]:
                    raise ValueError("Negative-weight cycle detected!")

        return dist


def display_distances(name, distances):
    print(f"\n{name} Shortest Distances:")

    for vertex, distance in enumerate(distances):
        if distance == float('inf'):
            print(f"Vertex {vertex}: INF")
        else:
            print(f"Vertex {vertex}: {distance}")


def main():
    vertices = int(input("Enter number of vertices: "))
    edges = int(input("Enter number of edges: "))

    graph = ShortestPath(vertices)

    print("Enter directed edges (source destination weight):")

    for _ in range(edges):
        u, v, weight = map(int, input().split())
        graph.add_edge(u, v, weight)

    src = int(input("Enter source vertex: "))

    try:
        dijkstra_result = graph.dijkstra(src)
        bellman_result = graph.bellman_ford(src)

        display_distances("Dijkstra's Algorithm", dijkstra_result)
        display_distances("Bellman-Ford Algorithm", bellman_result)

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
