import platform
from typing import cast

from matplotlib.axes import Axes
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import numpy.typing as npt

import sys


args = sys.argv

def main():
    global args
    try:
        args = args[1:]
        if len(args) < 2:
            raise ValueError("Files to read not specified")
        imu_file = pd.read_csv(args[0])
        input_file = pd.read_csv(args[1])
    except (ValueError, FileNotFoundError) as e:
        print("Failed to parse arguments: ", e)
        sys.exit(-1)
    
    try:
        t_imu = imu_file["t"].to_numpy()
        x_imu = imu_file["x"].to_numpy()
        y_imu = imu_file["y"].to_numpy()
        z_imu = imu_file["z"].to_numpy()

        t_in = input_file["t"].to_numpy()
        ele = input_file["ele"].to_numpy()
        ail = input_file["ail"].to_numpy()
        thr = input_file["thr"].to_numpy()
    except Exception as e:
        print("Files are invalid: ", e)
        sys.exit(-1)
    
    fig, sbplt = plt.subplots(3,2)
    
    fig.suptitle("IMU gyro data")
    sbplt[0,0].plot(t_imu, x_imu, "tab:blue")
    sbplt[0,0].set(xlabel="t [s]", ylabel="x [deg/s]")

    sbplt[1,0].plot(t_imu, y_imu,"tab:blue")
    sbplt[1,0].set(xlabel="t [s]", ylabel="y [deg/s]")

    sbplt[2,0].plot(t_imu, z_imu, "tab:blue") 
    sbplt[2,0].set(xlabel="t [s]", ylabel="z [deg/s]")


    sbplt[0,1].plot(t_in, ail, "tab:orange")
    sbplt[0,1].set(xlabel="t [s]", ylabel="aileron_pw [us]")
    sbplt[0,1].sharex(sbplt[0,0])

    sbplt[1,1].plot(t_in, ele,"tab:orange")
    sbplt[1,1].set(xlabel="t [s]", ylabel="elevator_pw [us]")
    sbplt[1,1].sharex(sbplt[1,0])

    sbplt[2,1].plot(t_in, thr, "tab:green")
    sbplt[2,1].set(xlabel="t [s]", ylabel="thrust_pw [us]")

    plt.show()

if __name__ == "__main__":
    main()