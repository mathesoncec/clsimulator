import random, time

line = ("-" * 64)

#Initialize classes
class Team:
    def __init__(self, team, rating, country):
        self.team = team
        self.rating = rating
        self.country = country
        self.played = 0
        self.won = 0
        self.drew = 0
        self.lost = 0
        self.goalsfor = 0
        self.goalsagainst = 0
        self.goaldifference = 0
        self.points = 0

team_data = [
    ('Bayern Munich', 1, 'GER'), ('Manchester United', 2, 'ENG'),
    ('FC Copenhagen', 5, 'DEN'), ('Galatasaray', 4, 'TUR'),
    ('Sevilla', 2, 'ESP'), ('Arsenal', 2, 'ENG'),
    ('PSV Eindhoven', 4, 'NED'), ('RC Lens', 4, 'FRA'),
    ('SSC Napoli', 2, 'ITA'), ('Real Madrid', 1, 'ESP'),
    ('SC Braga', 4, 'POR'), ('Union Berlin', 5, 'GER'),
    ('Benfica', 3, 'POR'), ('Inter Milan', 2, 'ITA'),
    ('FC Salzburg', 5, 'AUT'), ('Real Sociedad', 3, 'ESP'),
    ('Feyenoord', 3, 'NED'), ('Atletico Madrid', 2, 'ESP'),
    ('S.S. Lazio', 4, 'ITA'), ("Celtic", 5, 'SCO'),
    ('Paris Saint-Germain', 1, 'FRA'), ('Borussia Dortmund', 2, 'GER'),
    ('AC Milan', 2, 'ITA'), ("Newcastle United", 3, 'ENG'),
    ('Manchester City', 1, 'ENG'), ('RB Leipzig', 3, 'GER'),
    ('FC Crvena Zvezda', 5, 'SER'), ('BSC Young Boys', 5, 'SUI'),
    ('FC Barcelona', 2, 'ESP'), ('FC Porto', 3, 'POR'),
    ('Shakhtar Donetsk', 4, 'UKR'), ('Royal Antwerp', 5, 'BEL')
]

teams = [Team(*data) for data in team_data]

#Select score variables
BLUE = [0, 1, 1, 2, 3, 4]
RED = [0, 1, 1, 2, 2, 3]
BLACK = [0, 0, 2, 2, 2, 3]
GREY = [0, 0, 1, 1, 2, 3]
BROWN = [0, 1, 1, 2, 4, 5]
YELLOW = [0, 0, 1, 1, 1, 2]
GREEN = [0, 1, 2, 3, 4, 5]

groupA = [teams[0], teams[1], teams[2], teams[3]]
groupB = [teams[4], teams[5], teams[6], teams[7]]
groupC = [teams[8], teams[9], teams[10], teams[11]]
groupD = [teams[12], teams[13], teams[14], teams[15]]
groupE = [teams[16], teams[17], teams[18], teams[19]]
groupF = [teams[20], teams[21], teams[22], teams[23]]
groupG = [teams[24], teams[25], teams[26], teams[27]]
groupH = [teams[28], teams[29], teams[30], teams[31]]


def start_game():
        print(line)
        print("CHAMPIONS LEAGUE SIMULATOR 23/24")
        print(line)
        time.sleep(2)
        print("""
Hello there and welcome to the Champions League Simulator 23/24! 
This little program I came up with simulates all the rounds of 
the 2023/24 Champions League, from the groups to the knockouts.
I have tried to make it as realistic as possible, the results 
between the teams, so a team like Real Madrid and Manchester 
City are more likely to have an advantage over smaller teams.
But as in the real Champions League, there might be some 
surprises. I hope you enjoy the program!""")
        print(line)
        time.sleep(2)
        input("\n Press any key to begin the simulation: ")
        print("\n")

def group_table(group, group_name):
        time.sleep(1)
    
        sorted_teams = sorted(group, key=lambda team: (-team.points, -team.goaldifference))

        print("{:<20} {:<3} {:<3} {:<3} {:<3} {:<3} {:<3} {:<4} {:<4}".format(group_name, "P", "W", "D", "L", "F", "A", "GD", "PTS"))
        print(line)
        for team in sorted_teams:
                print("{:<20} {:<3} {:<3} {:<3} {:<3} {:<3} {:<3} {:<4} {:<4}".format(
                team.team, team.played, team.won, team.drew, team.lost, team.goalsfor, team.goalsagainst, team.goaldifference, team.points))
        print("\n")

def show_groups():
        print("Standings")
        print(line)
        group_table(groupA, "Group A")
        group_table(groupB, "Group B")
        group_table(groupC, "Group C")
        group_table(groupD, "Group D")
        group_table(groupE, "Group E")
        group_table(groupF, "Group F")
        group_table(groupG, "Group G")
        group_table(groupH, "Group H")
        input("Press any key to continue: ")
        print("\n")
        

def matchday_one():
    time.sleep(1)
    matches = []
    print("\nMatchday 1: Tuesday 19th September 2023")
    print(line)
    print("Group F: " + groupF[2].team + " (" + groupF[2].country + ") vs " + groupF[3].team + " (" + groupF[3].country + ") (17:45)")
    print("Group G: " + groupG[3].team + " (" + groupG[3].country + ") vs " + groupG[1].team + " (" + groupG[1].country + ") (17:45)")
    print("Group E: " + groupE[0].team + " (" + groupE[0].country + ") vs " + groupE[3].team + " (" + groupE[3].country + ") (20:00)")
    print("Group E: " + groupE[2].team + " (" + groupE[2].country + ") vs " + groupE[1].team + " (" + groupE[1].country + ") (20:00)")
    print("Group F: " + groupF[0].team + " (" + groupF[0].country + ") vs " + groupF[1].team + " (" + groupF[1].country + ") (20:00)")
    print("Group G: " + groupG[0].team + " (" + groupG[0].country + ") vs " + groupG[2].team + " (" + groupG[2].country + ") (20:00)")
    print("Group H: " + groupH[0].team + " (" + groupH[0].country + ") vs " + groupH[3].team + " (" + groupH[3].country + ") (20:00)")
    print("Group H: " + groupH[2].team + " (" + groupH[2].country + ") vs " + groupH[1].team + " (" + groupH[1].country + ") (20:00)")
    matches.append(groupF[2])
    matches.append(groupF[3])
    matches.append(groupG[3])
    matches.append(groupG[1])
    matches.append(groupE[0])
    matches.append(groupE[3])
    matches.append(groupE[2])
    matches.append(groupE[1])
    matches.append(groupF[0])
    matches.append(groupF[1])
    matches.append(groupG[0])
    matches.append(groupG[2])
    matches.append(groupH[0])
    matches.append(groupH[3])
    matches.append(groupH[2])
    matches.append(groupH[1])



    time.sleep(1)
    print("\nMatchday 1: Wednesday 20th September 2023")
    print(line)
    time.sleep(1)
    print("Group A: " + groupA[2].team + " (" + groupA[2].country + ") vs " + groupA[3].team + " (" + groupA[3].country + ") (17:45)")
    print("Group C: " + groupC[1].team + " (" + groupC[1].country + ") vs " + groupC[3].team + " (" + groupC[3].country + ") (17:45)")
    print("Group A: " + groupA[0].team + " (" + groupA[0].country + ") vs " + groupA[1].team + " (" + groupA[1].country + ") (20:00)")
    print("Group B: " + groupB[1].team + " (" + groupB[1].country + ") vs " + groupA[2].team + " (" + groupA[2].country + ") (20:00)")
    print("Group B: " + groupB[0].team + " (" + groupB[0].country + ") vs " + groupB[3].team + " (" + groupB[3].country + ") (20:00)")
    print("Group C: " + groupC[2].team + " (" + groupC[2].country + ") vs " + groupC[0].team + " (" + groupC[0].country + ") (20:00)")
    print("Group D: " + groupD[0].team + " (" + groupD[0].country + ") vs " + groupD[2].team + " (" + groupD[2].country + ") (20:00)")
    print("Group D: " + groupD[3].team + " (" + groupD[3].country + ") vs " + groupD[1].team + " (" + groupD[1].country + ") (20:00)")
    matches.append(groupA[2])
    matches.append(groupA[3])
    matches.append(groupC[1])
    matches.append(groupC[3])
    matches.append(groupA[0])
    matches.append(groupA[1])
    matches.append(groupB[1])
    matches.append(groupB[2])
    matches.append(groupB[0])
    matches.append(groupB[3])
    matches.append(groupC[2])
    matches.append(groupC[0])
    matches.append(groupD[0])
    matches.append(groupD[2])
    matches.append(groupD[3])
    matches.append(groupD[1])

    return matches

