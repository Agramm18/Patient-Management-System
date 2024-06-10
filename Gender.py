class BiologicalGender:
    def __init__(self):
        self.Gender = ""

    def getBiologicalGender(self):
        #Get the Biological Gender from user input
        while True:

            self.Gender = input("Type in your Biological Gender male/ female or divers: ")

            #Error Handeling
            if self.Gender == "":
                    print("Invalid input please follow the instructions to continue")
                    continue

            elif self.Gender == "M":
                self.Gender = "Male"

            elif self.Gender == "F":
                self.Gender = "Female"

            elif self.Gender == "D":
                self.Gender = "Diverse"

            else:
                break

    def getGender(self):
        return self.Gender #We need this in another file for a function

    def __str__(self):
        #Convert everything to a string
        return f"Thank you, now we know that your Biological gender is: {self.Gender}\n"

PatientGender = BiologicalGender()
PatientGender.getBiologicalGender()
print(PatientGender)

