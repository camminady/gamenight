import numpy as np 

def score_stich(cards):
  """Distributes the reward."""

  winner = cards == np.max(cards)
  # Normalize reward:
  # 1 winner: 1   point
  # 2 winnnr: 1/2 points
  # 3 winner: 1/3 points
  # 4 winner: 1/4 points
  # (but the code should work with n players too)
  return winner / np.sum(winner)

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



def did_cheat(history,ncards):
  """Determines who of the players has cheated."""
  
  turns, nplayers = history.shape
  cheated = False* np.ones(nplayers,dtype=bool)
  for i in range(nplayers):
    x = history[:,i]
    if len(np.unique(x)) != len(x):
      cheated[i] = True
    for xi in x:
      if not xi in np.arange(ncards):
        cheated[i] = True # a card that is not in [0,...,ncards-1]
 
  return cheated
  


