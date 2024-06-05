'''
Let's play! You have to return which player won! In case of a draw return Draw!.

Examples(Input1, Input2 --> Output):

"scissors", "paper" --> "Player 1 won!"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!"
'''

def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    if p1 == 'scissors':
        if p2 == 'paper':
            return 'Player 1 won!'
        else:
            return 'Player 2 won!'
    if p1 == 'rock':
        if p2 == 'scissors':
            return 'Player 1 won!'
        else:
            return 'Player 2 won!'
    if p1 == 'paper':
        if p2 == 'rock':
            return 'Player 1 won!'
        else:
            return 'Player 2 won!'

def rps1(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"

def rps2(p1, p2):
    hand = {'rock':0, 'paper':1, 'scissors':2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]


