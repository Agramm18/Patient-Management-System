#Date Time Import
from datetime import datetime
class BirthDate:
    #Birthdate Class initalisation
    def __init__(self):
        self.birth_day = int #Get the Birth date
        self.birth_month = int #Get the Birth Month
        self.birth_year = int #Get the Birth Year
        self.Current_Age = int #Get the current age from the Patient  from the calculation
        self.Birth_Date = int #Get the Birthdate from the Patient

    def getBirthDate(self):
        while True:
            try:
                print("\n")
                print("Note that every input must be in numerical integer inputs")
                self.birth_day= int(input("Ohn what date were you born: ")) #Get the Birthdate from the Patient

                self.birth_month = int(input("On what month were you born: ")) #Get the Birth Month from the Patient

                self.birth_year = int(input("On what year where you born: ")) #Get the Birth Year from the Patient

                self.Birth_Date = datetime(day=self.birth_day, month=self.birth_month, year=self.birth_year) #Get the Birthdate from Birth day, Birth month and Birth Year

                #Calculate the current age with the current age and the Birth Date
                Current_Date = datetime.now().year
                self.Current_Age = Current_Date - self.birth_year
                break

            #+Error Handeling
            except ValueError:
                print("Invalid Input please follow the instructions to continue")
            except Exception as e:
                print(f"Error: {e} ")

    def currentAge(self):
        return (self.Current_Age) #This will be needed for a calculation in another file

    def __str__(self):
        return (f"Thank you now we know that the Patient is: {self.Current_Age} years old \n"
                f" The Birthdate from the patient is: {self.Birth_Date}\n")

PatientBirth = BirthDate()
PatientBirth.getBirthDate()
PatientBirth.currentAge()
print(PatientBirth)