def matchday_two():
    time.sleep(1)
    matches = []
    print("\nMatchday 2: Tuesday 3rd October 2023")
    print(line)
    print("Group C: " + groupC[3].team + " (" + groupC[3].country + ") vs " + groupC[2].team + " (" + groupC[2].country + ") (17:45)")
    print("Group D: " + groupD[2].team + " (" + groupD[2].country + ") vs " + groupD[3].team + " (" + groupD[3].country + ") (17:45)")
    print("Group A: " + groupA[1].team + " (" + groupA[1].country + ") vs " + groupA[3].team + " (" + groupA[3].country + ") (20:00)")
    print("Group A: " + groupA[2].team + " (" + groupA[2].country + ") vs " + groupA[0].team + " (" + groupA[0].country + ") (20:00)")
    print("Group B: " + groupB[3].team + " (" + groupB[3].country + ") vs " + groupB[1].team + " (" + groupB[1].country + ") (20:00)")
    print("Group B: " + groupB[2].team + " (" + groupB[2].country + ") vs " + groupB[0].team + " (" + groupB[0].country + ") (20:00)")
    print("Group C: " + groupC[0].team + " (" + groupC[0].country + ") vs " + groupC[1].team + " (" + groupC[1].country + ") (20:00)")
    print("Group D: " + groupD[1].team + " (" + groupD[1].country + ") vs " + groupD[0].team + " (" + groupD[0].country + ") (20:00)")
    matches.append(groupC[3])
    matches.append(groupC[2])
    matches.append(groupD[2])
    matches.append(groupD[3])
    matches.append(groupA[1])
    matches.append(groupA[3])
    matches.append(groupA[2])
    matches.append(groupA[0])
    matches.append(groupB[3])
    matches.append(groupB[1])
    matches.append(groupB[2])
    matches.append(groupB[0])
    matches.append(groupC[0])
    matches.append(groupC[1])
    matches.append(groupD[1])
    matches.append(groupD[0])



    time.sleep(1)
    print("\nMatchday 2: Wednesday 4th October 2023")
    print(line)
    time.sleep(1)
    print("Group E: " + groupE[1].team + " (" + groupE[1].country + ") vs " + groupE[0].team + " (" + groupE[0].country + ") (17:45)")
    print("Group H: " + groupH[3].team + " (" + groupH[3].country + ") vs " + groupH[2].team + " (" + groupH[2].country + ") (17:45)")
    print("Group E: " + groupE[3].team + " (" + groupE[3].country + ") vs " + groupE[2].team + " (" + groupE[2].country + ") (20:00)")
    print("Group F: " + groupF[1].team + " (" + groupF[1].country + ") vs " + groupF[2].team + " (" + groupF[2].country + ") (20:00)")
    print("Group F: " + groupF[3].team + " (" + groupF[3].country + ") vs " + groupF[0].team + " (" + groupF[0].country + ") (20:00)")
    print("Group G: " + groupG[1].team + " (" + groupG[1].country + ") vs " + groupG[0].team + " (" + groupG[0].country + ") (20:00)")
    print("Group G: " + groupG[2].team + " (" + groupG[2].country + ") vs " + groupG[3].team + " (" + groupG[3].country + ") (20:00)")
    print("Group H: " + groupH[1].team + " (" + groupH[1].country + ") vs " + groupH[0].team + " (" + groupH[0].country + ") (20:00)")
    matches.append(groupE[1])
    matches.append(groupE[0])
    matches.append(groupH[3])
    matches.append(groupH[2])
    matches.append(groupE[3])
    matches.append(groupE[2])
    matches.append(groupF[1])
    matches.append(groupF[2])
    matches.append(groupF[3])
    matches.append(groupF[0])
    matches.append(groupG[1])
    matches.append(groupG[0])
    matches.append(groupG[2])
    matches.append(groupG[3])
    matches.append(groupH[1])
    matches.append(groupH[0])

    return matches

def matchday_three():
    time.sleep(1)
    matches = []
    print("\nMatchday 3: Tuesday 24th October 2023")
    print(line)
    print("Group A: " + groupA[3].team + " (" + groupA[3].country + ") vs " + groupA[0].team + " (" + groupA[0].country + ") (17:45)")
    print("Group D: " + groupD[1].team + " (" + groupD[1].country + ") vs " + groupD[2].team + " (" + groupD[2].country + ") (17:45)")
    print("Group A: " + groupA[1].team + " (" + groupA[1].country + ") vs " + groupA[2].team + " (" + groupA[2].country + ") (20:00)")
    print("Group B: " + groupB[0].team + " (" + groupB[0].country + ") vs " + groupB[1].team + " (" + groupB[1].country + ") (20:00)")
    print("Group B: " + groupB[3].team + " (" + groupB[3].country + ") vs " + groupB[2].team + " (" + groupB[2].country + ") (20:00)")
    print("Group C: " + groupC[2].team + " (" + groupC[2].country + ") vs " + groupC[1].team + " (" + groupC[1].country + ") (20:00)")
    print("Group C: " + groupC[3].team + " (" + groupC[3].country + ") vs " + groupC[0].team + " (" + groupC[0].country + ") (20:00)")
    print("Group D: " + groupD[0].team + " (" + groupD[0].country + ") vs " + groupD[3].team + " (" + groupD[3].country + ") (20:00)")
    matches.append(groupA[3])
    matches.append(groupA[0])
    matches.append(groupD[1])
    matches.append(groupD[2])
    matches.append(groupA[1])
    matches.append(groupA[2])
    matches.append(groupB[0])
    matches.append(groupB[1])
    matches.append(groupB[3])
    matches.append(groupB[2])
    matches.append(groupC[2])
    matches.append(groupC[1])
    matches.append(groupC[3])
    matches.append(groupC[0])
    matches.append(groupD[0])
    matches.append(groupD[3])



    time.sleep(1)
    print("\nMatchday 3: Wednesday 25th October 2023")
    print(line)
    time.sleep(1)
    print("Group E: " + groupE[0].team + " (" + groupE[0].country + ") vs " + groupE[2].team + " (" + groupE[2].country + ") (17:45)")
    print("Group H: " + groupH[0].team + " (" + groupH[0].country + ") vs " + groupH[2].team + " (" + groupH[2].country + ") (17:45)")
    print("Group E: " + groupE[3].team + " (" + groupE[3].country + ") vs " + groupE[1].team + " (" + groupE[1].country + ") (20:00)")
    print("Group F: " + groupF[0].team + " (" + groupF[0].country + ") vs " + groupF[2].team + " (" + groupF[2].country + ") (20:00)")
    print("Group F: " + groupF[3].team + " (" + groupF[3].country + ") vs " + groupF[1].team + " (" + groupF[1].country + ") (20:00)")
    print("Group G: " + groupG[1].team + " (" + groupG[1].country + ") vs " + groupG[2].team + " (" + groupG[2].country + ") (20:00)")
    print("Group G: " + groupG[3].team + " (" + groupG[3].country + ") vs " + groupG[0].team + " (" + groupG[0].country + ") (20:00)")
    print("Group H: " + groupH[3].team + " (" + groupH[3].country + ") vs " + groupH[1].team + " (" + groupH[1].country + ") (20:00)")
    matches.append(groupE[0])
    matches.append(groupE[2])
    matches.append(groupH[0])
    matches.append(groupH[2])
    matches.append(groupE[3])
    matches.append(groupE[1])
    matches.append(groupF[0])
    matches.append(groupF[2])
    matches.append(groupF[3])
    matches.append(groupF[1])
    matches.append(groupG[1])
    matches.append(groupG[2])
    matches.append(groupG[3])
    matches.append(groupG[0])
    matches.append(groupH[3])
    matches.append(groupH[1])

    return matches

