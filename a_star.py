import heapq

def a_star(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    came_from = {}
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0
    
    f_cost = {node: float('inf') for node in graph}
    f_cost[start] = heuristic[start]
    
    while open_list:
        current = heapq.heappop(open_list)[1]
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, g_cost[goal]
        
        for neighbor, cost in graph[current]:
            temp_g = g_cost[current] + cost
            
            if temp_g < g_cost[neighbor]:
                came_from[neighbor] = current
                g_cost[neighbor] = temp_g
                f_cost[neighbor] = temp_g + heuristic[neighbor]
                heapq.heappush(open_list, (f_cost[neighbor], neighbor))
    
    return None

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 2)],
    'D': [('G', 3)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 2,
    'G': 0
}

path, cost = a_star(graph, 'A', 'G', heuristic)

print("Shortest Path:", path)
print("Total Cost:", cost)