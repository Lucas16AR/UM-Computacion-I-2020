import random
from carton import Carton
from bingo import Bingo
from os import system
from prettytable import PrettyTable

myTable = PrettyTable(["Bola extraida", "En carton ID 0", "En carton ID 1", "En carton ID 2", "En carton ID 3", "En carton ID 4"])

system("cls")
cartones = []

def generate_cartons():
    for i in range(5):
        IdCarton = i
        lengCarton = random.randrange(4, 8)
        numbersCarton = random.sample(bingo1.bombo, lengCarton)
        
        carton = Carton(IdCarton, numbersCarton, lengCarton)
        cartones.append(carton)

carton_winner = ""
winner = False
balls_for_table = []
def take_ball_from_bombo():
    global carton_winner
    global winner
    global balls_for_table
    ball = bingo1.random_ball()
    balls_for_table.append(ball)
    for i in range(len(cartones)):
        if ball in cartones[i].numbers:
            cartones[i].numbers.remove(ball)
            balls_for_table.append("SI")
            if len(cartones[i].numbers) == 0:
                carton_winner = cartones[i].Id
                winner = True
                break
        else:
            balls_for_table.append("no")
    if len(balls_for_table) == 5:
        myTable.add_row(balls_for_table)
    else:
        faltantes = 6 - len(balls_for_table)
        for i in range(faltantes):
            balls_for_table.append("no")
        myTable.add_row(balls_for_table) 
    balls_for_table = []
    


def start_take_balls_to_the_end():

    for i in range(len(bingo1.bombo)):
        take_ball_from_bombo()
        if winner:
            print("El ganador fue el carton con el ID: {}".format(carton_winner))
            break





bingo1 = Bingo(0, [i for i in range(100)], [], 0, 0)
generate_cartons()

print("================Cartones==========")
for c in cartones:
    print(c)
print("===================================")
print("\n\n\n")

start_take_balls_to_the_end()

print(myTable)

