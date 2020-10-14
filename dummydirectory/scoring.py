import numpy as np 

def score_stich(cards, cheated):
  """Distributes the reward and return winner id."""

  cardscopy = np.copy(cards)
  cardscopy[cheated] = -99999999

  winner = cardscopy == np.max(cardscopy)
  # Normalize reward:
  # 1 winner: 1   point
  # 2 winnnr: 1/2 points
  # 3 winner: 1/3 points
  # 4 winner: 1/4 points
  # (but the code should work with n players too)
  points =  winner / np.sum(winner)

  # find out which player won (if multiple winner, pick one)
  winnerid = np.random.permutation(np.argwhere(cardscopy == np.max(cardscopy)))[0]
  return points, winnerid

def score_game(cards):
  """Distributes the points after a full match."""

  winner = cards == np.max(cards)
  # Normalize reward:
  # 1 winner: 3 points
  # 2 winnnr: 2 points
  # 3 winner: 1 point
  # 4 winner: 0 points
  # (but the code should work with n players too)
  return winner*(len(cards)-np.sum(winner))



def did_cheat(history):
  """Determines who of the players has (at any point) cheated."""

  ncards, nplayers = history.shape
  cheated = False * np.ones(nplayers,dtype=bool)

  for i in range(nplayers):
    x = history[:,i]
    x = x[x>-1] # -1 entries are unplayed cards
    if len(np.unique(x)) != len(x): # duplicate cards
      cheated[i] = True
    for xi in x:
      if not xi in np.arange(ncards):
        cheated[i] = True # a card that is not in [0,...,ncards-1]
 
  return cheated
  


