import heapq

def dijkstra(graph, source):
    # initialize distance with infinity
    distances = {vertex: float('infinity') for vertex in graph}
    distances[source] = 0

    #priority queue to hold vertices to explore
    priority_queue = [(0, source)]

    while priority_queue:
        #get the vertex with the smallest distance
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue
        #exploring neighbors
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances
# assigning values
graph = {0: {1: 4, 2: 1}, 1: {3: 1}, 2: {1: 2, 3: 5}, 3: {}}
source = 0

#printing result
print(dijkstra(graph, source))
