class Driver:

    Available = False


    def __init__(self, name):
        self.name = name

    @classmethod
    def openApp(cls):
        cls.Available = True

    @classmethod
    def closeApp(cls):
        cls.Available = False

    @classmethod
    def checkAvailibility(cls):
        return cls.Available


