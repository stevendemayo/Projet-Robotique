#!/bin/bash

export TURTLEBOT3_MODEL=burger

MAP_DIR="/home/ros/ProjetROS/map"
MAP_NAME="map_gmapping"

mkdir -p "$MAP_DIR"

gnome-terminal \
  --tab --title="ROS Core" -e "bash -c 'roscore; exec bash'" \
  --tab --title="Gazebo World" -e "bash -c 'sleep 3; roslaunch turtlebot3_gazebo turtlebot3_world.launch; exec bash'" \
  --tab --title="SLAM Gmapping" -e "bash -c 'sleep 6; roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping; exec bash'" \
  --tab --title="RViz" -e "bash -c 'sleep 10; rosrun rviz rviz -d \$(rospack find turtlebot3_slam)/rviz/turtlebot3_slam.rviz; exec bash'" \
  --tab --title="Teleop" -e "bash -c 'sleep 12; roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch; exec bash'"

echo "[INFO] Tout est lancer"
read -p "Appuie sur une touche pour sauvegarder la carte..."

rosrun map_server map_saver -f "$MAP_DIR/$MAP_NAME"

echo "✅ Carte sauvegardée ici : $MAP_DIR/$MAP_NAME"

pkill -f roscore
pkill -f roslaunch
pkill -f rosrun
sleep 2 
