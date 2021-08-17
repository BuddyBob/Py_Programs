import random
#teams
def createTeams():
    teams = []
    for i in range(128):
        #players
        players = []
        for i in range(10):
            players.append(random.randint(66,104))
        teams.append(players)
    return teams
teams = createTeams()
def simulateGame(teams):
    while True:
        count = 0
        for i in range(0,len(teams),2):
            double = teams[i:i+2]
            Bigger = [max(value) for value in zip(double[0], double[1])]
            teams[count] = Bigger
            count += 1
        teams = teams[:int(len(teams)/2)]
        if len(teams) == 2:
            return teams
doubleTeam = simulateGame(teams)
print('''               -Rosters-
Team1: '''+str(doubleTeam[0])+'''
Team2: '''+str(doubleTeam[1]))
sum1 = sum(doubleTeam[0])
sum2 = sum(doubleTeam[1])
if sum1 > sum2: Winner = 0
else: Winner = 1
print('''-Winner-
'''+str(doubleTeam[Winner]))





