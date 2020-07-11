from pdb import set_trace as breakpoint


class Dog():

    """Use the Dog class to store and retrieve information about dogs. name,
    age, housebroke, breed."""

    def __init__(self, name, age, housebroke, breed):
        self.housebroke = housebroke
        self.name = name
        self.age = age
        self.breed = breed
        self.housebroke = housebroke

    def is_housebroke(self):
        if self.housebroke == True:
            print(f'{self.name} is housebroken!')
        else:
            print(f'{self.name} is not housebroken...')

    #    super(, self).__init__()
    #    self.arg = arg

class Beagle(Dog):
    pass

if __name__ == "__main__":

    lucky = Dog('Lucky', 2, False, True)
    breakpoint()
