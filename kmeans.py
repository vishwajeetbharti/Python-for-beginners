



import numpy as np
import pandas as pd

empl = pd.read_csv('d:/vishwajeet/Python-for-beginner/Python-for-beginner/infertility_data_csv.csv')
empl.PCOS = empl.PCOS.fillna(empl.PCOS.median())
empl.Age = empl.Age.fillna(empl.Age.median())
empl.BMI = empl.BMI.fillna(empl.BMI.median())
empl.Pulse_rate = empl.Pulse_rate.fillna(empl.Pulse_rate.median())
empl.Hb = empl.Hb.fillna(empl.Hb.median())
empl.Cycle_length = empl.Cycle_length.fillna(empl.Cycle_length.median())
empl.Marriage_Status = empl.Marriage_Status.fillna(empl.Marriage_Status.median())
empl.Pregnant = empl.Pregnant.fillna(empl.Pregnant.median())
empl.no_of_abortion = empl.no_of_abortion.fillna(empl.no_of_abortion.median())
empl.FSH = empl.FSH.fillna(empl.FSH.median())
empl.LH = empl.LH.fillna(empl.LH.median())
empl.FSH_LH = empl.FSH_LH.fillna(empl.FSH_LH.median())
empl.TSH = empl.TSH.fillna(empl.TSH.median())
empl.AMH = empl.AMH.fillna(empl.AMH.median())
empl.Vit_D3 = empl.Vit_D3.fillna(empl.Vit_D3.median())
empl.PRG = empl.PRG.fillna(empl.PRG.median())
empl.RBS = empl.RBS.fillna(empl.RBS.median())
empl.BP_Systolic = empl.BP_Systolic.fillna(empl.BP_Systolic.median())
empl.BP_Diastolic = empl.BP_Diastolic.fillna(empl.BP_Diastolic.median())
empl.Endometrium = empl.Endometrium.fillna(empl.Endometrium.median())

data = []

# Iterate through the rows and print each one
data = empl.values.tolist()




# Selecting features for clustering
features = [row[1:] for row in data]


# Choosing the number of clusters (k)
k = 3 # You can choose the appropriate number of clusters based on your analysis

def k_means_clustering(data, k, max_iterations=100):
    # Initialize centroids randomly
    centroids = np.array(data)[:k]

    for _ in range(max_iterations):
        # Calculate distances from each point to each centroid
        distances = np.linalg.norm(np.array(data)[:, np.newaxis] - centroids, axis=2)

        # Assign each point to the cluster of the nearest centroid
        labels = np.argmin(distances, axis=1)

        # Update centroids based on the mean of points in each cluster
        new_centroids = np.array([np.mean(np.array(data)[labels == i], axis=0) for i in range(k)])

        # Check for convergence
        if np.all(centroids == new_centroids):
            break

        centroids = new_centroids

    return labels

# Applying k-means clustering
cluster_labels = k_means_clustering(features, k)

# Display the resulting cluster labels
# for i, label in enumerate(cluster_labels):
#     print(f"Data point {i+1}: Cluster {label+1}")

# Calculate the chance of infertility (assuming 'infertility' is in the last column)
infertility_chances = [row[-2] for i, row in enumerate(data) if cluster_labels[i] == 1]
print(infertility_chances)

average_infertility_chance = sum(infertility_chances) / len(infertility_chances) if infertility_chances else 0

print(f"\nAverage chance of infertility in Cluster : {average_infertility_chance}")