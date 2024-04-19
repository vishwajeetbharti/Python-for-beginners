# Logistic function
import math
import pandas as pd


empl = pd.read_csv('infertility_data_csv.csv')
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


def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Given data
age = empl['Age'].values
bmi = empl['BMI'].values
hb = empl['Hb'].values
cycle_length = empl['Cycle_length'].values
marriage_status = empl['Marriage_Status'].values
no_of_abortion = empl['no_of_abortion'].values
fsh = empl['FSH'].values
lh = empl['LH'].values
ths = empl['TSH'].values
amh = empl['AMH'].values
vit_d3 = empl['Vit_D3'].values
prg = empl['PRG'].values
sugar = empl['RBS'].values
bp = empl['BP_Diastolic'].values
endometrium = empl['Endometrium'].values

# Dependent variable (chance of infertility)
infertility = [0, 1, 1]  # Assuming 1 indicates infertility and 0 indicates no infertility

# Calculate means
mean_age = sum(age) / len(age)
# print(mean_age)
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
beta0 = sum(yi - mean_infertility for yi in infertility) / len(infertility)

# print(beta0)
beta1 = sum((xi - mean_age) * (yi - mean_infertility) for xi, yi in zip(age, infertility)) / sum((xi - mean_age)**2 for xi in age)
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

# Calculate the predicted chance of infertility using the linear regression formula
predicted_infertility = (
    beta0 +
    beta1 * (new_data[0] - mean_age) +
    beta2 * (new_data[1] - mean_bmi) +
    beta3 * (new_data[2] - mean_hb) +
    beta4 * (new_data[3] - mean_cycle_length) +
    beta5 * (new_data[4] - mean_marriage_status) +
    beta6 * (new_data[5] - mean_no_of_abortion) +
    beta7 * (new_data[6] - mean_fsh) +
    beta8 * (new_data[7] - mean_lh) +
    beta9 * (new_data[8] - mean_ths) +
    beta10 * (new_data[9] - mean_amh) +
    beta11 * (new_data[10] - mean_vit_d3) +
    beta12 * (new_data[11] - mean_prg) +
    beta13 * (new_data[12] - mean_sugar) +
    beta14 * (new_data[13] - mean_bp) +
    beta15 * (new_data[14] - mean_endometrium)
)

predicted_probability = sigmoid(predicted_infertility)
#print(beta0,beta1,beta2,beta3,beta4,beta5,beta6,beta7,beta8,beta9,beta10,beta11,beta12,beta13,beta14,beta15)
print("\nPredicted Chance of Infertility for New Data:", predicted_probability)