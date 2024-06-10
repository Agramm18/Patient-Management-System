class adress:
    #Inintalation from the Class Adress
    def __init__(self):
        self.country = ""
        self.state = ""
        self.city = ""
        self.postal_code = ""
        self.street_name = ""
        self.street_number = ""

    def getAdress(self):
        #The User must type in his Adress information
        #Based on Country/ State/ City/ Postal Code/ Street Name and Street number
        while True:
                self.country = input("In what Country do you live: ")
                self.state = input("In what State do you live: ")
                self.city = input("In what city do you live: ")
                self.postal_code = input("what is your Postal Code: ")
                self.street_name = input("What is your street name where you live: ")
                self.street_number = input("What is your current Street Number: ")

                #Error handeling if the user input is empty
                if self.country == "":
                    print("Invalid input please follow the instructions to continue")
                elif self.state == "":
                    print("Invalid input please follow the instructions to continue")
                elif self.city == "":
                    print("Invalid input please follow the instructions to continue")
                elif self.postal_code == "":
                    print("Invalid input please follow the instructions to continue")
                elif self.street_name == "":
                    print("Invalid input please follow the instructions to continue")
                elif self.street_number == "":
                    print("Invalid input please follow the instructions to continue")
                else:
                    break

    def __str__(self):
        #String Convert for the Self Statments
        return (f"Thank you now we know that you live in: {self.country}, {self.state}, {self.city}, {self.postal_code},"
                f" {self.street_name}, {self.street_number} ")

adress_patient = adress()
adress_patient.getAdress()
print(adress_patient)

