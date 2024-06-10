class medicalList:
    def __init__(self):
        self.ListMedic = []

    def getMedicalList(self):
        #Get your Medical list
        while True:
            try:
                medicalStatus = input("Do you take medicals Y/N: ")
                if medicalStatus == "Y":

                    #Converts Everything into a List
                    countMedicals = int(input("Please type in how many medicals do you take: "))
                    for i in range(countMedicals):
                        dailyMedicals = input("Please type in what medicals do you take: ")
                        self.ListMedic.append(dailyMedicals)
                    print("Thank you now we know what medicals you must take every day")

                else:
                    medicalStatus = "N"
                    print("Okay thats good please continue withe the programm")

            #Error Handeling
            except Exception as e:
                print("Invalid Syntax please follow the instructions to continue")
                print(f"Error as {e}")
                continue

            else:
                break

    def __str__(self):
        return (f"Thank you now we know that the daily medicals that you must take are: \n"
                f"{self.ListMedic}")

medicals_person = medicalList()
medicals_person.getMedicalList()
print(medicals_person)