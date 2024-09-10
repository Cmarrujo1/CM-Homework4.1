from collections import deque

graph = {
    "OMA": ["SDF", "PWM", "SLC", "BZE"],
    "SDF": ["OMA", "PWM", "SLC", "BZE"],
    "PWM": ["OMA", "SDF", "SLC", "BZE"],
    "SLC": ["OMA", "SDF", "PWM", "BZE"],
    "BZE": ["OMA", "SDF", "PWM", "SLC"],
}

def bfs_shortest_path(graph, start, goal):
    if start not in graph or goal not in graph:
        return []

    if start == goal:
        return [start]


    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node in visited:
            continue

        for neighbor in graph[node]:
            new_path = path + [neighbor]
            queue.append(new_path)

            if neighbor == goal:
                return new_path

        visited.add(node)

    return []

def bfs_multi_stop(graph, start, stops):
    if not stops:
        return [start]

    full_path = []
    current = start

    for stop in stops:
        path = bfs_shortest_path(graph, current, stop)
        if not path:
            return []
        full_path.extend(path[:-1])
        current = stop

    full_path.append(stops[-1])
    return full_path

def find_routes():
    print("OMA to SDF:", bfs_shortest_path(graph, "OMA", "SDF"))
    print("OMA to SLC to PWM:", bfs_multi_stop(graph, "OMA", ["SLC", "PWM"]))  
    print("BZE to PWM:", bfs_shortest_path(graph, "BZE", "PWM"))

find_routes()
