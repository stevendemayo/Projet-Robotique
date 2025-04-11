import numpy as np
from PIL import Image
import argparse
import os

def convert_pgm_to_npy(pgm_path, output_path=None, threshold=128):
    # Charger l'image PGM en niveaux de gris
    img = Image.open(pgm_path).convert("L")
    map_array = np.array(img)

    # Afficher des infos utiles
    print(f"[INFO] Carte chargée : {pgm_path}")
    print(f"[INFO] Dimensions : {map_array.shape}")
    print(f"[INFO] Exemple de valeurs : min={map_array.min()}, max={map_array.max()}")

    # Binarisation (0 = libre, 1 = obstacle)
    binary_map = np.where(map_array < threshold, 1, 0)

    # Déduire le nom de fichier de sortie si non fourni
    if output_path is None:
        output_path = os.path.splitext(pgm_path)[0] + ".npy"

    # Sauvegarder au format .npy
    np.save(output_path, binary_map)
    print(f"[✅] Carte sauvegardée en format .npy : {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convertir une carte PGM en matrice binaire NumPy")
    parser.add_argument("pgm_path", help="Chemin du fichier .pgm (généré par map_saver)")
    parser.add_argument("-o", "--output", help="Chemin du fichier .npy de sortie")
    parser.add_argument("-t", "--threshold", type=int, default=128, help="Seuil de binarisation (par défaut : 128)")
    args = parser.parse_args()

    convert_pgm_to_npy(args.pgm_path, args.output, args.threshold)
