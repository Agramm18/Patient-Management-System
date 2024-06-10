class WeightHeight:
    def __init__(self):
        self.weight = ""
        self.height = ""

    def getHeight(self):
        #Gets the height from the Patient
        while True:
            print("Please note that every input must be numerical.")
            self.height = float(input("Please type in your actual height: "))
            self.height = round(self.height, 2)

            if self.height == "":
                print("Invalid input please follow the instructions to continue")
                continue
            else:
                break

    def getWeight(self):
        #Gets the weight from the Patient
        while True:

            print("Please note that every input must be numerical.")
            self.weight = float(input("Please type in your actual weight: "))
            self.weight = round(self.weight, 3)

            if self.weight == "":
                print("Invalid input please follow the instructions to continue")
                continue
            else:
                break

    def get_Weight(self):
        return self.weight #we need this in another file

    def get_Height(self):
        return self.height #We need this in another file

    def __str__(self):
        return (f"Thank you, now we know that your current weight is {self.weight} kg "
                f"and your current height is {self.height} m. \n")

weight_hight = WeightHeight()
weight_hight.getWeight()
weight_hight.getHeight()
weight_hight.get_Weight()
weight_hight.get_Height()
print(weight_hight)

