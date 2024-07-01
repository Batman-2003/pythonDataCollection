# Written by Gaurav Khaire on Last Weekend of June-24
# Aim is to Experiment with Magnetometer and IMU Calibration

# TODO: 1. Putting the Raw->Useful Values in csv file.
# TODO: 2. Plotting the 3 Circles in R, G, B ( Scatter Plots)
# TODO: 3. Calibrate for Hard Iron Losses.
# TODO: 4. Implement Sensor Fusion for Mag + Gyro
# TODO: 5. Make it Pretty

import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import serial
import csv

# Global Variables Sit Here
PORT = "COM4"
BAUDERATE = 115200
LLIMIT = -3
ULIMIT =  3+1
# X = np.arange(-3, 3+0.1, 0.1)
# Y = np.arange(-3, 3+0.1, 0.1)
# Z = np.arange(-3, 3+0.1, 0.1)

X = np.arange(LLIMIT, ULIMIT, 1)
Y = np.arange(LLIMIT, ULIMIT, 1)
Z = np.arange(LLIMIT, ULIMIT, 1)

sphere = []
x_sp = []
y_sp = []
z_sp = []


for x in X:
  for y in Y:
    for z in Z:
      if (np.square(x) + np.square(y) + np.square(z) <= 9):
        sphere.append([x, y, z])
        x_sp.append(x)
        y_sp.append(y)
        z_sp.append(z)

with open('test.csv', 'w', newline='') as csvfile:
  csvWr = csv.writer(csvfile)
  csvWr.writerow(["X-Axis", "Y-Axis", "Z-Axis"])
  for it, val in enumerate(X):
    csvWr.writerow([X[it], Y[it], Z[it]])






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
  # print(sphere)

  fig = plt.figure(figsize=(8, 8))
  plt.subplot(221)
  plt.title("X-Y")
  plt.scatter(x_sp, y_sp, color='red')

  plt.subplot(222)
  plt.title("Y-Z")
  plt.scatter(y_sp, z_sp, color='green')

  plt.subplot(223)
  plt.title("X-Z")
  plt.scatter(x_sp, z_sp, color='blue')

  plt.show()

# --------------------------------------------------------------
main()