def matchday_four():
    
    time.sleep(1)
    matches = []
    print("\nMatchday 4: Tuesday 7th November 2023")
    print(line)
    time.sleep(1)
    print("Group F: " + groupF[1].team + " (" + groupF[1].country + ") vs " + groupF[3].team + " (" + groupF[3].country + ") (17:45)")
    print("Group H: " + groupH[2].team + " (" + groupH[2].country + ") vs " + groupH[0].team + " (" + groupH[0].country + ") (17:45)")
    print("Group E: " + groupE[1].team + " (" + groupE[1].country + ") vs " + groupE[3].team + " (" + groupE[3].country + ") (20:00)")
    print("Group E: " + groupE[2].team + " (" + groupE[2].country + ") vs " + groupE[0].team + " (" + groupE[0].country + ") (20:00)")
    print("Group F: " + groupF[2].team + " (" + groupF[2].country + ") vs " + groupF[0].team + " (" + groupF[0].country + ") (20:00)")
    print("Group G: " + groupG[0].team + " (" + groupG[0].country + ") vs " + groupG[3].team + " (" + groupG[3].country + ") (20:00)")
    print("Group G: " + groupG[2].team + " (" + groupG[2].country + ") vs " + groupG[1].team + " (" + groupG[1].country + ") (20:00)")
    print("Group H: " + groupH[1].team + " (" + groupH[1].country + ") vs " + groupH[3].team + " (" + groupH[3].country + ") (20:00)")
    matches.append(groupF[1])
    matches.append(groupF[3])
    matches.append(groupH[2])
    matches.append(groupH[0])
    matches.append(groupE[1])
    matches.append(groupE[3])
    matches.append(groupE[2])
    matches.append(groupE[0])
    matches.append(groupF[2])
    matches.append(groupF[0])
    matches.append(groupG[0])
    matches.append(groupG[3])
    matches.append(groupG[2])
    matches.append(groupG[1])
    matches.append(groupH[1])
    matches.append(groupH[3])

    time.sleep(1)
    print("\nMatchday 4: Wednesday 8th November 2023")
    print(line)
    print("Group C: " + groupC[0].team + " (" + groupC[0].country + ") vs " + groupC[3].team + " (" + groupC[3].country + ") (17:45)")
    print("Group D: " + groupD[3].team + " (" + groupD[3].country + ") vs " + groupD[0].team + " (" + groupD[0].country + ") (17:45)")
    print("Group A: " + groupA[0].team + " (" + groupA[0].country + ") vs " + groupA[3].team + " (" + groupA[3].country + ") (20:00)")
    print("Group A: " + groupA[2].team + " (" + groupA[2].country + ") vs " + groupA[1].team + " (" + groupA[1].country + ") (20:00)")
    print("Group B: " + groupB[1].team + " (" + groupB[1].country + ") vs " + groupB[0].team + " (" + groupB[0].country + ") (20:00)")
    print("Group B: " + groupB[2].team + " (" + groupB[2].country + ") vs " + groupB[3].team + " (" + groupB[3].country + ") (20:00)")
    print("Group C: " + groupC[1].team + " (" + groupC[1].country + ") vs " + groupC[2].team + " (" + groupC[2].country + ") (20:00)")
    print("Group D: " + groupD[2].team + " (" + groupD[2].country + ") vs " + groupD[1].team + " (" + groupD[1].country + ") (20:00)")
    matches.append(groupC[0])
    matches.append(groupC[3])
    matches.append(groupD[3])
    matches.append(groupD[0])
    matches.append(groupA[0])
    matches.append(groupA[3])
    matches.append(groupA[2])
    matches.append(groupA[1])
    matches.append(groupB[1])
    matches.append(groupB[0])
    matches.append(groupB[2])
    matches.append(groupB[3])
    matches.append(groupC[1])
    matches.append(groupC[2])
    matches.append(groupD[2])
    matches.append(groupD[1])
       
    return matches

def matchday_five():
    time.sleep(1)
    matches = []
    print("\nMatchday 5: Tuesday 28th November 2023")
    print(line)
    time.sleep(1)
    print("Group E: " + groupE[2].team + " (" + groupE[2].country + ") vs " + groupE[3].team + " (" + groupE[3].country + ") (17:45)")
    print("Group H: " + groupH[2].team + " (" + groupH[2].country + ") vs " + groupH[3].team + " (" + groupH[3].country + ") (17:45)")
    print("Group E: " + groupE[0].team + " (" + groupE[0].country + ") vs " + groupE[1].team + " (" + groupE[1].country + ") (20:00)")
    print("Group F: " + groupF[0].team + " (" + groupF[0].country + ") vs " + groupF[3].team + " (" + groupF[3].country + ") (20:00)")
    print("Group F: " + groupF[2].team + " (" + groupF[2].country + ") vs " + groupF[1].team + " (" + groupF[1].country + ") (20:00)")
    print("Group G: " + groupG[0].team + " (" + groupG[0].country + ") vs " + groupG[1].team + " (" + groupG[1].country + ") (20:00)")
    print("Group G: " + groupG[3].team + " (" + groupG[3].country + ") vs " + groupG[2].team + " (" + groupG[2].country + ") (20:00)")
    print("Group H: " + groupH[0].team + " (" + groupH[0].country + ") vs " + groupH[1].team + " (" + groupH[1].country + ") (20:00)")
    matches.append(groupE[2])
    matches.append(groupE[3])
    matches.append(groupH[2])
    matches.append(groupH[3])
    matches.append(groupE[0])
    matches.append(groupE[1])
    matches.append(groupF[0])
    matches.append(groupF[3])
    matches.append(groupF[2])
    matches.append(groupF[1])
    matches.append(groupG[0])
    matches.append(groupG[1])
    matches.append(groupG[3])
    matches.append(groupG[2])
    matches.append(groupH[0])
    matches.append(groupH[1])

    time.sleep(1)
    print("\nMatchday 5: Wednesday 29th November 2023")
    print(line)
    print("Group A: " + groupA[3].team + " (" + groupA[3].country + ") vs " + groupA[1].team + " (" + groupA[1].country + ") (17:45)")
    print("Group B: " + groupB[0].team + " (" + groupB[0].country + ") vs " + groupB[2].team + " (" + groupB[2].country + ") (17:45)")
    print("Group A: " + groupA[0].team + " (" + groupA[0].country + ") vs " + groupA[2].team + " (" + groupA[2].country + ") (20:00)")
    print("Group B: " + groupB[1].team + " (" + groupB[1].country + ") vs " + groupB[3].team + " (" + groupB[3].country + ") (20:00)")
    print("Group C: " + groupC[1].team + " (" + groupC[1].country + ") vs " + groupC[0].team + " (" + groupC[0].country + ") (20:00)")
    print("Group C: " + groupC[2].team + " (" + groupC[2].country + ") vs " + groupC[3].team + " (" + groupC[3].country + ") (20:00)")
    print("Group D: " + groupD[0].team + " (" + groupD[0].country + ") vs " + groupD[1].team + " (" + groupD[1].country + ") (20:00)")
    print("Group D: " + groupD[3].team + " (" + groupD[3].country + ") vs " + groupD[2].team + " (" + groupD[2].country + ") (20:00)")
    matches.append(groupA[3])
    matches.append(groupA[1])
    matches.append(groupB[0])
    matches.append(groupB[2])
    matches.append(groupA[0])
    matches.append(groupA[2])
    matches.append(groupB[1])
    matches.append(groupB[3])
    matches.append(groupC[1])
    matches.append(groupC[0])
    matches.append(groupC[2])
    matches.append(groupC[3])
    matches.append(groupD[0])
    matches.append(groupD[1])
    matches.append(groupD[3])
    matches.append(groupD[2])
       
    return matches

