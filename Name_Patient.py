class DataPatient:

    def __init__(self):
        self.name = ""
        self.last_name = ""

    def getName(self):
        #Get the Patients first Name
        self.name = input("Enter your first name: ")
        return self.name

    def getNameLast(self):
        #Get the Patients last name
        self.last_name = input("What is your last name: ")
        return self.last_name

    def __str__(self):
        return f"The patient's name is: {self.name} {self.last_name}\n"

    def errorHandlingFirstName(self):
        #Error Handeling
        while True:
            try:
                if self.getName() == "":
                    print("Invalid input. Please enter your first name to continue.")
                    continue
                break
            except Exception as e:
                print(f"Error {e}")

    def errorHandlingLastName(self):
        #Error Handeling
        while True:
            try:
                if self.getNameLast() == "":
                    print("Invalid input. Please enter your last name to continue.")
                    continue
                break
            except Exception as e:
                print(f"Error {e}")

NamePatient = DataPatient()
NamePatient.errorHandlingFirstName()
NamePatient.errorHandlingLastName()
print(NamePatient)
