class name_Patient:
    def __init__(self):
        self.Name = ""

    def getName(self):
        while True:
            try:
                first = input("What is your first Name: ")
                last = input("What is your last Name: ")

                self.Name = f"{first} {last}"
                print(f"Your Name is {self.Name}")
                break

            except Exception as e:
                print("Invalid input please follow the instructions to continue")
                print(f"Error {e}")



name = name_Patient()
name.getName()