def matchday_six():
    time.sleep(1)
    matches = []
    print("\nMatchday 6: Tuesday 12th December 2023")
    print(line)
    print("Group B: " + groupB[3].team + " (" + groupB[3].country + ") vs " + groupB[0].team + " (" + groupB[0].country + ") (17:45)")
    print("Group B: " + groupB[2].team + " (" + groupB[2].country + ") vs " + groupB[1].team + " (" + groupB[1].country + ") (17:45)")
    print("Group A: " + groupA[1].team + " (" + groupA[1].country + ") vs " + groupA[0].team + " (" + groupA[0].country + ") (20:00)")
    print("Group A: " + groupA[2].team + " (" + groupA[2].country + ") vs " + groupA[3].team + " (" + groupA[3].country + ") (20:00)")
    print("Group C: " + groupC[0].team + " (" + groupC[0].country + ") vs " + groupC[2].team + " (" + groupC[2].country + ") (20:00)")
    print("Group C: " + groupC[3].team + " (" + groupC[3].country + ") vs " + groupC[1].team + " (" + groupC[1].country + ") (20:00)")
    print("Group D: " + groupD[1].team + " (" + groupD[1].country + ") vs " + groupD[3].team + " (" + groupD[3].country + ") (20:00)")
    print("Group D: " + groupD[2].team + " (" + groupD[2].country + ") vs " + groupD[0].team + " (" + groupD[0].country + ") (20:00)")
    matches.append(groupB[3])
    matches.append(groupB[0])
    matches.append(groupB[2])
    matches.append(groupB[1])
    matches.append(groupA[1])
    matches.append(groupA[0])
    matches.append(groupA[2])
    matches.append(groupA[3])
    matches.append(groupC[0])
    matches.append(groupC[2])
    matches.append(groupC[3])
    matches.append(groupC[1])
    matches.append(groupD[1])
    matches.append(groupD[3])
    matches.append(groupD[2])
    matches.append(groupD[0])

    time.sleep(1)
    print("\nMatchday 6: Wednesday 13th December 2023")
    print(line)
    time.sleep(1)
    print("Group G: " + groupG[1].team + " (" + groupG[1].country + ") vs " + groupG[3].team + " (" + groupG[3].country + ") (17:45)")
    print("Group G: " + groupG[2].team + " (" + groupG[2].country + ") vs " + groupG[0].team + " (" + groupG[0].country + ") (17:45)")
    print("Group E: " + groupE[1].team + " (" + groupE[1].country + ") vs " + groupE[2].team + " (" + groupE[2].country + ") (20:00)")
    print("Group E: " + groupE[3].team + " (" + groupE[3].country + ") vs " + groupE[0].team + " (" + groupE[0].country + ") (20:00)")
    print("Group F: " + groupF[1].team + " (" + groupF[1].country + ") vs " + groupF[0].team + " (" + groupF[0].country + ") (20:00)")
    print("Group F: " + groupF[3].team + " (" + groupF[3].country + ") vs " + groupF[2].team + " (" + groupF[2].country + ") (20:00)")
    print("Group H: " + groupH[1].team + " (" + groupH[1].country + ") vs " + groupH[2].team + " (" + groupH[2].country + ") (20:00)")
    print("Group H: " + groupH[3].team + " (" + groupH[3].country + ") vs " + groupH[0].team + " (" + groupH[0].country + ") (20:00)")
    matches.append(groupG[1])
    matches.append(groupG[3])
    matches.append(groupG[2])
    matches.append(groupG[0])
    matches.append(groupE[1])
    matches.append(groupE[2])
    matches.append(groupE[3])
    matches.append(groupE[0])
    matches.append(groupF[1])
    matches.append(groupF[0])
    matches.append(groupF[3])
    matches.append(groupF[2])
    matches.append(groupH[1])
    matches.append(groupH[2])
    matches.append(groupH[3])
    matches.append(groupH[0])
       
    return matches

def find_group_winners_and_runners_up(group, group_name):
    group_winners = []
    runners_up = []

    sorted_teams = sorted(group, key=lambda team: (-team.points, -team.goaldifference))
    group_winners.append(sorted_teams[0])
    runners_up.append(sorted_teams[1])

    return group_winners, runners_up

def show_group_winners():
    group_winners = []
    runners_up = []

    # Assuming groupA, groupB, etc., are lists of Team objects
    groups = {
        "Group A": groupA,
        "Group B": groupB,
        "Group C": groupC,
        "Group D": groupD,
        "Group E": groupE,
        "Group F": groupF,
        "Group G": groupG,
        "Group H": groupH
    }

    for group_name, group_data in groups.items():
        winners, runners = find_group_winners_and_runners_up(group_data, group_name)
        group_winners.extend(winners)
        runners_up.extend(runners)

    print("Group Winners:")
    print("-----------------------------------------------------------")
    for team in group_winners:
        time.sleep(.5)
        print(f"{team.team} ({team.country})")

    print("\nRunners-up:")
    print("-----------------------------------------------------------")
    for team in runners_up:
        time.sleep(.5)
        print(f"{team.team} ({team.country})")

    input("\nPress any key to continue: ")
    print("\n")

    return group_winners, runners_up

def last16_draw(group_winners, runners_up):
    
    matches = []

    print("Round of 16 Draw")
    print(line)

    while group_winners and runners_up:
        random.shuffle(group_winners)
        random.shuffle(runners_up)
        team1 = runners_up[0]
        team2 = group_winners[0]
        team3 = runners_up[-1]
        team4 = group_winners[-1]

        if team1.country != team2.country and team3.country != team4.country:
            time.sleep(1)
            matches.append(team2)
            matches.append(team1)
            print(f"{team1.team} ({team1.country}) vs {team2.team} ({team2.country})")
            group_winners.remove(team2)
            runners_up.remove(team1)
        else:
            time.sleep(1)

    time.sleep(1)
    
    return matches

def knockoutdraw(winners):
       
        matches = []
        random.shuffle(winners)
        team1 = winners[0]
        team2 = winners[1]

        if len(winners) == 8:
                print("Quarter Final Draw")
                print(line)
        if len(winners) == 4:
                print("Semi Final Draw")
                print(line)
        if len(winners) == 2:
                print("Final")
                print(line)

        while winners:
                time.sleep(1)
                random.shuffle(winners)
                team1 = winners[0]
                team2 = winners[1]
                print(f"{team1.team} ({team1.country}) vs {team2.team} ({team2.country})")
                matches.append(team1)
                matches.append(team2)
                winners.remove(team1)
                winners.remove(team2)
        time.sleep(1)

        return matches

