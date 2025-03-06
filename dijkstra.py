import heapq
import math


def dijkstra(s, adj_matrix):
    visited = [False] * len(adj_matrix)
    min_dist = [math.inf] * len(adj_matrix)
    heap = []
    min_dist[s] = 0
    heap.append((0, s))

    while heap:
        dist, node = heapq.heappop(heap)
        if dist != min_dist[node]:
            continue
        visited[node] = True
        for i, dist in enumerate(adj_matrix[node]):
            if dist == 0:
                continue
            else:
                if dist + min_dist[node] < min_dist[i]:
                    min_dist[i] = dist + min_dist[node]
                    heapq.heappush(heap, (min_dist[i], i))
    return min_dist


# adj_matrix = [[0, 1, 5], [1, 0, 1], [5, 1, 0]]
# print("hello world")
# print(dijkstra(0, adj_matrix))
