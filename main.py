class car(object):
    def __init__(self):
        print("we just created car instance")

    def drive(self):
        print("Car started...")

    def stop(self):
        print("Car is Stopped")


class bmw(car):
    def __init__(self):
        # this line is optional but preferred to have
        car.__init__(self)
        print("just created another class of bmw")

    def drive(self):
        # this executes original code + added code
        super().drive()
        # this is new added code
        print("you are driving BMW")

    @staticmethod
    def heads(self):
        print("The car have headslights")

c1 = car()
c1.drive()
c1.stop()

b = bmw()
b.drive()
b.stop()
b.heads('self')
