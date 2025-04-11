import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import yaml
import os
import argparse

def afficher_map_ros(pgm_path):
    # Charger l'image PGM
    img = Image.open(pgm_path).convert('L')
    map_array = np.array(img)

    # Lire le fichier YAML associé
    yaml_path = os.path.splitext(pgm_path)[0] + ".yaml"
    if os.path.exists(yaml_path):
        with open(yaml_path, 'r') as file:
            map_metadata = yaml.safe_load(file)
            resolution = map_metadata.get('resolution', 1.0)
            origin = map_metadata.get('origin', [0, 0, 0])
    else:
        resolution = 1.0
        origin = [0, 0, 0]
        print(f"[⚠️] Aucun fichier .yaml trouvé, valeurs par défaut utilisées.")

    print(f"✅ Carte chargée : {pgm_path}")
    print(f"🧭 Résolution : {resolution} m/pixel")
    print(f"📍 Origine : {origin}")

    # Dimensions physiques
    height, width = map_array.shape
    extent = [
        origin[0],
        origin[0] + width * resolution,
        origin[1],
        origin[1] + height * resolution,
    ]

    # Affichage
    plt.figure(figsize=(10, 8))
    plt.imshow(map_array, cmap='gray_r', origin='lower', extent=extent)
    plt.title(f"Carte SLAM : {os.path.basename(pgm_path)}")
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.grid(True)
    plt.show()

# --- Point d'entrée principal ---
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Afficher une carte SLAM ROS (format .pgm + .yaml)")
    parser.add_argument("pgm_file", help="Chemin du fichier .pgm à afficher")
    args = parser.parse_args()

    if not os.path.isfile(args.pgm_file):
        print(f"❌ Fichier non trouvé : {args.pgm_file}")
        exit(1)

    afficher_map_ros(args.pgm_file)