def play_knockout_matches(matches):
        
        firstleg_scores = []
        winners = []
        input("\nPress any key to begin the round: ")
        print("\n")
        time.sleep(2)
        if len(matches) > 2:
                print("Results for First Leg")
                print(line)
                time.sleep(1)
        
                for i in range(0, len(matches), 2):
                        team1 = matches[i+1]
                        team2 = matches[i]
                        if len(matches) == 16:
                                if i == 0:
                                        input("Press any key to continue: ")
                                        print("\n")
                                        print("Fixtures for February 13th, 2024")
                                        print(line)
                                if i == 4:
                                        input("Press any key to continue: ")
                                        print("\n")
                                        print("Fixtures for February 14th, 2024")
                                        print(line)
                                if i == 8:
                                        input("Press any key to continue: ")
                                        print("\n")
                                        print("Fixtures for February 20th, 2024")
                                        print(line)
                                if i == 12:
                                        input("Press any key to continue: ")
                                        print("\n")
                                        print("Fixtures for February 21st, 2024")
                                        print(line)
                        if len(matches) == 8:                
                                if i == 0:
                                        input("Press any key to continue: ")
                                        print("\n")
                                        print("Fixtures for April 9th, 2024")
                                        print(line)
                                if i == 4:
                                        input("Press any key to continue: ")
                                        print("\n")
                                        print("Fixtures for April 10th, 2024")
                                        print(line)
                        if len(matches) == 4:                
                                if i == 0:
                                        input("Press any key to continue: ")
                                        print("\n")
                                        print("Fixtures for April 30th, 2024")
                                        print(line)
                                if i == 2:
                                        input("Press any key to continue: ")
                                        print("\n")
                                        print("Fixtures for May 1st, 2024")
                                        print(line)

                        if team1.rating == 1 and team2.rating == 1:
                                team1_score = (str(random.choice(BLUE)))
                                team2_score = (str(random.choice(RED)))
                        if team1.rating == 1 and team2.rating == 2:
                                team1_score = (str(random.choice(BLUE)))
                                team2_score = (str(random.choice(GREY)))
                        if team1.rating == 1 and team2.rating == 3:
                                team1_score = (str(random.choice(BROWN)))
                                team2_score = (str(random.choice(YELLOW)))
                        if team1.rating == 1 and team2.rating == 4:
                                team1_score = (str(random.choice(GREEN)))
                                team2_score = (str(random.choice(YELLOW)))
                        if team1.rating == 1 and team2.rating == 5:
                                team1_score = (str(random.choice(GREEN)))
                                team2_score = (str(random.choice(YELLOW)))
                        if team1.rating == 2 and team2.rating == 1:
                                team1_score = (str(random.choice(BLACK)))
                                team2_score = (str(random.choice(BLACK)))
                        if team1.rating == 2 and team2.rating == 2:
                                team1_score = (str(random.choice(BLUE)))
                                team2_score = (str(random.choice(RED)))
                        if team1.rating == 2 and team2.rating == 3:
                                team1_score = (str(random.choice(BLUE)))
                                team2_score = (str(random.choice(GREY)))
                        if team1.rating == 2 and team2.rating == 4:
                                team1_score = (str(random.choice(BROWN)))
                                team2_score = (str(random.choice(YELLOW)))
                        if team1.rating == 2 and team2.rating == 5:
                                team1_score = (str(random.choice(GREEN)))
                                team2_score = (str(random.choice(YELLOW)))
                        if team1.rating == 3 and team2.rating == 1:
                                team1_score = (str(random.choice(RED)))
                                team2_score = (str(random.choice(BLUE)))
                        if team1.rating == 3 and team2.rating == 2:
                                team1_score = (str(random.choice(BLACK)))
                                team2_score = (str(random.choice(BLACK)))
                        if team1.rating == 3 and team2.rating == 3:
                                team1_score = (str(random.choice(BLUE)))
                                team2_score = (str(random.choice(RED)))
                        if team1.rating == 3 and team2.rating == 4:
                                team1_score = (str(random.choice(BLUE)))
                                team2_score = (str(random.choice(GREY)))
                        if team1.rating == 3 and team2.rating == 5:
                                team1_score = (str(random.choice(BROWN)))
                                team2_score = (str(random.choice(YELLOW)))
                        if team1.rating == 4 and team2.rating == 1:
                                team1_score = (str(random.choice(GREY)))
                                team2_score = (str(random.choice(BLUE)))
                        if team1.rating == 4 and team2.rating == 2:
                                team1_score = (str(random.choice(RED)))
                                team2_score = (str(random.choice(BLUE)))
                        if team1.rating == 4 and team2.rating == 3:
                                team1_score = (str(random.choice(BLACK)))
                                team2_score = (str(random.choice(BLACK)))
                        if team1.rating == 4 and team2.rating == 4:
                                team1_score = (str(random.choice(BLUE)))
                                team2_score = (str(random.choice(RED)))
                        if team1.rating == 4 and team2.rating == 5:
                                team1_score = (str(random.choice(BLUE)))
                                team2_score = (str(random.choice(GREY)))
                        if team1.rating == 5 and team2.rating == 1:
                                team1_score = (str(random.choice(YELLOW)))
                                team2_score = (str(random.choice(BROWN)))
                        if team1.rating == 5 and team2.rating == 2:
                                team1_score = (str(random.choice(GREY)))
                                team2_score = (str(random.choice(BLUE)))
                        if team1.rating == 5 and team2.rating == 3:
                                team1_score = (str(random.choice(RED)))
                                team2_score = (str(random.choice(BLUE)))
                        if team1.rating == 5 and team2.rating == 4:
                                team1_score = (str(random.choice(BLACK)))
                                team2_score = (str(random.choice(BLACK)))
                        if team1.rating == 5 and team2.rating == 5:
                                team1_score = (str(random.choice(YELLOW)))
                                team2_score = (str(random.choice(BROWN)))

                        print(f"{team1.team} ({team1.country}) {team1_score}-{team2_score} {team2.team} ({team2.country})\n")
                        time.sleep(1)
                        firstleg_scores.append(int(team1_score))
                        firstleg_scores.append(int(team2_score))
                input("\nRound complete. Press any key to continue: ")
                print("\n")
                print("Results for Second Leg")
                print(line)

                for i in range(0, len(matches), 2):
                        team1 = matches[i]
                        team2 = matches[i+1]
                       
                        if len(matches) == 16:
                                if i == 0:
                                        input("Press any key to continue: ")
                                        print("\n")
                                        print("Fixtures for March 5th, 2024")
                                        print(line)
                                if i == 4:
                                        input("Press any key to continue: ")
                                        print("\n")
                                        print("Fixtures for March 6th, 2024")
                                        print(line)
                                if i == 8:
                                        input("Press any key to continue: ")
                                        print("\n")
                                        print("Fixtures for March 12th, 2024")
                                        print(line)
                                if i == 12:
                                        input("Press any key to continue: ")
                                        print("\n")
                                        print("Fixtures for March 13th, 2024")
                                        print(line)
                        if len(matches) == 8:                
                                if i == 0:
                                        input("Press any key to continue: ")
                                        print("\n")
                                        print("Fixtures for April 16th, 2024")
                                        print(line)
                                if i == 4:
                                        input("Press any key to continue: ")
                                        print("\n")
                                        print("Fixtures for April 17th, 2024")
                                        print(line)
                        if len(matches) == 4:                
                                if i == 0:
                                        input("Press any key to continue: ")
                                        print("\n")
                                        print("Fixtures for May 7th, 2024")
                                        print(line)
                                if i == 2:
                                        input("Press any key to continue: ")
                                        print("\n")
                                        print("Fixtures for May 8th, 2024")
                                        print(line)


                        if team1.rating == 1 and team2.rating == 1:
                                team1_score = (str(random.choice(BLUE)))
                                team2_score = (str(random.choice(RED)))
                        if team1.rating == 1 and team2.rating == 2:
                                team1_score = (str(random.choice(BLUE)))
                                team2_score = (str(random.choice(GREY)))
                        if team1.rating == 1 and team2.rating == 3:
                                team1_score = (str(random.choice(BROWN)))
                                team2_score = (str(random.choice(YELLOW)))
                        if team1.rating == 1 and team2.rating == 4:
                                team1_score = (str(random.choice(GREEN)))
                                team2_score = (str(random.choice(YELLOW)))
                        if team1.rating == 1 and team2.rating == 5:
                                team1_score = (str(random.choice(GREEN)))
                                team2_score = (str(random.choice(YELLOW)))
                        if team1.rating == 2 and team2.rating == 1:
                                team1_score = (str(random.choice(BLACK)))
                                team2_score = (str(random.choice(BLACK)))
                        if team1.rating == 2 and team2.rating == 2:
                                team1_score = (str(random.choice(BLUE)))
                                team2_score = (str(random.choice(RED)))
                        if team1.rating == 2 and team2.rating == 3:
                                team1_score = (str(random.choice(BLUE)))
                                team2_score = (str(random.choice(GREY)))
                        if team1.rating == 2 and team2.rating == 4:
                                team1_score = (str(random.choice(BROWN)))
                                team2_score = (str(random.choice(YELLOW)))
                        if team1.rating == 2 and team2.rating == 5:
                                team1_score = (str(random.choice(GREEN)))
                                team2_score = (str(random.choice(YELLOW)))
                        if team1.rating == 3 and team2.rating == 1:
                                team1_score = (str(random.choice(RED)))
                                team2_score = (str(random.choice(BLUE)))
                        if team1.rating == 3 and team2.rating == 2:
                                team1_score = (str(random.choice(BLACK)))
                                team2_score = (str(random.choice(BLACK)))
                        if team1.rating == 3 and team2.rating == 3:
                                team1_score = (str(random.choice(BLUE)))
                                team2_score = (str(random.choice(RED)))
                        if team1.rating == 3 and team2.rating == 4:
                                team1_score = (str(random.choice(BLUE)))
                                team2_score = (str(random.choice(GREY)))
                        if team1.rating == 3 and team2.rating == 5:
                                team1_score = (str(random.choice(BROWN)))
                                team2_score = (str(random.choice(YELLOW)))
                        if team1.rating == 4 and team2.rating == 1:
                                team1_score = (str(random.choice(GREY)))
                                team2_score = (str(random.choice(BLUE)))
                        if team1.rating == 4 and team2.rating == 2:
                                team1_score = (str(random.choice(RED)))
                                team2_score = (str(random.choice(BLUE)))
                        if team1.rating == 4 and team2.rating == 3:
                                team1_score = (str(random.choice(BLACK)))
                                team2_score = (str(random.choice(BLACK)))
                        if team1.rating == 4 and team2.rating == 4:
                                team1_score = (str(random.choice(BLUE)))
                                team2_score = (str(random.choice(RED)))
                        if team1.rating == 4 and team2.rating == 5:
                                team1_score = (str(random.choice(BLUE)))
                                team2_score = (str(random.choice(GREY)))
                        if team1.rating == 5 and team2.rating == 1:
                                team1_score = (str(random.choice(YELLOW)))
                                team2_score = (str(random.choice(BROWN)))
                        if team1.rating == 5 and team2.rating == 2:
                                team1_score = (str(random.choice(GREY)))
                                team2_score = (str(random.choice(BLUE)))
                        if team1.rating == 5 and team2.rating == 3:
                                team1_score = (str(random.choice(RED)))
                                team2_score = (str(random.choice(BLUE)))
                        if team1.rating == 5 and team2.rating == 4:
                                team1_score = (str(random.choice(BLACK)))
                                team2_score = (str(random.choice(BLACK)))
                        if team1.rating == 5 and team2.rating == 5:
                                team1_score = (str(random.choice(YELLOW)))
                                team2_score = (str(random.choice(BROWN)))

                        print(f"{team1.team} ({team1.country}) {team1_score}-{team2_score} {team2.team} ({team2.country})")
                        time.sleep(1)
                        #Get first leg scores
                        first_leg_score_team1 = firstleg_scores[i+1]
                        first_leg_score_team2 = firstleg_scores[i]

                        #Calculate aggregate scores
                        team1.aggscore = first_leg_score_team1 + int(team1_score)
                        team2.aggscore = first_leg_score_team2 + int(team2_score)
                        time.sleep(1)
                        print(f"Agg: {team1.team} ({team1.country}) {team1.aggscore}-{team2.aggscore} {team2.team} ({team2.country})")
                        if team1.aggscore > team2.aggscore:
                                time.sleep(1)
                                print(f"{team1.team} advances!\n")
                                winners.append(team1)
                                time.sleep(2)
                        if team2.aggscore > team1.aggscore:
                                time.sleep(1)
                                print(f"{team2.team} advances!\n")
                                winners.append(team2)
                                time.sleep(2)
                        if team1.aggscore == team2.aggscore:
                                team1_etscore = (str(random.choice(YELLOW)))
                                team2_etscore = (str(random.choice(YELLOW)))
                                team1.aggscore += int(team1_etscore)
                                team2.aggscore += int(team2_etscore)
                                time.sleep(1)
                                print(f"ET: {team1.team} ({team1.country}) {team1.aggscore}-{team2.aggscore} {team2.team} ({team2.country})")
                                if team1.aggscore > team2.aggscore:
                                        time.sleep(1)
                                        print(f"{team1.team} advances!\n")
                                        winners.append(team1)
                                        time.sleep(2)
                                elif team2.aggscore > team1.aggscore:
                                        time.sleep(1)
                                        print(f"{team2.team} advances!\n")
                                        winners.append(team2)
                                        time.sleep(2)
                                else:
                                        team1_penscore = int((str(random.choice(GREEN))))
                                        team2_penscore = int((str(random.choice(GREEN))))
                                        if int(team1_penscore) < 3 and int(team2_penscore) < 3:
                                                team1_penscore = int((str(random.choice(GREEN))))
                                                team2_penscore = int((str(random.choice(GREEN))))
                                        while int(team1_penscore) >= 4 and int(team2_penscore) < 2:
                                                team2_penscore = team2_penscore + int(str(random.choice(GREEN)))
                                        while int(team2_penscore) >= 4 and int(team1_penscore) < 2:
                                                team1_penscore = team1_penscore + int(str(random.choice(GREEN)))

                                        while team1_penscore == team2_penscore:
                                                team1_penscore = int(team1_penscore) + int(str(random.choice(YELLOW)))
                                                team2_penscore = int(team2_penscore) + int(str(random.choice(YELLOW)))
                                        time.sleep(1)
                                        print(f"PENS: {team1.team} ({team1.country}) {team1_penscore}-{team2_penscore} {team2.team} ({team2.country})")
                                        if team1_penscore > team2_penscore:
                                                time.sleep(1)
                                                print(f"{team1.team} advances!\n")
                                                winners.append(team1)
                                                time.sleep(2)
                                        else:
                                                time.sleep(1)
                                                print(f"{team2.team} advances!\n")
                                                winners.append(team2)
                                                time.sleep(2)
        if len(matches) == 2:
                for i in range(0, len(matches), 2):
                        team1 = matches[i]
                        team2 = matches[i+1]
                        if i == 0:
                                input("Press any key to continue: ")
                                print("\n")
                                print("FINAL on June 1st, 2024")
                                print(line)
                        if team1.rating == 1 and team2.rating == 1:
                                team1_score = (str(random.choice(BLUE)))
                                team2_score = (str(random.choice(BLUE)))
                                print(team1.team + ": " + team1_score)
                                print(team2.team + ": " + team2_score)
                        if team1.rating == 1 and team2.rating == 2:
                                team1_score = (str(random.choice(BLUE)))
                                team2_score = (str(random.choice(RED)))
                                print(team1.team + ": " + team1_score)
                                print(team2.team + ": " + team2_score)
                        if team1.rating == 1 and team2.rating == 3:
                                team1_score = (str(random.choice(BLUE)))
                                team2_score = (str(random.choice(GREY)))
                                print(team1.team + ": " + team1_score)
                                print(team2.team + ": " + team2_score)
                        if team1.rating == 1 and team2.rating == 4:
                                team1_score = (str(random.choice(RED)))
                                team2_score = (str(random.choice(YELLOW)))
                                print(team1.team + ": " + team1_score)
                                print(team2.team + ": " + team2_score)
                        if team1.rating == 1 and team2.rating == 5:
                                team1_score = (str(random.choice(GREEN)))
                                team2_score = (str(random.choice(YELLOW)))
                                print(team1.team + ": " + team1_score)
                                print(team2.team + ": " + team2_score)
                        if team1.rating == 2 and team2.rating == 1:
                                team1_score = (str(random.choice(RED)))
                                team2_score = (str(random.choice(BLUE)))
                                print(team1.team + ": " + team1_score)
                                print(team2.team + ": " + team2_score)
                        if team1.rating == 2 and team2.rating == 2:
                                team1_score = (str(random.choice(BLUE)))
                                team2_score = (str(random.choice(BLUE)))
                                print(team1.team + ": " + team1_score)
                                print(team2.team + ": " + team2_score)
                        if team1.rating == 2 and team2.rating == 3:
                                team1_score = (str(random.choice(BLUE)))
                                team2_score = (str(random.choice(RED)))
                                print(team1.team + ": " + team1_score)
                                print(team2.team + ": " + team2_score)
                        if team1.rating == 2 and team2.rating == 4:
                                team1_score = (str(random.choice(BLUE)))
                                team2_score = (str(random.choice(GREY)))
                                print(team1.team + ": " + team1_score)
                                print(team2.team + ": " + team2_score)
                        if team1.rating == 2 and team2.rating == 5:
                                team1_score = (str(random.choice(BROWN)))
                                team2_score = (str(random.choice(YELLOW)))
                                print(team1.team + ": " + team1_score)
                                print(team2.team + ": " + team2_score)
                        if team1.rating == 3 and team2.rating == 1:
                                team1_score = (str(random.choice(GREY)))
                                team2_score = (str(random.choice(BLUE)))
                                print(team1.team + ": " + team1_score)
                                print(team2.team + ": " + team2_score)
                        if team1.rating == 3 and team2.rating == 2:
                                team1_score = (str(random.choice(RED)))
                                team2_score = (str(random.choice(BLUE)))
                                print(team1.team + ": " + team1_score)
                                print(team2.team + ": " + team2_score)
                        if team1.rating == 3 and team2.rating == 3:
                                team1_score = (str(random.choice(BLUE)))
                                team2_score = (str(random.choice(BLUE)))
                                print(team1.team + ": " + team1_score)
                                print(team2.team + ": " + team2_score)
                        if team1.rating == 3 and team2.rating == 4:
                                team1_score = (str(random.choice(BLUE)))
                                team2_score = (str(random.choice(RED)))
                                print(team1.team + ": " + team1_score)
                                print(team2.team + ": " + team2_score)
                        if team1.rating == 3 and team2.rating == 5:
                                team1_score = (str(random.choice(BLUE)))
                                team2_score = (str(random.choice(GREY)))
                                print(team1.team + ": " + team1_score)
                                print(team2.team + ": " + team2_score)
                        if team1.rating == 4 and team2.rating == 1:
                                team1_score = (str(random.choice(YELLOW)))
                                team2_score = (str(random.choice(RED)))
                                print(team1.team + ": " + team1_score)
                                print(team2.team + ": " + team2_score)
                        if team1.rating == 4 and team2.rating == 2:
                                team1_score = (str(random.choice(GREY)))
                                team2_score = (str(random.choice(BLUE)))
                                print(team1.team + ": " + team1_score)
                                print(team2.team + ": " + team2_score)
                        if team1.rating == 4 and team2.rating == 3:
                                team1_score = (str(random.choice(RED)))
                                team2_score = (str(random.choice(BLUE)))
                                print(team1.team + ": " + team1_score)
                                print(team2.team + ": " + team2_score)
                        if team1.rating == 4 and team2.rating == 4:
                                team1_score = (str(random.choice(BLUE)))
                                team2_score = (str(random.choice(BLUE)))
                                print(team1.team + ": " + team1_score)
                                print(team2.team + ": " + team2_score)
                        if team1.rating == 4 and team2.rating == 5:
                                team1_score = (str(random.choice(BLUE)))
                                team2_score = (str(random.choice(RED)))
                                print(team1.team + ": " + team1_score)
                                print(team2.team + ": " + team2_score)
                        if team1.rating == 5 and team2.rating == 1:
                                team1_score = (str(random.choice(YELLOW)))
                                team2_score = (str(random.choice(GREEN)))
                                print(team1.team + ": " + team1_score)
                                print(team2.team + ": " + team2_score)
                        if team1.rating == 5 and team2.rating == 2:
                                team1_score = (str(random.choice(YELLOW)))
                                team2_score = (str(random.choice(BROWN)))
                                print(team1.team + ": " + team1_score)
                                print(team2.team + ": " + team2_score)
                        if team1.rating == 5 and team2.rating == 3:
                                team1_score = (str(random.choice(GREY)))
                                team2_score = (str(random.choice(BLUE)))
                                print(team1.team + ": " + team1_score)
                                print(team2.team + ": " + team2_score)
                        if team1.rating == 5 and team2.rating == 4:
                                team1_score = (str(random.choice(RED)))
                                team2_score = (str(random.choice(BLUE)))
                                print(team1.team + ": " + team1_score)
                                print(team2.team + ": " + team2_score)
                        if team1.rating == 5 and team2.rating == 5:
                                team1_score = (str(random.choice(BLUE)))
                                team2_score = (str(random.choice(BLUE)))
                                print(team1.team + ": " + team1_score)
                                print(team2.team + ": " + team2_score)

                        print(f"{team1.team} ({team1.country}) {team1_score}-{team2_score} {team2.team} ({team2.country})")
                        time.sleep(1)

                        if team1_score > team2_score:
                                time.sleep(1)
                                print(f"{team1.team} wins!\n")
                                winners.append(team1)
                        if team2_score > team1_score:
                                time.sleep(2)
                                print(f"{team2.team} wins!\n")
                                winners.append(team2)
                        if team1_score == team2_score:
                                team1_etscore = (str(random.choice(YELLOW)))
                                team2_etscore = (str(random.choice(YELLOW)))
                                team1_score = int(team1_score) + int(team1_etscore)
                                team2_score = int(team2_score) + int(team2_etscore)
                                time.sleep(1)
                                print(f"ET: {team1.team} ({team1.country}) {team1_score}-{team2_score} {team2.team} ({team2.country})")
                                if team1_score > team2_score:
                                        time.sleep(1)
                                        print(f"{team1.team} wins!\n")
                                        winners.append(team1)
                                        time.sleep(2)
                                elif team2_score > team1_score:
                                        time.sleep(1)
                                        print(f"{team2.team} wins!\n")
                                        winners.append(team2)
                                        time.sleep(2)
                                else:
                                        team1_penscore = int((str(random.choice(GREEN))))
                                        team2_penscore = int((str(random.choice(GREEN))))
                                        if int(team1_penscore) < 3 and int(team2_penscore) < 3:
                                                team1_penscore = int((str(random.choice(GREEN))))
                                                team2_penscore = int((str(random.choice(GREEN))))
                                        while int(team1_penscore) >= 4 and int(team2_penscore) < 2:
                                                team2_penscore = team2_penscore + int(str(random.choice(GREEN)))
                                        while int(team2_penscore) >= 4 and int(team1_penscore) < 2:
                                                team1_penscore = team1_penscore + int(str(random.choice(GREEN)))

                                        while team1_penscore == team2_penscore:
                                                team1_penscore = int(team1_penscore) + int(str(random.choice(YELLOW)))
                                                team2_penscore = int(team2_penscore) + int(str(random.choice(YELLOW)))
                                        time.sleep(1)
                                        print(f"PENS: {team1.team} ({team1.country}) {team1_penscore}-{team2_penscore} {team2.team} ({team2.country})")
                                        if team1_penscore > team2_penscore:
                                                time.sleep(1)
                                                print(f"{team1.team} wins!\n")
                                                winners.append(team1)
                                                time.sleep(2)
                                        else:
                                                time.sleep(1)
                                                print(f"{team2.team} wins!\n")
                                                winners.append(team2)
                                                time.sleep(2)
                                
                      

        time.sleep(1)
        print("Round Winners")   
        print(line)
        for team in winners:
                time.sleep(1)
                print(team.team + " (" + team.country + ")")

        time.sleep(1)
        input("\nRound complete. Press any key to continue: ")
        print("\n")

        return winners            

