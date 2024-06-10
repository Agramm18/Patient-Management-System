class emergencyContact:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.phone = ""
        self.country = ""
        self.state = ""
        self.city = ""
        self.postal_code = ""
        self.street_name = ""
        self.street_number = ""

    def getName(self):
        while True:

            first_name = input("Please type in the first name from your emergency contact: ") #Get the first name from the emergency Contact
            last_name= input("Please type in the last name from your emergency: ") #Get the last Name from the Emergency Contact

            self.name = first_name + "" "" + last_name #Output the full name from the Emergency Contact

            #Error Handeling
            if self.name == "":
                print("Invalid input please follow the instructions to continue")
                continue
            else:
                break

    def getContact(self):
        while True:

                self.phone = input("Please type in the phone number from your emergency contact: ") #Get the Contact from the emergency contact
                self.email = input("Please type in the email from your emergency contact: ") #Get the E-Mail from the emergency contact

                #Error Handeling
                if self.phone or self.email == "":
                    print("Invalid input please follow the instructions to continue")
                    continue
                else:
                    break


    def getAdress(self):
        #Get the Adress from your emergecny contact
        while True:

            self.country = input("In what Country does your emergency contact live: ")
            self.state = input("In what State does your emergency contact live: ")
            self.city = input("In what city does your emergency contact live: ")
            self.postal_code = input("what is the Postal Code from your emergency contact: ")
            self.street_name = input("What is the street name where your emergency contact lives: ")
            self.street_number = input("What is the current Street Number from your emergency contact: ")

            #Error Handeling
            if self.country or self.state or self.city or self.postal_code or self.street_name or self.street_number == "":
                print("Invalid input please follow the instructions to continue")
                continue
            else:
                break

    def getContactBackOptions(self):
        #Get Contact Status
        print("Type in both, specific or no to continue")
        CallBack = input("Can we call or type your emergency contact back on phone or email or both: ")

        if CallBack == "both":
            print("Thank you we will call your emergency contact back on phone and email")

        elif CallBack == "specific":
            CallBackSpecific = input("What would your emergency contact prefer to be contact at phone or email: ")
            print("Type in phone or email to continue")

            if CallBackSpecific == "phone":
                print("Okay we will contact your emergency contact only via phone")
                print("Continue with the programm")

            elif CallBackSpecific == "email":
                print("Okay we will contact your emergency contact only via email")
                print("Continue with the programm")

        elif CallBack == "no":
            print("Okay we wont call or type your emergency contact back")
            print("Continue with the programm")

    def __str__(self):
        #Convert every Thing to a string
        return (f"Thank you now we know that the name from your emergency contact is: {self.name} \n"
                f" Thank you now we know that the E-Mail adress from your emergency contact is: {self.email} \n"
                f" Thank you now we know that the phone number from your emergency contact is: {self.phone} \n"
                f"Thank you now we know that your emergency contact lives in: \n"
                f" Country: {self.country} \n"
                f" State: {self.state} \n"
                f" City: {self.city} \n"
                f" Postalcode: {self.postal_code} \n"
                f" Street Name: {self.street_name} \n"
                f" Street Number: {self.street_number} \n")

emergencyOptions = emergencyContact()
emergencyOptions.getName()
emergencyOptions.getContact()
emergencyOptions.getAdress()
emergencyOptions.getContactBackOptions()
print(emergencyOptions)