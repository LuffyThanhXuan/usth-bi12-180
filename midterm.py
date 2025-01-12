import heapq

def build_graph(file_path):
    graph = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split('\t')
            parts = [part.strip() for part in parts if part.strip()]
            
            if len(parts) != 3:
                continue
            
            try:
                origin, destination, distance = parts[0], parts[1], float(parts[2])
            except ValueError:
                continue

            if origin not in graph:
                graph[origin] = []
            if destination not in graph:
                graph[destination] = []

            graph[origin].append((destination, distance))
            graph[destination].append((origin, distance))

    return graph


def shortest_path(graph, src, dst):
    priority_queue = [(0, src, [])]
    visited = set()

    while priority_queue:
        current_distance, current_node, path = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        path = path + [current_node]
        visited.add(current_node)

        if current_node == dst:
            return current_distance, path

        for neighbor, distance in graph.get(current_node, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (current_distance + distance, neighbor, path))

    return float('inf'), []

def main():
    file_path = 'C:/Users/DO SINH HUNG/USTH/gt2025/Vietnam - Distance between Cities.txt'
    graph = build_graph(file_path)

    src = input("Enter the source city: ").strip()
    dst = input("Enter the destination city: ").strip()

    distance, path = shortest_path(graph, src, dst)

    if distance == float('inf'):
        print(f"No path found between {src} and {dst}.")
    else:
        print(f"The shortest path from {src} to {dst} is {distance} km.")
        print("Path: " + " -> ".join(path))

if __name__ == "__main__":
    main()
