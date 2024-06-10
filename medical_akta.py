class medicalAkta:
    def __init__(self):
        self.medical_acta = []

    def getMedicalActa(self):
        #Make you medical acta
        while True:
            try:
                medical_history = input("Do you have a medical history? Y/N: ")

                if medical_history == "Y":

                    accidents = input("Did you have any accidents? Y/N: ")

                    #Converts everything into a list
                    if accidents == "Y":
                        accident_count = int(input("How many accidents did you have: "))
                        for i in range(accident_count):
                            self.medical_acta.append()
                            break

                    else:
                        print("Invalid input, please follow the instructions to continue")
                        continue

                elif medical_history == "N":
                    print("Well done, please continue with the other questions")
                    break

                else:
                    print("Invalid input, please follow the instructions to continue")
                    continue

            except Exception as e:
                print("Invalid input please follow the instructions to continue")
                print(f"Error as {e}")
                continue
            else:
                break

medical_acta = medicalAkta()
medical_acta.getMedicalActa()
print(medical_acta)
