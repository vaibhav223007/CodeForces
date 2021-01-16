number_of_games = int(input())

matches_won = input()

if matches_won.count('A') > matches_won.count('D'):
    print('Anton')
elif matches_won.count('A') < matches_won.count('D'):
    print('Danik')
else:
    print('Friendship')
