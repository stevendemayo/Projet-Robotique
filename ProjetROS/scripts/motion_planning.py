import numpy as np
import matplotlib.pyplot as plt
import heapq
import math

# -------- Chargement de la carte depuis un fichier .npy --------
grid = np.load("../map/map_gmapping.npy")
height, width = grid.shape

# -------- A* étendu avec orientation --------
def heuristic(a, b):
    return np.linalg.norm(np.array(a) - np.array(b))

def motion_model():
    motions = []
    for omega in [-0.5, 0.0, 0.5]:  # rad/s
        motions.append((1.0, omega))  # vitesse linéaire constante
    return motions

def hybrid_a_star(start, goal):
    sx, sy, stheta = start
    gx, gy = goal

    dt = 0.5  # pas de temps
    frontier = []
    heapq.heappush(frontier, (0, (sx, sy, stheta)))
    came_from = {}
    cost_so_far = {(round(sx, 1), round(sy, 1), round(stheta, 1)): 0}
    visited = []

    while frontier:
        _, current = heapq.heappop(frontier)
        x, y, theta = current
        visited.append((x, y))

        if heuristic((x, y), (gx, gy)) < 1.0:
            goal_state = current
            break

        for v, omega in motion_model():
            new_theta = theta + omega * dt
            new_x = x + v * math.cos(new_theta) * dt
            new_y = y + v * math.sin(new_theta) * dt

            ix, iy = int(round(new_x)), int(round(new_y))
            if not (0 <= ix < width and 0 <= iy < height):
                continue
            if grid[iy, ix] == 1:
                continue

            state_key = (round(new_x, 1), round(new_y, 1), round(new_theta, 1))
            prev_key = (round(x, 1), round(y, 1), round(theta, 1))
            new_cost = cost_so_far[prev_key] + dt

            if state_key not in cost_so_far or new_cost < cost_so_far[state_key]:
                cost_so_far[state_key] = new_cost
                priority = new_cost + heuristic((new_x, new_y), (gx, gy))
                heapq.heappush(frontier, (priority, (new_x, new_y, new_theta)))
                came_from[state_key] = prev_key

    # Reconstruction du chemin
    path = []
    current = (round(goal_state[0], 1), round(goal_state[1], 1), round(goal_state[2], 1))
    while current in came_from:
        path.append((current[0], current[1]))
        current = came_from[current]
    path.append((sx, sy))
    return path[::-1]

# -------- Exécution --------
start = (160, 180, 0)  # (x, y, θ)
goal = (200, 230)      # (x, y)

motion_path = hybrid_a_star(start, goal)

# -------- Affichage --------
plt.imshow(grid, cmap="gray_r", origin="lower")
if motion_path:
    plt.plot(*zip(*motion_path), "b-", label="Chemin Hybrid A*")
plt.plot(start[0], start[1], "go", label="Départ")
plt.plot(goal[0], goal[1], "ro", label="Objectif")
plt.legend()
plt.title("Motion Planning (A* avec orientation)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
