# class ChineseChef:
# what if the Chinese Chef can do everything that Chef class do.
# that I want to give this Chinese Chef all functionality that Chef class has
# one way to do is that copy and pasted the functions in Chef class as below,
#     def make_chicken(self):
#         print ("the chef makes a chicken")
#     def make_salad(self):
#         print ("The chef makes a salad")
#     def make_special_dish(self):
#         print ("The chef makes orange chicken") and make differences if you need
#     def make_fired_rice(self):
#         print ("The chef makes fired rice") and add some new functions if you need

'''instead of copy and paste, we can apply inheritance to inherit the function in Chef class'''

from Chef import Chef


class ChineseChef(Chef):

    def make_special_dish(self):
        print("The chef makes orange chicken")  # if you need a change that you can rewrite this function

    def make_fired_rice(self):
        print("The chef makes fired rice")
