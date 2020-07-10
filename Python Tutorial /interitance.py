from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_salad()
# it still works that ChineseChef can still make chicken and salad

myChineseChef.make_special_dish()
# due to the ChineseChef class modify the new function of making special dish
# it will shows that ChineseChef make special dish as orange chicken instead of bbq ribs

