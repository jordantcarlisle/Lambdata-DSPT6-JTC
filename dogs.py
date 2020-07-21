from pdb import set_trace as breakpoint


class Dog():
    def __init__(self, name, age, housebroke, breed):
        self.name = name
        self.age = age
        self.breed = breed
        self.housebroke = housebroke

    def is_housebroke(self):
        if self.housebroke == True:
            print(f'{self.name} is housebroken!')
        else:
            print(f'{self.name} is not housebroken... :(')


class Beagle(Dog):
    def barks_alot(self, barker)


if __name__ == "__main__":

    lucky = Dog('Lucky', 2, True)
    breakpoint()
