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

def dfs(graph, start, goal):
    stack = [[start]]   # pakai stack, bukan queue
    visited = []

    while stack:
        path = stack.pop()   # ambil dari belakang (LIFO)
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.append(node)

            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)

    return None

hasil = dfs(graph, "Twin Peaks", "Golden Gate Bridge")

print("rute yang ditemukan (DFS): ")
print("->".join(hasil))