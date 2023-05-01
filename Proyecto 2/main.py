import random

def diceGame(firstParticipantName, secondParticipantName):
    firstParticipantScore = playerDice(None)
    secondParticipantScore = playerDice(firstParticipantScore)
    
    if firstParticipantScore > secondParticipantScore:
        return  firstParticipantName
    elif firstParticipantScore < secondParticipantScore:
        return secondParticipantName
    else:
        return "EMPATE"

def playerDice(opponentScore):
    participantScore = 0
    attempts = 1
    acceptScore = False
    
    firstParticipantThrow = [0, 0]
    while attempts <= 2 and not acceptScore:
        attempts += 1
        
        dice1 = throwDice() if firstParticipantThrow[0] != 4 or participantScore == 0 else 4

        if (participantScore == 0 or participantScore == 4 or firstParticipantThrow[1] != 4):
            dice2 = throwDice()
        else:
            dice2 = 4
        
        firstParticipantThrow[0] = dice1
        firstParticipantThrow[1] = dice2
        
        if (firstParticipantThrow[0] == 4):
            participantScore = firstParticipantThrow[1]
        elif (firstParticipantThrow[1] == 4):
            participantScore = firstParticipantThrow[0]
        
        if opponentScore is None:
            if participantScore > 3:
                acceptScore = True
        else: 
            if secondParticipantEstrategy(participantScore, opponentScore):
                acceptScore = True

    return participantScore

def throwDice():
    return random.randint(1, 6)

def secondParticipantEstrategy(participantScore, opponentScore):
    if (participantScore > opponentScore):
        return True
    elif (participantScore < opponentScore):
        return False
    else:
        match participantScore:
            case 0 | 1 | 2 | 3:
                return False
    return True

def diceGameAnalyzer(numberOfGames):
    firstParticipantName = "Juan"
    secondParticipantName = "Maria"
    firstParticipantVictories = 0
    secondParticipantVictories = 0
    draws = 0
    for i in range(numberOfGames):
        gameChampion = diceGame(firstParticipantName, secondParticipantName)
        if (firstParticipantName == gameChampion):
            firstParticipantVictories += 1
        elif (secondParticipantName == gameChampion):
            secondParticipantVictories += 1
        else:
            draws += 1

    results = [(firstParticipantName, firstParticipantVictories), 
                (secondParticipantName, secondParticipantVictories), 
                ("EMPATE", draws)]
    return results

def printAnalyzer(numberOfGames):
    gameData = diceGameAnalyzer(numberOfGames)
    print(f"*****************Resultados para {numberOfGames}*****************\n")
    
    for i in range(0,3):
        favorableResults = gameData[i][1]
        victoriesPercentage = round(favorableResults * (100/numberOfGames), 2)
        
        if (gameData[i][0] == "EMPATE"):
            print(f"Empataron {favorableResults} ({victoriesPercentage}%) veces")
        else:
            print(f"{gameData[i][0]} gano {favorableResults} ({victoriesPercentage}%) veces")
        
        print(f"Frecuencia: {favorableResults}\nFrecuencia relativa: {favorableResults/numberOfGames}")
        print("-----------------------------------------\n")

printAnalyzer(1000)
printAnalyzer(10000)
printAnalyzer(100000)