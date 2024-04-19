# Given data
age = [28, 36, 33]
bmi = [19.3, 24.9, 25.3]
hb = [10.48, 11.7, 11.8]
cycle_length = [5, 5, 5]
marriage_status = [20, 25, 30]
no_of_abortion = [0, 0, 0]
fsh = [9.95, 6.75, 5.54]
lh = [3.67, 1.09, 0.88]
ths = [0.68, 3.16, 2.54]
amh = [2.07, 1.53, 6.63]
vit_d3 = [17.1, 61.3, 49.7]
prg = [0.57, 0.97, 0.36]
sugar = [92, 92, 84]
bp = [92, 92, 84]
endometrium = [8.5, 3.7, 10]

# Dependent variable (chance of infertility)
infertility = [0, 1, 1]  # Assuming 1 indicates infertility and 0 indicates no infertility

# Calculate means
mean_age = sum(age) / len(age)
mean_bmi = sum(bmi) / len(bmi)
mean_hb = sum(hb) / len(hb)
mean_cycle_length = sum(cycle_length) / len(cycle_length)
mean_marriage_status = sum(marriage_status) / len(marriage_status)
mean_no_of_abortion = sum(no_of_abortion) / len(no_of_abortion)
mean_fsh = sum(fsh) / len(fsh)
mean_lh = sum(lh) / len(lh)
mean_ths = sum(ths) / len(ths)
mean_amh = sum(amh) / len(amh)
mean_vit_d3 = sum(vit_d3) / len(vit_d3)
mean_prg = sum(prg) / len(prg)
mean_sugar = sum(sugar) / len(sugar)
mean_bp = sum(bp) / len(bp)
mean_endometrium = sum(endometrium) / len(endometrium)
mean_infertility = sum(infertility) / len(infertility)

# Calculate coefficients
epsilon = 1e-10
beta1 = sum((xi - mean_age) * (yi - mean_infertility) for xi, yi in zip(age, infertility)) / (sum((xi - mean_age)**2 for xi in age))
beta2 = sum((xi - mean_bmi) * (yi - mean_infertility) for xi, yi in zip(bmi, infertility)) / sum((xi - mean_bmi)**2 for xi in bmi )
beta3 = sum((xi - mean_hb) * (yi - mean_infertility) for xi, yi in zip(hb, infertility)) / sum((xi - mean_hb)**2 for xi in hb )
beta4 = sum((xi - mean_cycle_length) * (yi - mean_infertility) for xi, yi in zip(cycle_length, infertility)) / (sum((xi - mean_cycle_length)**2 for xi in cycle_length) + epsilon)
beta5 = sum((xi - mean_marriage_status) * (yi - mean_infertility) for xi, yi in zip(marriage_status, infertility)) / sum((xi - mean_marriage_status)**2 for xi in marriage_status )
beta6 = sum((xi - mean_no_of_abortion) * (yi - mean_infertility) for xi, yi in zip(no_of_abortion, infertility)) / (sum((xi - mean_no_of_abortion)**2 for xi in no_of_abortion) + epsilon)
beta7 = sum((xi - mean_fsh) * (yi - mean_infertility) for xi, yi in zip(fsh, infertility)) / sum((xi - mean_fsh)**2 for xi in fsh)
beta8 = sum((xi - mean_lh) * (yi - mean_infertility) for xi, yi in zip(lh, infertility)) / sum((xi - mean_lh)**2 for xi in lh)
beta9 = sum((xi - mean_ths) * (yi - mean_infertility) for xi, yi in zip(ths, infertility)) / sum((xi - mean_ths)**2 for xi in ths)
beta10 = sum((xi - mean_amh) * (yi - mean_infertility) for xi, yi in zip(amh, infertility)) / sum((xi - mean_amh)**2 for xi in amh)
beta11 = sum((xi - mean_vit_d3) * (yi - mean_infertility) for xi, yi in zip(vit_d3, infertility)) / sum((xi - mean_vit_d3)**2 for xi in vit_d3)
beta12 = sum((xi - mean_prg) * (yi - mean_infertility) for xi, yi in zip(prg, infertility)) / sum((xi - mean_prg)**2 for xi in prg)
beta13 = sum((xi - mean_sugar) * (yi - mean_infertility) for xi, yi in zip(sugar, infertility)) / sum((xi - mean_sugar)**2 for xi in sugar)
beta14 = sum((xi - mean_bp) * (yi - mean_infertility) for xi, yi in zip(bp, infertility)) / sum((xi - mean_bp)**2 for xi in bp)
beta15 = sum((xi - mean_endometrium) * (yi - mean_infertility) for xi, yi in zip(endometrium, infertility)) / sum((xi - mean_endometrium)**2 for xi in endometrium)

