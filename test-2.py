import numpy as np
from scipy.stats import zscore
import matplotlib.pyplot as plt

# Example dataset
data = np.array([12, 15, 18, 22, 25, 30, 32, 35, 5000, 38, 40])

# Calculate z-scores for the dataset
z_scores = zscore(data)

# Set a threshold for identifying outliers
outlier_threshold = 3.0

# Identify outliers based on threshold
outliers_mask = np.abs(z_scores) > outlier_threshold

# Visualize the dataset with outliers highlighted
plt.scatter(np.arange(len(data)), data, c='b', label='Data')

# Remove outliers from the dataset
filtered_data = data[~outliers_mask]

print("Original dataset:", data)
print("Filtered dataset (without outliers):", filtered_data)