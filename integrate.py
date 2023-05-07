import numpy as np
import pandas as pd
import gtsam

def load_data(filename):
    data = pd.read_csv(filename, header=None, names=["Timestamp", "east", "north"])
    return data

wifi_data = load_data("wifi_data.csv")
vps_data = load_data("vps_data.csv")
gnss_data = load_data("gnss_data.csv")

# Calculate standard deviations for each dataset
wifi_std_dev_east = np.std(wifi_data["east"])
wifi_std_dev_north = np.std(wifi_data["north"])

vps_std_dev_east = np.std(vps_data["east"])
vps_std_dev_north = np.std(vps_data["north"])

gnss_std_dev_east = np.std(gnss_data["east"])
gnss_std_dev_north = np.std(gnss_data["north"])

# Define Wi-Fi noise model function based on timestamp
def wifi_noise_model(timestamp):
    if timestamp <= 40:
        return gtsam.noiseModel.Diagonal.Sigmas(np.array([wifi_std_dev_east / 10, wifi_std_dev_north / 10, 1.0]))
    else:
        return gtsam.noiseModel.Diagonal.Sigmas(np.array([wifi_std_dev_east, wifi_std_dev_north, 1.0]))

# Create factor graph
graph = gtsam.NonlinearFactorGraph()

# Add Wi-Fi factors to the graph
for index, row in wifi_data.iterrows():
    graph.add(gtsam.PriorFactorPose2(int(row["Timestamp"]), gtsam.Pose2(row["east"], row["north"], 0), wifi_noise_model(row["Timestamp"])))

# Add VPS factors to the graph
for index, row in vps_data.iterrows():
    graph.add(gtsam.PriorFactorPose2(int(row["Timestamp"]), gtsam.Pose2(row["east"], row["north"], 0), gtsam.noiseModel.Diagonal.Sigmas(np.array([vps_std_dev_east, vps_std_dev_north, 1.0]))))

# Add GNSS factors to the graph
for index, row in gnss_data.iterrows():
    graph.add(gtsam.PriorFactorPose2(int(row["Timestamp"]), gtsam.Pose2(row["east"], row["north"], 0), gtsam.noiseModel.Diagonal.Sigmas(np.array([gnss_std_dev_east, gnss_std_dev_north, 1.0]))))

# Create initial estimates using Wi-Fi data
initial_estimates = gtsam.Values()
for index, row in wifi_data.iterrows():
    initial_estimates.insert(int(row["Timestamp"]), gtsam.Pose2(row["east"], row["north"], 0))

# Optimize the graph
optimizer = gtsam.LevenbergMarquardtOptimizer(graph, initial_estimates)
result = optimizer.optimize()

# Extract optimized poses and save to a CSV file
optimized_coords = []
for key in result.keys():
    pose = result.atPose2(key)
    optimized_coords.append({
        "Timestamp": key,
        "east": pose.x(),
        "north": pose.y()
    })

optimized_data = pd.DataFrame(optimized_coords)
optimized_data.to_csv("optimized_data.csv", index=False)
