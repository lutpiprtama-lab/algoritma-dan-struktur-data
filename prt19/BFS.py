from collections import deque

graph = {
    "Twin Peaks": ["Bus #44", "Bus #33"],
    "Bus #44": ["Bus #28"],
    "Bus #33": ["Bus #5L", "Bus #38"],
    "Bus #5L": ["Bus #28"],
    "Bus #38": ["Bus #28"],
    "Bus #28": ["Golden Gate Bridge"],
    "Golden Gate Bridge": []
}

def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = []

    while queue:
        path = queue.popleft()
        node = path [-1]

        if node == goal:
            return path
        
        if node not in visited:
            visited.append(node)

            for neighbor in graph [node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None

hasil = bfs(graph, "Twin Peaks", "Golden Gate Bridge")

print("Rute yang ditemukan: ")
print("->".join(hasil))