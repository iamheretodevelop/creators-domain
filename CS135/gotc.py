team1 = {'AI':0, 'MJ':0, 'KD':0, 'TD':0, 'KAJ':0} 
team2 = {'KI':0, 'KB':0, 'LJ':0, 'DN':0, 'HO':0}
team1_names_abbreviations = {'Allen Iverson': 'AI', 'Michael Jordan': 'MJ', 'Kevin Durant': 'KD', 'Tim Duncan': 'TD', 'Kareem Abdul-Jabbar': 'KAJ'}
team2_names_abbreviations = {'Kyrie Irving': 'KI', 'Kobe Bryant': 'KB', 'Lebron James': 'LJ', 'Dirk Nowitzki': 'DN', 'Hakeem Olajuwon': 'HO'}

points = {'Made Layup': 2, 'Missed Layup': -2, 'Made Dunk': 2, 'Missed Dunk': -2, 'Made Free Throw': 1, 'Missed Free Throw': -1, 'Made Mid Range': 2, 'Missed Mid Range': -2, 'Made Three': 3, 'Missed Three': -3, 'Made AND-1': +3}

def formatScore(team1:dict, team2:dict):
    #formatting team1
    final_string_output = f'Team 1 True Score\n'
    for name in team1_names_abbreviations:
        abbreviation = team1_names_abbreviations[name]
        final_string_output += f'{name}: {team1[abbreviation]} points\n'

    team1_max = max(team1.values())
    top_t1_abbreviation = [player for player, points in team1.items() if points == team1_max]
    top_t1 = []
    for name, abbreviation in team1_names_abbreviations.items():
        if abbreviation in top_t1_abbreviation:
            top_t1.append(name)
    team1_top = ','.join(top_t1)
    team1_top += f" {team1_max} points\n"
    team1_total = sum(team1.values())
    final_string_output += f'Team 1 Leading Scorer(s): {team1_top}Team 1 Total Score: {team1_total} points\n\n'

    #formatting team2
    final_string_output += f'Team 2 True Score\n'
    for name in team2_names_abbreviations:
        abbreviation = team2_names_abbreviations[name]
        final_string_output += f'{name}: {team2[abbreviation]} points\n'

    team2_max = max(team2.values())
    top_t2_abbreviation = [player for player, points in team2.items() if points == team2_max]
    top_t2 = []
    for name, abbreviation in team2_names_abbreviations.items():
        if abbreviation in top_t2_abbreviation:
            top_t2.append(name)
    team2_top = ','.join(top_t2)
    team2_top += f" {team2_max} points\n"
    team2_total = sum(team2.values())
    final_string_output += f'Team 2 Leading Scorer(s): {team2_top}Team 2 Total Score: {team2_total} points\n\n'

    #final score
    final_string_output += f'Final Score\n{team1_total} - {team2_total}\n\n'
    #winner
    if team1_total > team2_total:
        final_string_output += f'Winner\nTeam 1 by {team1_total - team2_total} points' 
    elif team2_total > team1_total:
        final_string_output += f'Winner\nTeam 2 by {team2_total - team1_total} points'
    else:
        final_string_output += f'Winner\nScore is tied at {team1_total} points'

    return final_string_output

def outerFunction(team1:dict, team2:dict):
    def innerFunction(commands:list, finalCommand:bool):
      nonlocal team1, team2
      for command in commands:
        name_and_action = command.split(",")
        name = name_and_action[0]
        action = name_and_action[1]
        add_points = points[action]
        if name in team1:
          team1[name] += add_points
        if name in team2:
          team2[name] += add_points
      if finalCommand:
            return formatScore(team1, team2)
    return innerFunction

