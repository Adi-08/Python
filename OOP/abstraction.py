class Car:
    def __init__(self):
        # These are internal details of the car.
        # The user does not need to manually control these variables.
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        # Abstraction:
        # The user only needs to call start().
        # They don't need to know HOW the car starts internally.
        #
        # Behind the scenes, the car:
        # 1. Presses clutch
        # 2. Presses accelerator
        # 3. Starts the car
        self.clutch = True
        self.acc = True

        print("Car started")


car1 = Car()

# We simply tell the car to start.
# We don't worry about the internal steps.
car1.start()