#CALCULTION OF BATTING POINTS

def calculate_batting_points(player):
    runs = player['runs']
    fours = player['4']
    sixes = player['6']
    balls = player['balls']

    points = runs // 2
    if runs >= 50:
        points += 5
    if runs >= 100:
        points += 10
    strike_rate = (runs / balls) * 100
    if 80 <= strike_rate <= 100:
        points += 2
    if strike_rate > 100:
        points += 4
    points += fours
    points += 2 * sixes

    return points


#CALCULTION OF BOWLING POINTS
        
def calculate_bowling_points(player):
    wickets = player['wkts']
    overs = player['overs']
    runs_conceded = player['runs']

    points = wickets * 10
    if wickets >= 3:
        points += 5
    if wickets >= 5:
        points += 10

    economy_rate = runs_conceded / overs
    if 3.5 <= economy_rate <= 4.5:
        points += 4
    if 2 <= economy_rate < 3.5:
        points += 7
    if economy_rate < 2:
        points += 10

    return points


#CALCULTION OF FILEDING POINTS

def calcultion_for_feilding(player):
    field= player['field']
    points= field*10
    return points

##CALCULTION OF TOTAL POINTS:


def calculate_total_points_for_each_player(player):
    batting_points= calculate_batting_points(player) if player['role'] == 'bat' else 0
    bowling_points= calculate_bowling_points(player) if player['role'] == 'bowl' else 0
    Total_points=batting_points+bowling_points
    return Total_points


#CALCULTION OF HIGHEST POINTS

def find_man_of_the_match(players):
    max_points = 0
    man_of_the_match = None
    for player in players:
        total_points = calculate_total_points_for_each_player(player)
        if total_points > max_points:
            max_points = total_points
            man_of_the_match = player['name']
    return man_of_the_match

 
 
 # Data for players
players = [
    {'name': 'Virat Kohli', 'role': 'bat', 'runs': 112, '4': 10, '6': 0, 'balls': 119, 'field': 0},
    {'name': 'du Plessis', 'role': 'bat', 'runs': 120, '4': 11, '6': 2, 'balls': 112, 'field': 0},
    {'name': 'Bhuvneshwar Kumar', 'role': 'bowl', 'wkts': 1, 'overs': 10, 'runs': 71, 'field': 1},
    {'name': 'Yuzvendra Chahal', 'role': 'bowl', 'wkts': 2, 'overs': 10, 'runs': 45, 'field': 0},
    {'name': 'Kuldeep Yadav', 'role': 'bowl', 'wkts': 3, 'overs': 10, 'runs': 34, 'field': 0}
]

# Find Man of the Match
man_of_the_match = find_man_of_the_match(players)
print('Man of the Match: {}'.format (find_man_of_the_match(players)))

 
 
 