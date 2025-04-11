# 🤖 Projet ROS – SLAM, Navigation & Planification intelligente

Bienvenue dans un projet ROS d’exception combinant **SLAM**, **planification de trajectoire**, **navigation autonome**, **simulation Gazebo** et **visualisation avancée**.  
Conçu avec passion et précision, ce dépôt est une véritable plateforme d’expérimentation et d’apprentissage autour de ROS et de la robotique mobile.

---

## 🗂️ Arborescence du projet

```
ProjetROS/
├── map/             # Fichiers de carte (SLAM, .npy, .pgm, .yaml)
├── scripts/         # Scripts Python & Shell (SLAM, navigation, planif)
├── workspace/       # Catkin workspace structuré
└── README.md       
```

---

## 🚀 Fonctionnalités principales

### 🧠 SLAM – `slam.sh`

- Lancement automatique de :
  - `roscore`
  - Gazebo + TurtleBot3
  - SLAM avec `gmapping`
  - RViz + téléop clavier
- Sauvegarde automatique de la carte via `map_saver`
- Fichiers générés : `.pgm`, `.yaml`, `.npy`

```bash
./scripts/slam.sh
```

---

### 🔄 Conversion de carte – `convert.py`

- Convertit une carte `.pgm` en matrice binaire `.npy` utilisable par les algorithmes de planification

```bash
python3 scripts/convert.py map/map_gmapping.pgm -o map/map_gmapping.npy
```

---

### 🧭 Navigation intelligente – `navigation.py`

- Implémente **A\***, **Dijkstra** et **Greedy**
- Analyse des performances (temps, nœuds explorés)
- Affichage graphique + tableau de comparaison (`pandas`)

```bash
python3 scripts/navigation.py map/map_gmapping.npy --start 2 2 --goal 47 27
```

---

### 🧠 Planification de mouvement réaliste – `motion_planning.py`

- Simule un déplacement **cinématique orienté** (version simplifiée de Hybrid A\*)
- Prend en compte l’orientation du robot
- Visualisation complète

```bash
python3 scripts/motion_planning.py
```

---

### 🧩 Planification 2D classique – `path_planning.py`

- Implémente un **A\*** avec diagonales sur une carte SLAM
- Vérifie les positions valides et trace le chemin optimal

```bash
python3 scripts/path_planning.py
```

---

### 📊 Visualisation pédagogique – `voisin.py`

- Compare les coûts de déplacement pour **Dijkstra, A\*** et **Greedy**
- Affichage clair, centré sur la logique de voisinage et de coût

```bash
python3 scripts/voisin.py
```

---

### 🚦 Lancement complet de la navigation – `motion_planning.sh`

- Démarre :
  - Gazebo
  - Navigation stack avec DWA
- Te laisse placer une pose initiale et un objectif dans RViz

```bash
./scripts/motion_planning.sh
```

---

### 🧬 Scénario global – `planification.sh`

- Lance simulation + ton propre serveur de planification (si intégré)
- Prévu pour une démo de planif maison sur TurtleBot3

```bash
./scripts/planification.sh
```

---

## 📦 Dépendances Python

Installe-les facilement via pip :

```text
numpy
pillow
matplotlib
pandas
```

```bash
pip install -r requirements.txt
```

> Modules standards inclus : `os`, `argparse`, `math`, `heapq`, `time`

---

## 🧩 Utilisation étape par étape

Voici comment exploiter ton projet de manière fluide et logique :

### 🔹 Étape 1 : Générer la carte SLAM

```bash
./scripts/slam.sh
```

- Lance `roscore`, Gazebo, le SLAM avec `gmapping`, RViz et la téléop.
- Explore manuellement la carte avec les flèches.
- Appuie sur une touche pour sauvegarder la carte (`.pgm` + `.yaml`).

---

### 🔹 Étape 2 : Convertir la carte `.pgm` en `.npy`

```bash
python3 scripts/convert.py map/map_gmapping.pgm -o map/map_gmapping.npy
```

- Permet de travailler plus facilement la carte avec NumPy.

---

### 🔹 Étape 3 : Visualiser la carte

```bash
python3 map/showmap.py
```

- Affiche la carte en utilisant `matplotlib`.

---

### 🔹 Étape 4 : Tester les algorithmes de planification

```bash
python3 scripts/navigation.py map/map_gmapping.npy --start 2 2 --goal 47 27
```

- Compare A*, Dijkstra et Greedy.
- Affiche les chemins + génère un tableau récapitulatif (`pandas`).

---

### 🔹 Étape 5 : Lancer le robot en navigation autonome

```bash
./scripts/motion_planning.sh
```

- Lance la simulation Gazebo + Navigation Stack (DWA).
- Utilise RViz :
  - Pose initiale : **2D Pose Estimate**
  - Objectif : **2D Nav Goal**

---

### 🔹 Étape 6 : Comprendre les voisins et coûts

```bash
python3 scripts/voisin.py
```

- Visualisation des coûts A*, Dijkstra, Greedy depuis une cellule centrale.
- Très utile pour l’analyse pédagogique.

---

### 🔹 Étape 7 : Planification simple sur grille

```bash
python3 scripts/path_planning.py
```

- Applique un A* classique 8 directions sur ta carte SLAM.

---

### 🔹 Étape 8 : Lancement global du scénario de planification

```bash
./scripts/planification.sh
```

- Démarre tout : simulation + ton propre serveur de planification si présent.

---
