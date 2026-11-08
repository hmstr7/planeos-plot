# Plane OS flight log visualizer
This python script visualizes the data from gyro and input logs for analysis and comparison using `matplotlib`.

## Installation
Clone this repository: 
```sh
git clone https://github.com/hmstr7/planeos-plot.git
cd planeos-plot
```
Create a virtual environment and install the requirements: 
```sh
uv venv
source .venv/bin/activate
uv sync
```

## Running
Usage:
```sh
uv run src/planeos_plot/plot-data.py <path to -imu.csv log file> <path to -input.csv log file>
```

Example:
```sh
uv run src/planeos_plot/plot-data.py data/examples/example-flightlog-imu.csv data/examples/example-flightlog-input.csv
```
