class contact:
    def __init__(self):
        self.phone = ""
        self.email = ""

    def getContact(self):
        while True:
            try:
                self.phone = int(input("Please type in your phone number: ")) #Get the Number from the Patient
                self.email = input("Please type in your Email adress: ") #Get the E-Mail from the Patient
                break

            #Error Handeling
            except Exception as e:
                print("Invalid input please follow the instructions to continue")
                print(f"Error {e}")
                continue

    def contaccallback(self):
            #Get the Contact Status from the Patient
                print("Type in both, specific or no to continue")
                CallBack = input("Can we call or type you back on phone or email or both: ")

                if CallBack == "both":
                    print("Thank you we will call you back on phone and email")

                elif CallBack == "specific":
                    CallBackSpecific = input("What would you prefer to be contact at phone or email: ")
                    print("Type in phone or email to continue")

                    if CallBackSpecific == "phone":
                        print("Okay we will contact you only via phone")
                        print("Continue with the programm")

                    elif CallBackSpecific == "email":
                        print("Okay we will contact you only via email")
                        print("Continue with the programm")

                elif CallBack == "no":
                    print("Okay we wont call or type you back")
                    print("Continue with the programm")

    def __str__(self):
        return (f"Thank you now we know that your Phone Number is: {self.phone} and that your Email is: "
                f" {self.email}")

Contact_Patient = contact()
Contact_Patient.getContact()
Contact_Patient.contaccallback()
print(Contact_Patient)