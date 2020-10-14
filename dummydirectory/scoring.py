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



