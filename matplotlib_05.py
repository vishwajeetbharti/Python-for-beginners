from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter

class Addmision:
    def plotGraph(self,key,value):
        plt.barh(key,value,color='green')
        plt.xlabel('Number of student')
        plt.title('Students addmision Lists')
        plt.show()

    def trigerSwitch(self ,argument):
        match argument:
            case 1:
                print('hhh')
                self.sickSemData(3)
            case 2:
                self.sickSemData(5)
            case 3:
                self.sickSemData(7)
            case 4:
                self.sickData()
            case default:
                return "Invalid Input\n"
    
    def sickSemData(self,semester):
        students = pd.read_csv('amc.csv')

        all_data = pd.DataFrame(students)
        sem_accr_gen = all_data[['sem','admittedQuota']]

        sem = {}
        for item in range(len(sem_accr_gen)):
            if f'{semester}_MGMT' not in sem.keys():
                sem[f'{semester}_MGMT'] = 0
                sem[f'{semester}_SNQ'] = 0
                sem[f'{semester}_CET'] = 0
                sem[f'{semester}_COMED-K'] = 0
                sem[f'{semester}_KCET'] = 0
                sem[f'{semester}_Pmsss_scholarship'] = 0

            if(sem_accr_gen['admittedQuota'][item]=="MGMT" and sem_accr_gen['sem'][item]==semester):
                sem[f'{sem_accr_gen["sem"][item]}_MGMT'] +=1
            elif(sem_accr_gen['admittedQuota'][item]=="SNQ"and sem_accr_gen['sem'][item]==semester):
                sem[f'{sem_accr_gen["sem"][item]}_SNQ'] +=1
            elif(sem_accr_gen['admittedQuota'][item]=="CET"and sem_accr_gen['sem'][item]==semester):
                sem[f'{sem_accr_gen["sem"][item]}_CET'] +=1
            elif(sem_accr_gen['admittedQuota'][item]=="COMED-K"and sem_accr_gen['sem'][item]==semester):
                sem[f'{sem_accr_gen["sem"][item]}_COMED-K'] +=1
            elif(sem_accr_gen['admittedQuota'][item]=="KCET"and sem_accr_gen['sem'][item]==semester):
                sem[f'{sem_accr_gen["sem"][item]}_KCET'] +=1
            elif(sem_accr_gen['admittedQuota'][item]=="Pmsss scholarship"and sem_accr_gen['sem'][item]==semester):
                sem[f'{sem_accr_gen["sem"][item]}_Pmsss_scholarship'] +=1
        key = []
        value = []
        for item in sem:
            key.append(item)
            value.append(sem[item])
        self.plotGraph(key,value)
    
    def sickData(self):
        stu_data = pd.read_csv('amc.csv')
        addmi_count = Counter()
        addmission_kotta= []
        no_Of_Students= []
        addmission_data = stu_data['admittedQuota']
        for item in addmission_data:
            addmi_count.update([item])
    
        for item in addmi_count:
            addmission_kotta.append(item)
            no_Of_Students.append(addmi_count[item])
        self.plotGraph(addmission_kotta,no_Of_Students)


print("\n1. 3th sem Students\n2. 5th sem Students\n3. 7th sem Students\n4. All Semester")
choice = int(input('Enter your choice\n'))
obj = Addmision()
obj.trigerSwitch(choice)
