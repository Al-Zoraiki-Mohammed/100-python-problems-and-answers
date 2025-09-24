"Task33"

result = dict()

def play(team, player):
    result[team].append(int(input(f'Type team {team} player {player} result: ')))


def print_winners():
    winners = []
    for team, players in result.items():
        print(f'team no: {team}, winner no: {players.index(max(players)) + 1}, socre: {max(players)}')
        winners.append(max(players))
    print('--'*30)
    print(f'The overall score is: {max(winners)} from team: {winners.index(max(winners)) + 1}')
    print('--'*30)


def start_competition(teams, players):
    for team in range(1,teams +1):
        result[team]= []
        for player in range(1, players +1):
            play(team, player)
    

if __name__ == "__main__":
   start_competition(3,4)
   print_winners()
