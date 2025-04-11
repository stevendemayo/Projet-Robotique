import numpy as np
import matplotlib.pyplot as plt

# Création d'une grille plus grande pour montrer le cheminement avec coût
grid = np.zeros((7, 7))

start = (1, 1)
goal = (5, 5)

# Fonction d'affichage des voisins avec annotations de coût
def plot_with_costs(ax, title, moves, cost_fn):
    ax.imshow(grid, cmap="gray_r", origin="lower")
    ax.set_title(title)
    ax.plot(start[0], start[1], 'go', label="Départ")
    ax.plot(goal[0], goal[1], 'ro', label="Objectif")

    for dx, dy in moves:
        nx, ny = start[0] + dx, start[1] + dy
        if 0 <= nx < grid.shape[1] and 0 <= ny < grid.shape[0]:
            ax.plot(nx, ny, 's', color="lightblue")
            cost = cost_fn((nx, ny), start, goal)
            ax.text(nx, ny, f"{cost:.1f}", ha="center", va="center", fontsize=8, color="black")

    ax.grid(True)
    ax.set_xticks(range(grid.shape[1]))
    ax.set_yticks(range(grid.shape[0]))
    ax.legend()

# Fonctions de coût pour chaque algo
def cost_dijkstra(pos, start, goal):
    return np.linalg.norm(np.array(start) - np.array(pos))  # coût réel depuis start

def cost_astar(pos, start, goal):
    g = np.linalg.norm(np.array(start) - np.array(pos))  # coût réel
    h = np.linalg.norm(np.array(goal) - np.array(pos))   # heuristique
    return g + h

def cost_greedy(pos, start, goal):
    return np.linalg.norm(np.array(goal) - np.array(pos))  # heuristique uniquement

# Mouvements 8 directions
moves_8 = [(-1, 0), (1, 0), (0, -1), (0, 1),
           (-1, -1), (-1, 1), (1, -1), (1, 1)]

# Création des sous-figures
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

plot_with_costs(axes[0], "Dijkstra : coût réel depuis le départ", moves_8, cost_dijkstra)
plot_with_costs(axes[1], "A* : coût réel + heuristique", moves_8, cost_astar)
plot_with_costs(axes[2], "Greedy : heuristique uniquement", moves_8, cost_greedy)

plt.tight_layout()
plt.show()

