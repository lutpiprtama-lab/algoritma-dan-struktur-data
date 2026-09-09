
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

def dfs(graph, start, goal):
    stack = [[start]]   
    visited = []

    while stack:
        path = stack.pop()   
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

hasil = dfs(graph, "A", "F")

print("rute yang ditemukan (DFS): ")
print("->".join(hasil))