# New data for prediction
new_data = [30, 23.0, 11.0, 5, 22, 0, 7.0, 2.5, 2.0, 1.8, 30.0, 1.0, 90, 90, 8.0]
beta0 = (mean_infertility - beta1*mean_age - beta2*mean_bmi - beta3*mean_hb - beta4*mean_cycle_length - beta5*mean_marriage_status - beta6*mean_no_of_abortion - beta7*mean_fsh - beta8*mean_lh - beta9*mean_ths - beta10*mean_amh - beta11*mean_vit_d3 - beta12*mean_prg - beta13*mean_sugar - beta14*mean_bp - beta15*mean_endometrium)

# Calculate the predicted chance of infertility using the linear regression formula
# predicted_infertility = (
#     beta0 +
#     beta1 * (new_data[0] - mean_age) +
#     beta2 * (new_data[1] - mean_bmi) +
#     beta3 * (new_data[2] - mean_hb) +
#     beta4 * (new_data[3] - mean_cycle_length) +
#     beta5 * (new_data[4] - mean_marriage_status) +
#     beta6 * (new_data[5] - mean_no_of_abortion) +
#     beta7 * (new_data[6] - mean_fsh) +
#     beta8 * (new_data[7] - mean_lh) +
#     beta9 * (new_data[8] - mean_ths) +
#     beta10 * (new_data[9] - mean_amh) +
#     beta11 * (new_data[10] - mean_vit_d3) +
#     beta12 * (new_data[11] - mean_prg) +
#     beta13 * (new_data[12] - mean_sugar) +
#     beta14 * (new_data[13] - mean_bp) +
#     beta15 * (new_data[14] - mean_endometrium)
# )

# print("Predicted Chance of Infertility for New Data:", predicted_infertility)


import pandas as pd 
import matplotlib.pyplot as plt 
import math
from sklearn.metrics import mean_squared_error
from sklearn import linear_model #Scipy provides low-level mathematical and scientific functions. scikit-learn provides high-level machine learning functions.
empl = pd.read_csv('d:/vishwajeet/Python-for-beginner/Python-for-beginner/infertility_data_csv.csv')
test_set = pd.read_csv('d:/vishwajeet/Python-for-beginner/Python-for-beginner/PCOS_data.csv')

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
def plot_infertility(pcos, age, bmi, infertility, colors):
  plt.figure(figsize=(10, 6))  # Adjust figure size as needed

  # Scatter plot with transparency
  for i in range(len(pcos)):
    plt.scatter(age[i], bmi[i], alpha=0.7, c=colors[infertility[i]])

  # Labels and title
  plt.xlabel('Age')
  plt.ylabel('BMI')
  plt.title('Infertility by PCOS Status, Age, and BMI (Sample Data)')

  # Add legend for infertility categories (optional)
  if len(set(infertility)) > 1:
    plt.legend()

  plt.show()

# Color list based on infertility (modify as needed)
colors = {1: 'green', 0: 'red'}

# Call the plotting function
plot_infertility(empl.PCOS, empl.Age, empl.BMI, empl.Pregnant, colors)

reg = linear_model.LinearRegression()
X = empl[['Age','BMI','Hb','Cycle_length','Marriage_Status','no_of_abortion','FSH','LH','TSH','AMH','Vit_D3','PRG','RBS','BP_Systolic','Endometrium']]
Y = empl['Pregnant']

reg.fit(empl[['Age','BMI','Hb','Cycle_length','Marriage_Status','no_of_abortion','FSH','LH','TSH','AMH','Vit_D3','PRG','RBS','BP_Systolic','Endometrium']].values,empl['Pregnant'])
value = reg.coef_ 
value1 = reg.intercept_
value2 = reg.predict([new_data])
# print('pridiction')
# print(value2)

# print(value)
# print(value1)
tested_data = reg.predict(test_set[['Age','BMI','Hb','Cycle_length','Marriage_Status','no_of_abortion','FSH','LH','TSH','AMH','Vit_D3','PRG','RBS','BP_Systolic','Endometrium']])
# print(tested_data)









rmse = math.sqrt(mean_squared_error([1,0,0,0],test_set.Pregnant)) *100
print("Accuracy of linear Regression : " , rmse)

