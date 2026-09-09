from collections import deque

graph = {
    "A" : ["B", "C"],
    "B" : ["A", "C", "I"],
    "C" : ["A", "B", "D"],
    "D" : ["C", "E"],
    "E" : ["D", "F"],
    "F" : ["E", "H"],
    "G" : ["H"],
    "H" : ["F", "G", "I"],
    "I" : ["B", "H"]
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

hasil = bfs(graph, "A", "F")

print("Rute yang ditemukan: ")
print("->".join(hasil))