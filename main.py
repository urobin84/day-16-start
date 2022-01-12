# import another_module
# print(another_module.another_variable)

# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
#
# my_screen = Screen()
# my_screen.canvheight
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Nama Nabi", ["Adam", "Idris"])
table.add_column("Mujizat Nabi", ["Adam", "Idris"])

table.align = "l"
print(table)