import numpy as np
import matplotlib.pyplot as plt
import heapq
import time
import pandas as pd

# --- Heuristique ---
def heuristic(a, b, type="euclidean"):
    a = np.array(a)
    b = np.array(b)
    if type == "manhattan":
        return np.sum(np.abs(a - b))
    return np.linalg.norm(a - b)

# --- Voisins valides ---
def get_neighbors(pos, grid):
    x, y = pos
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < grid.shape[1] and 0 <= ny < grid.shape[0] and grid[ny, nx] == 0:
            neighbors.append((nx, ny))
    return neighbors

# --- Algorithmes de recherche : A*, Dijkstra, Greedy ---
def search(start, goal, grid, method="astar"):
    frontier = []
    visited = set()
    heapq.heappush(frontier, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        _, current = heapq.heappop(frontier)
        visited.add(current)

        if current == goal:
            break

        for neighbor in get_neighbors(current, grid):
            new_cost = cost_so_far[current] + 1  # all moves cost 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                if method == "dijkstra":
                    priority = new_cost
                elif method == "greedy":
                    priority = heuristic(goal, neighbor)
                else:  # astar
                    priority = new_cost + heuristic(goal, neighbor)
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current

    path = []
    current = goal
    while current != start and current in came_from:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path, visited

# --- Enrichissement : collecte des métriques ---
def search_with_metrics(start, goal, grid, method="astar"):
    start_time = time.time()
    path, visited = search(start, goal, grid, method)
    duration = time.time() - start_time
    return {
        "method": method,
        "path": path,
        "visited": visited,
        "duration": duration,
        "path_length": len(path),
        "explored_nodes": len(visited)
    }

# --- Carte / Obstacles ---
width, height = 50, 30
grid = np.zeros((height, width))
grid[10:13, 5:25] = 1
grid[5:20, 30:33] = 1
grid[20:23, 10:35] = 1
grid[5:8, 40:47] = 1
grid[15:27, 45:48] = 1

start = (2, 2)
goal = (47, 27)

# --- Exécution des 3 algos avec analyse ---
results = [
    search_with_metrics(start, goal, grid, "astar"),
    search_with_metrics(start, goal, grid, "dijkstra"),
    search_with_metrics(start, goal, grid, "greedy")
]

# --- Affichage graphique ---
paths = [r["path"] for r in results]
visiteds = [r["visited"] for r in results]
methods = ["A*", "Dijkstra", "Greedy"]

fig, axes = plt.subplots(1, 3, figsize=(20, 8))
for ax, method, path, visited in zip(axes, methods, paths, visiteds):
    ax.imshow(grid, cmap="gray_r", origin="lower")
    if visited:
        vx, vy = zip(*visited)
        ax.plot(vx, vy, "y.", markersize=1, linestyle='', label="Exploré")
    if path:
        px, py = zip(*path)
        ax.plot(px, py, "b-", label="Chemin")
        ax.plot(start[0], start[1], "go", label="Départ")
        ax.plot(goal[0], goal[1], "ro", label="Objectif")
    ax.set_title(f"{method}")
    ax.legend()
    ax.grid(True)

plt.tight_layout()
plt.show()

# --- Tableau de comparaison ---
df = pd.DataFrame([{
    "Algorithme": r["method"].capitalize(),
    "Temps de calcul (s)": round(r["duration"], 4),
    "Longueur du chemin": r["path_length"],
    "Nœuds explorés": r["explored_nodes"]
} for r in results])

print(df)
