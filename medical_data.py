#import the other functions and classes for calculation
from datetime import datetime
from Birthdate import PatientBirth
from Gender import PatientGender
from weight_and_height import weight_hight


class medical_data:
    def __init__(self):
        #Convert the imports into a constructor
        self.age = PatientBirth.currentAge()
        self.gender = PatientGender.getGender()
        self.weight = weight_hight.get_Weight()
        self.height = weight_hight.get_Height()

    def getBMI(self):
        #Calculate your BMI based on your gender and age
        if self.gender.lower() == "male" and self.age > 20:
            bmi_calculation = self.weight / (self.height * self.height)
            return round(bmi_calculation, 2)

        elif self.gender.lower() == "male" and self.age < 20:
            bmi_calculation = self.weight / (self.height * self.height)
            return round(bmi_calculation, 2)

        elif self.gender.lower() == "female" and self.age > 20:
            bmi_calculation = 1.3 * (self.weight / (self.height * self.height))
            return round(bmi_calculation, 2)

        elif self.gender.lower() == "female" and self.age < 20:
            bmi_calculation = (self.weight / (self.height * self.height)) * 1.3
            return round(bmi_calculation, 2)

        else:
            return "Invalid input please follow the instructions"

    def getBMIStatus(self):

        #Outputs your BMI Status based on the BMI Table and your gender and age
        bmi_wert = self.getBMI()
        if self.gender.lower() == "female" and bmi_wert < 17.5:
            print("According to BMI table you are underweight")

        elif self.gender.lower() == "female" and 17.9 < bmi_wert < 25:
            print("According to BMI table you are at normal weight, Congratulations")

        elif self.gender.lower() == "female" and 23.99 < bmi_wert < 30:
            print("According to BMI table you are overweight")

        elif self.gender.lower() == "female" and 28.99 < bmi_wert < 35:
            print("According to BMI table you have Obesity level 1")

        elif self.gender.lower() == "female" and 33.99 < bmi_wert < 36.6:
            print("According to BMI table you have Obesity level 2")

        elif self.gender.lower() == "female" and bmi_wert > 39:
            print("According to BMI table you have Obesity level 3")


        elif self.gender.lower() == "male" and bmi_wert < 20:
            print("According to BMI table you are underweight")

        elif self.gender.lower() == "male" and 19.99 < bmi_wert < 24.9:
            print("According to BMI table you are at normal weight, Congratulations")

        elif self.gender.lower() == "male" and 25 < bmi_wert < 29.99:
            print("According to BMI table you are overweight")

        elif self.gender.lower() == "male" and 30 < bmi_wert < 34.9:
            print("According to BMI table you have Obesity level 1")

        elif self.gender.lower() == "male" and 35 < bmi_wert < 39.9:
            print("According to BMI table you have Obesity level 2")

        elif self.gender.lower() == "male" and bmi_wert > 40:
            print("According to BMI table you have Obesity level 3")

    def getOptimalenBloolpressure(self):
        #Outputs the perfect BloodPressure based on your age
        if self.age in range(1, 5):
            optimal_blood_pressure = range(60, 80)
            print(f"The patient's optimal blood pressure is between {optimal_blood_pressure}")

        elif self.age in range(6, 12):
            optimal_blood_pressure = range(60, 95)
            print(f"The patient's optimal blood pressure is between {optimal_blood_pressure}")

        elif self.age in range(13, 20):
            optimal_blood_pressure = range(70, 110)
            print(f"The patient's optimal blood pressure is between {optimal_blood_pressure}")

        elif self.age in range(20, 50):
            optimal_blood_pressure = range(80, 120)
            print(f"The patient's optimal blood pressure is between {optimal_blood_pressure}")

        elif self.age > 49:
            optimal_blood_pressure = range(95, 150)
            print(f"The patient's optimal blood pressure is between {optimal_blood_pressure}")


medicalData = medical_data()
medicalData.getBMI()
print(f"The Patients BMI is: {medicalData.getBMI()}")
medicalData.getBMIStatus()
medicalData.getOptimalenBloolpressure()
print()
