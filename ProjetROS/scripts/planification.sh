#!/bin/bash

# === Étape 1 : Lancer Gazebo avec TurtleBot3 ===
gnome-terminal -- bash -c "source ~/catkin_ws/devel/setup.bash && roslaunch ros_world turtlebot3_world.launch; exec bash"

# Attente courte pour laisser le temps à Gazebo de démarrer
sleep 5

# === Étape 2 : Lancer RViz avec le nœud de planification ===
gnome-terminal -- bash -c "source ~/catkin_ws/devel/setup.bash && roslaunch global_path_planning turtlebot3_ros_world.launch; exec bash"

# Attente courte pour laisser le nœud s'initialiser
sleep 3

# === Étape 3 : Lancer le serveur de planification ===
gnome-terminal -- bash -c "source ~/catkin_ws/devel/setup.bash && rosrun global_path_planning path_planning_server.py; exec bash"