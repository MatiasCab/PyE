from fractions import Fraction
import random

def montysGame(changeDoor, showLog):
    doorsList = [1, 2, 3]
    carDoor = random.randint(1, 3)
    doorSelected = random.randint(1, 3)
    doorsList.remove(doorSelected)

    if (carDoor == doorSelected):
        montysDoor = random.randint(0, 1)
        montysDoor = doorsList.pop(montysDoor)
    else:
        montysDoor = doorsList.pop(1 if doorsList[0] == carDoor else 0)

    previousDoor = doorSelected 
    if (changeDoor):
        doorSelected = doorsList[0]
    if (showLog):
        print(f"Puerta elegida: {previousDoor}")
        print(f"Puerta donde esta el auto: {carDoor}")
        print(f"Puerta que abrio Monty: {montysDoor}")
        print(f"Se cambio la puerta {previousDoor} a {doorSelected}" if changeDoor else "No cambio la puerta")
        print("Jugador gano el auto" if carDoor == doorSelected else "Jugador perdio el auto")
    return carDoor == doorSelected

def montysGameAnalyzer(changeDoor, maxRange):
    victories = 0
    for i in range(0, maxRange):
        if(montysGame(changeDoor, False)):
            victories += 1
    return victories

def printAnalyzer(maxRange):
    victories = montysGameAnalyzer(True, maxRange)
    victoriesPercentage = round(victories * (100/maxRange), 2)
    
    print(f"*****************Resultados para {maxRange}*****************\n")
    print(f"El jugador cambiando la puerta ganó {victories} ({victoriesPercentage}%) veces")
    print(f"Frecuencia: {victories}\nFrecuencia relativa: {victories/maxRange}")
    print(f"Probabilidad: {Fraction(victories,maxRange)}\n")
    
    victories = montysGameAnalyzer(False, maxRange)
    victoriesPercentage = round(victories * (100/maxRange), 2)
    
    print(f"El jugador sin cambiar la puerta ganó {victories} ({victoriesPercentage}%) veces")
    print(f"Frecuencia: {victories}\nFrecuencia relativa: {victories/maxRange}")
    print(f"Probabilidad: {Fraction(victories,maxRange)}\n")
    print("-----------------------------------------\n")
    return

printAnalyzer(1000)
printAnalyzer(10000)
printAnalyzer(100000)

