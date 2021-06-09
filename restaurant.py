class Restaurant:

    Available = False
    orderPlaced = False

    def __init__(self, name, foodType):
        self.name = name
        self.foodType = foodType

    @classmethod
    def openRestaurant(cls):
        cls.Available = True
    @classmethod
    def closeRestaurant(cls):
        cls.Available = False
        cls.orderPlaced = False

    @classmethod
    def checkAvailibility(cls):
        return cls.Available

    @classmethod
    def order(cls):
        if cls.Available == True:
            cls.orderPlaced = True

        else:
            return "Restaurant is closed"


res_1 = Restaurant('Wuhan', 'Chinese')
print(res_1.name)
res_1.openRestaurant()
print(res_1.checkAvailibility())
res_1.order()
print(res_1.orderPlaced)
res_1.closeRestaurant()
print(res_1.orderPlaced)
print(res_1.order())

