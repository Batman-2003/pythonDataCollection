# Written by Gaurav Khaire on Last Weekend of June-24
# Aim is to Experiment with Magnetometer and IMU Calibration

# TODO: 1. Putting the Raw->Useful Values in csv file.
# TODO: 2. Plotting the 3 Circles in R, G, B ( Scatter Plots)
# TODO: 3. Calibrate for Hard Iron Losses.
# TODO: 4. Implement Sensor Fusion for Mag + Gyro
# TODO: 5. Make if Pretty

import numpy as np 
import matplotlib.pyplot as plt
import serial
import csv

# Global Variables Sit Here
PORT = "COM4"
BAUDERATE = 115200
LLIMIT = -3
ULIMIT =  3
X = np.arange(-3, 3+0.1, 0.1)
Y = np.arange(-3, 3+0.1, 0.1)
Z = np.arange(-3, 3+0.1, 0.1)
points = np.zeros((1, np.size(X), 3), np.float64)


def main():
  print("\n")
  print("Starting the IMU-Calibration CLI Program")
  print("Written by Gaurav Khaire in Last Weekend of June-2024 (or so he says)")
  print("")
  print("------------------------------------------------------------")
  print("")
  print("Printing out the Constant Parameters inside the script: ")
  print("\t PORT      = " + str(PORT)     )
  print("\t BAUDERATE = " + str(BAUDERATE))

  print("The Points are as follows: ")
  print(points)

  fig = plt.figure(figsize=(8, 6))
  ax = plt.axes(projection='3d')
  ax.scatter3D(points)
  plt.show()

# --------------------------------------------------------------
main()