def play_group_matches(matches):
    
    input("\nPress any key to begin the round: ")
    print("\n")
    time.sleep(2)
    print("Results")
    print(line)
    for i in range(0, len(matches), 2):
        team1 = matches[i]
        team2 = matches[i+1]

        if i == 16:
                input("End of Tuesday's games. Press any key to continue: ")
                print("\n")
                print("Results")
                print(line)

        if team1.rating == 1 and team2.rating == 1:
                team1_score = (str(random.choice(BLUE)))
                team2_score = (str(random.choice(RED)))
        if team1.rating == 1 and team2.rating == 2:
                team1_score = (str(random.choice(BLUE)))
                team2_score = (str(random.choice(GREY)))
        if team1.rating == 1 and team2.rating == 3:
                team1_score = (str(random.choice(BROWN)))
                team2_score = (str(random.choice(YELLOW)))
        if team1.rating == 1 and team2.rating == 4:
                team1_score = (str(random.choice(GREEN)))
                team2_score = (str(random.choice(YELLOW)))
        if team1.rating == 1 and team2.rating == 5:
                team1_score = (str(random.choice(GREEN)))
                team2_score = (str(random.choice(YELLOW)))
        if team1.rating == 2 and team2.rating == 1:
                team1_score = (str(random.choice(BLACK)))
                team2_score = (str(random.choice(BLACK)))
        if team1.rating == 2 and team2.rating == 2:
                team1_score = (str(random.choice(BLUE)))
                team2_score = (str(random.choice(RED)))
        if team1.rating == 2 and team2.rating == 3:
                team1_score = (str(random.choice(BLUE)))
                team2_score = (str(random.choice(GREY)))
        if team1.rating == 2 and team2.rating == 4:
                team1_score = (str(random.choice(BROWN)))
                team2_score = (str(random.choice(YELLOW)))
        if team1.rating == 2 and team2.rating == 5:
                team1_score = (str(random.choice(GREEN)))
                team2_score = (str(random.choice(YELLOW)))
        if team1.rating == 3 and team2.rating == 1:
                team1_score = (str(random.choice(RED)))
                team2_score = (str(random.choice(BLUE)))
        if team1.rating == 3 and team2.rating == 2:
                team1_score = (str(random.choice(BLACK)))
                team2_score = (str(random.choice(BLACK)))
        if team1.rating == 3 and team2.rating == 3:
                team1_score = (str(random.choice(BLUE)))
                team2_score = (str(random.choice(RED)))
        if team1.rating == 3 and team2.rating == 4:
                team1_score = (str(random.choice(BLUE)))
                team2_score = (str(random.choice(GREY)))
        if team1.rating == 3 and team2.rating == 5:
                team1_score = (str(random.choice(BROWN)))
                team2_score = (str(random.choice(YELLOW)))
        if team1.rating == 4 and team2.rating == 1:
                team1_score = (str(random.choice(GREY)))
                team2_score = (str(random.choice(BLUE)))
        if team1.rating == 4 and team2.rating == 2:
                team1_score = (str(random.choice(RED)))
                team2_score = (str(random.choice(BLUE)))
        if team1.rating == 4 and team2.rating == 3:
                team1_score = (str(random.choice(BLACK)))
                team2_score = (str(random.choice(BLACK)))
        if team1.rating == 4 and team2.rating == 4:
                team1_score = (str(random.choice(BLUE)))
                team2_score = (str(random.choice(RED)))
        if team1.rating == 4 and team2.rating == 5:
                team1_score = (str(random.choice(BLUE)))
                team2_score = (str(random.choice(GREY)))
        if team1.rating == 5 and team2.rating == 1:
                team1_score = (str(random.choice(YELLOW)))
                team2_score = (str(random.choice(BROWN)))
        if team1.rating == 5 and team2.rating == 2:
                team1_score = (str(random.choice(GREY)))
                team2_score = (str(random.choice(BLUE)))
        if team1.rating == 5 and team2.rating == 3:
                team1_score = (str(random.choice(RED)))
                team2_score = (str(random.choice(BLUE)))
        if team1.rating == 5 and team2.rating == 4:
                team1_score = (str(random.choice(BLACK)))
                team2_score = (str(random.choice(BLACK)))
        if team1.rating == 5 and team2.rating == 5:
                team1_score = (str(random.choice(YELLOW)))
                team2_score = (str(random.choice(BROWN)))

        if team1_score > team2_score:
               print(f"{team1.team} ({team1.country}) {team1_score}-{team2_score} {team2.team} ({team2.country})\n")
               team1.played += 1
               team1.won += 1
               team1.goalsfor += (int(team1_score))
               team1.goalsagainst += (int(team2_score))
               team1.goaldifference = team1.goalsfor - team1.goalsagainst
               team1.points += 3
               team2.played += 1
               team2.lost += 1
               team2.goalsfor += (int(team2_score))
               team2.goalsagainst += (int(team1_score))
               team2.goaldifference = team2.goalsfor - team2.goalsagainst
        elif team2_score > team1_score:
               print(f"{team1.team} ({team1.country}) {team1_score}-{team2_score} {team2.team} ({team2.country})\n")
               team2.played += 1
               team2.won += 1
               team2.goalsfor += (int(team2_score))
               team2.goalsagainst += (int(team1_score))
               team2.goaldifference = team2.goalsfor - team2.goalsagainst
               team2.points += 3
               team1.played += 1
               team1.lost += 1
               team1.goalsfor += (int(team1_score))
               team1.goalsagainst += (int(team2_score))
               team1.goaldifference = team1.goalsfor - team1.goalsagainst
        else:
               print(f"{team1.team} ({team1.country}) {team1_score}-{team2_score} {team2.team} ({team2.country})\n")
               team1.played +=1
               team1.drew += 1
               team1.goalsfor += (int(team1_score))
               team1.goalsagainst += (int(team2_score))
               team1.goaldifference = team1.goalsfor - team1.goalsagainst
               team1.points += 1
               team2.played +=1
               team2.drew += 1
               team2.goalsfor += (int(team2_score))
               team2.goalsagainst += (int(team1_score))
               team2.goaldifference = team2.goalsfor - team2.goalsagainst
               team2.points += 1
        time.sleep(1)

    input("\nRound complete. Press any key to continue: ")
    print("\n")
        
