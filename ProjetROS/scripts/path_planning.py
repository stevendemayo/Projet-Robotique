import numpy as np
import matplotlib.pyplot as plt
import heapq

# -------- Chargement de la carte SLAM --------
# Remplacer par le chemin vers votre carte (fichier .npy par exemple)
grid = np.load("../map/map_gmapping.npy")  # Ex: carte binaire 2D issue du SLAM

height, width = grid.shape

# -------- Définition des positions --------
start = (10, 10)
goal = (40, 30)

# -------- Vérification des positions valides --------
def is_valid(pos):
    x, y = pos
    return 0 <= x < width and 0 <= y < height and grid[y, x] == 0

if not is_valid(start):
    raise ValueError("Le point de départ est dans un obstacle ou hors de la grille.")
if not is_valid(goal):
    raise ValueError("Le point d’arrivée est dans un obstacle ou hors de la grille.")

# -------- A* classique --------
def heuristic(a, b):
    return np.linalg.norm(np.array(a) - np.array(b))

def get_neighbors(pos):
    x, y = pos
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1),
             (-1, -1), (1, 1), (1, -1), (-1, 1)]
    neighbors = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height and grid[ny, nx] == 0:
            neighbors.append((nx, ny))
    return neighbors

def a_star(start, goal):
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {}
    cost_so_far = {start: 0}

    while frontier:
        _, current = heapq.heappop(frontier)

        if current == goal:
            break

        for neighbor in get_neighbors(current):
            new_cost = cost_so_far[current] + heuristic(current, neighbor)
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(goal, neighbor)
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current

    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from.get(current)
        if current is None:
            print("Aucun chemin trouvé entre le départ et l’arrivée.")
            return []
    path.append(start)
    return path[::-1]

# -------- Exécution --------
path = a_star(start, goal)

# -------- Affichage --------
grid_display = np.copy(grid)

if path:
    for x, y in path:
        grid_display[y, x] = 0.5  # tracer le chemin

plt.imshow(grid_display, cmap="gray_r", origin="lower")
plt.plot(start[0], start[1], "go", label="Départ")
plt.plot(goal[0], goal[1], "ro", label="Objectif")
if path:
    plt.plot(*zip(*path), "b-", label="Chemin A*")
plt.legend()
plt.title("Path Planning (A* classique avec carte SLAM)")
plt.grid()
plt.show()
