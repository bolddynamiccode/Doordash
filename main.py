
from restaurant import Restaurant
from Driver import Driver

res_1 = Restaurant('Wuhan', 'Chinese')
res_2 = Restaurant('Spaghetti', "Italian")





print(res_1.name)
print(res_1.foodType)
print(res_1.Available)
res_1.openRestaurant()
print(res_1.Available)
res_1.closeRestaurant()
print(res_1.Available)
print(res_2.Available)
res_2.openRestaurant()
print(res_2.Available)


driver_1 = Driver('Jeff')
print(driver_1.name)
print(driver_1.Available)
driver_1.openApp()
print(driver_1.Available)
driver_1.closeApp()
print(driver_1.Available)