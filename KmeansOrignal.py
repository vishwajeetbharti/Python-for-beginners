import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

from matplotlib import pyplot as plt 


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

def plot_infertility(pcos, age, bmi, infertility, colors):
  plt.figure(figsize=(10, 6))  # Adjust figure size as needed

  # Scatter plot with transparency
  for i in range(len(pcos)):
    plt.scatter(age[i], bmi[i], alpha=0.7, c=colors[infertility[i]])

  # Labels and title
  plt.xlabel('BMI')
  plt.ylabel('Cycle_length')
  plt.title('Infertility by PCOS Status, BMI, and Cycle_length (Sample Data)')

  # Add legend for infertility categories (optional)
  if len(set(infertility)) > 1:
    plt.legend()

  plt.show()

# Color list based on infertility (modify as needed)
colors = {1: 'green', 0: 'red'}

# Call the plotting function
plot_infertility(empl.PCOS, empl.BMI, empl.Cycle_length, empl.Pregnant, colors)


# Selecting features for clustering
features = [row[1:] for row in data]

X = empl[['Age','BMI','Hb','Cycle_length',
          'Marriage_Status','no_of_abortion','FSH',
          'LH','TSH','AMH','Vit_D3',
          'PRG','RBS','BP_Systolic','Endometrium']].values

km = KMeans(n_clusters=3)
y_predict = km.fit_predict(X)
empl = empl.assign(cluster=y_predict)

###############Cluster vlaue Finding
# k_rng = range(1,10)
# sse = []
# for k in k_rng:
#     km  = KMeans(n_clusters=k)
#     km.fit([empl.PCOS,empl.Age,empl.BMI,empl.Pulse_rate,empl.Hb,empl.Cycle_length,empl.Marriage_Status,empl.Pregnant,empl.no_of_abortion,empl.FSH,empl.LH,empl.FSH_LH,empl.TSH,empl.AMH,empl.TSH,empl.Vit_D3,empl.PRG,empl.RBS,empl.BP_Systolic,empl.BP_Diastolic,empl.Endometrium])
#     sse.append(km.inertia_)

# print(sse)

# plt.xlabel('k')
# plt.ylabel('sum of squared')
# plt.plot(k_rng,sse)
# plt.show()

#################Example on New Data
new_data = [30, 23.0, 11.0, 5, 22, 0, 7.0, 2.5, 2.0, 1.8, 30.0, 1.0, 90, 90, 8.0]
first_data_point_cluster = km.predict([X[0]])
new_data_cluster = km.predict([new_data])
print(new_data_cluster)
is_firstalie = (new_data_cluster == first_data_point_cluster).all()
print("IsFirtalie:", is_firstalie)

################Accuracy
labels = km.labels_
silhouette_avg = (silhouette_score(X, labels)*100)-20
print("Accuracy Score:", silhouette_avg)

silhouette_scores = []
for n_clusters in range(2, 11):
    km = KMeans(n_clusters=n_clusters)
    labels = km.fit_predict(X)
    silhouette_avg = silhouette_score(X, labels)
    silhouette_scores.append(silhouette_avg)

# Plot silhouette scores against the number of clusters
plt.plot(range(2, 11), silhouette_scores, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Score vs Number of Clusters')
plt.xticks(np.arange(2, 11, step=1))
plt.grid(True)
plt.show()
