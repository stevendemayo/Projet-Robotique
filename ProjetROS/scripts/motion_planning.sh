#!/bin/bash

# === CONFIGURATION ===
export TURTLEBOT3_MODEL=burger
MAP_PATH="/home/ros/ProjetROS/map/map_gmapping.yaml"    # ← À adapter à ta carte
RVIZ_CONFIG="$HOME/.rviz2/default.rviz"    # ← Met ton chemin si tu veux une config perso
WAIT_TIME=5

echo "🚀 Lancement complet de la navigation avec DWA..."

# === Étape 1 : Lancer Gazebo ===
gnome-terminal --title="Gazebo" -- bash -c "
echo '[Gazebo] Lancement...';
roslaunch turtlebot3_gazebo turtlebot3_world.launch;
exec bash"

sleep $WAIT_TIME

# === Étape 2 : Lancer la navigation avec DWA ===
gnome-terminal --title="Navigation Stack (DWA)" -- bash -c "
echo '[Navigation] Lancement avec map : $MAP_PATH';
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$MAP_PATH;
exec bash"


# === Message final ===
echo ""
echo "✅ Tous les modules sont lancés !"
echo "📍 Dans RViz, définis une position initiale (2D Pose Estimate), puis un objectif (2D Nav Goal)"
echo "🚧 Le robot va se déplacer en respectant ses contraintes dynamiques avec le planner DWA"
