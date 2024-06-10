import random
from insurance import insurance_person

class getRoom:
    def __init__(self):
        self.insurance_status = insurance_person.getInsuranceState()

    def getRoom(self):
        #Give the Patient a room based on his helath and insurance status
        while True:

            try:

                if self.insurance_status.lower() == "privately":
                    sick_status = input("Is the patient severely ill or in a wheelchair? Y/N: ")
                    if sick_status == "Y":
                        floor = print("The patient is on the 1st floor")
                        room = random.randint(1, 30)
                        print(f"The Patient get the Room: {room}")

                    elif sick_status == "N":
                        floor = print("The patient is on the 2nd floor")
                        room = random.randint(1, 30)
                        print(f"The Patient get the Room: {room}")

                    else:
                        print("Invalid input, please type Y or N to continue")

                elif self.insurance_status.lower() == "publicly":
                    sick_status = input("Is the patient severely ill or in a wheelchair? Y/N: ")
                    if sick_status == "Y":
                        floor = print("The patient is on the 3rd floor")
                        room = random.randint(1, 30)
                        print(f"The Patient get the Room: {room}")

                    elif sick_status == "N":
                        floor = print("The patient is on the 4th floor")
                        room = random.randint(1, 30)
                        print(f"The Patient get the Room: {room}")

                    else:
                        print("Invalid input, please type Y or N to continue")

                else:
                    print("Invalid input, please follow the instructions")

            except Exception as e:
                print("Invalid input please follow the instructions to continue")
                print(f"Error as {e}")

            else:
                break


Room = getRoom()
Room.getRoom()
print()