def champions(winners):
        time.sleep(1)
        for team in winners:

                print("""
           ,*.                                    *((,          
      /*/     .*/(                           .**((,   */**(     
    *#.          ,*(                       .*(            *((   
   /(              /(                      /(               #(  
  /(               ##                      ((                #( 
 ((*              ,/,                      /((               ,((
 ((           */*(%                         .%((/,            #(
 (*         (,,%%                              &%,//          ((
 (*       ./*  ,//////*****,,,,,......,,,,***//.  ,(*         ((
 (*       /##%/(((((////******,,,,,......,,,***/*% #(        .##
 (/*       ##(#/(((//((((//**//(*//#####((###(#(####         /# 
  (,        /(#(/((((#((///***//.*//((((((((((/(%#,          *# 
  (*.       .,////***,,,,,,,,##(,,,,*******//(*((*          /(  
   (*     .,,.(,******   *(*##(#/*.,,,,,,,,**/,*((,         ,*  
   //.  ,,**. /(/(((/**.*#((%/((*.,  .,,*/((//,/(/(((,*    /#   
    #(  (%(#((((/*/(*******, *//  *//****((#(//(/((((#/   *#    
    .// /%###########%%#%#/////&(((%%&%#((((((((((((((*   (     
     #/ *%%#######%#%%%#%#////(#(/(#%&&#(((((((/(((#((,  //     
      #( *########%###&&%##////#(((#%&&#(((((((((((##/  /#      
       ##/%%##########%&#/#////(///(%&%#(((((((((((##* (#       
       .#/*###((##%%(##%#/*/*///**//&&%##(((((((((### ##        
        *(((###((((((#(/****////***//(%(#(((#(((#(##/##         
         /(,&(/////(*(((/(///(///(///(((#(((((######(#          
          /#,%////(/(//*/*,**///****,/(((#(((((###*(#           
           /*,(////#,,,,,**********////,,,(&#####*#(            
            *,,%,,,,,,,,,,,*******///,,,,***(###*#(             
             /,,,,,,,,,,,,,,,,,,,,,,,,,,,*****&*#(              
              (,,,,,,,,,,,,,,,,,,,,,,,,,*******%#               
               *,,,,,,,,,,,,,,,,,,,,,,,,,*****&,                
                 *,,,,,,,,,,,,,,,,,,,,,*******                  
                  ,,,,,,,,,,,,,,,,,,,,*******                   
                    ,,,,,,,,,,,,,,,,,,****,                     
                     ,,,,,,,,,,,,,,,,****                       
                      ,*,,/,,.***(/(/***                        
                        ,**,,,,,,,,,*/*                         
                        ,,,***,**///**                          
                       ,****,,,/,(////(                         
                  ,,,./,**/. /(/ ,,,,*/(/,,,                    
              ,,,.....*,**,,.,*/.**,*((#,,,,,*/*,               
             ,,/*,**,.. ,**,,*,*,,/*//((((////((*               
               **//**,,  . .,,/*   ,*,,,,*/((**,                
                     ,*,,,...,,,..,,,****.                       """)

                time.sleep(2)
                print(line)
                print(f"Your Champions League Winners: {team.team}! Congratulations!")
                print(line)
                print("Thanks for playing!")
                time.sleep(5)
                break 

#Main loop

#start_game()
#show_groups()
#matches = matchday_one()
#play_group_matches(matches)
#show_groups()
#matches = matchday_two()
#play_group_matches(matches)
#show_groups()
#matches = matchday_three()
#play_group_matches(matches)
#show_groups()
#matches = matchday_four()
#play_group_matches(matches)
#show_groups()
#matches = matchday_five()
#play_group_matches(matches)
#show_groups()
#matches = matchday_six()
#play_group_matches(matches)
#show_groups()
group_winners, runners_up = show_group_winners()
matches = last16_draw(group_winners, runners_up)
winners = play_knockout_matches(matches)
matches = knockoutdraw(winners)
winners = play_knockout_matches(matches)
matches = knockoutdraw(winners)
winners = play_knockout_matches(matches)
matches = knockoutdraw(winners)
winners = play_knockout_matches(matches)
champions(winners)


