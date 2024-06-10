from datetime import datetime
class insurance:
    def __init__(self):
        self.insurance_status = ""
        self.insurance_company = ""
        self.insurance_number = ""
        self.insurance_validity = ""
        self.insurance_list = []


    def getInsuranceStatus(self):
        #Get the insurance Status from the Patient (Publicly or Privately)
        while True:

            self.insurance_status = input("What is your insurance status? Are you publicly or privately insured?: ")

            #Error Handeling
            if self.insurance_status == "":
                print("Invalid input please follow the instructions to continue")
                continue
            else:
                break

    def getInsuranceCompany(self):
        #Get the Insurance Company from the Patient (Hkk, Aok...)
        while True:
            self.insurance_company = input("What is your Hospital Insurance Company: ")

            #Error Handeling
            if self.insurance_company == "":
                print("Invalid input please follow the instructions to continue")
                continue
            else:
                break
    def getInsuranceNumber(self):
        #Get the insurance Number from the Patient
        while True:

            self.insurance_number = int(input("Please type in your Insurance Number: "))

            #Error Handeling
            if self.insurance_number == "":
                print("Invalid input please follow the instructions to continue")
                continue
            else:
                break

    def getInsuranceValidtiy(self):
        #determine the insurance validtity from the patient and convert the validity in to a date
        while True:

            validity = input("Is your insurance card guilty? Y/N: ")
            if validity == "Y":
                validity_status_month = input("Please type in the Month of your card guiltiness: ")
                validity_status_year = input("Please type in the Year of your card guiltiness: ")
                self.insurance_validity = validity_status_month + validity_status_year
                print(f"Thank you your card guiltiness is: {self.insurance_validity}")

            if self.insurance_validity == "":
                print("Invalid input please follow the instructions to continue")
                continue
            else:
                break

    def getInsuranceState(self):
        return self.insurance_status #We need this in another file

    def getInsuranceList(self):
        #Convert your Insurances into a list if you have one
        while True:
            other_insurance = input("Do you have other insurances Y/N: ")
            if other_insurance == "Y":
                print("Okay please continue")
                count_insurance = int(input("Please type in how many other insurances do you have: "))
                for i in range(count_insurance):
                    other_insurance = input("What other insurances do you have: ")
                    self.insurance_list.append(other_insurance)
                    print(f"Your insurances are: {self.insurance_list}")
            elif other_insurance == "N":
                print("Okay thank you please continue and follow the instructions")
                break

            #Error Handeling
            if self.insurance_list == "":
                print("Invalid input please follow the instructions to continue")
                continue
            else:
                break

    def __str__(self):
        #Convert everything into a string
        print("\n")
        return (f"Thankyou now we know that your insurance status is: {self.insurance_status} \n"
                f" Thankyou now we know that your insurance Company is: {self.insurance_company} \n"
                f" Thank you now we know that your insurance number is: {self.insurance_number} \n"
                f" Thank you now we know that your insurance is {self.insurance_validity} \n"
                f" Thank you now we know that your other insurances are: {', '.join(self.insurance_list)}\n")

insurance_person = insurance()
insurance_person.getInsuranceStatus()
insurance_person.getInsuranceCompany()
insurance_person.getInsuranceNumber()
insurance_person.getInsuranceValidtiy()
insurance_person.getInsuranceList()
print(insurance_person)