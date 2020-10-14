import numpy as np  
import time

def letsplay(players, ncards, printmode,score_stich, score_game,did_cheat):
  """
  Plays one single match.
  Keyword arguments:
    players      -- an array with the bots
    ncards       -- the number of cards for this match
    printmode    -- whether to print or not  
    score_stich  -- scoring for one stich
    score_game   -- scoring for the whole match
    did_cheat    -- checks whether someone cheated
  Return:
    points       -- the points after the match
  """

  nplayers = len(players)
  stiche = np.zeros(nplayers)
  history = np.empty((0,nplayers))
  for nturn in range(ncards):
    cards = []
    for playerid, player in enumerate(players):
      card = player(nplayers, ncards, nturn, playerid, history)
      cards.append(card)
    cards = np.array(cards)
    history = np.vstack([history,cards])
    
    cheated = did_cheat(history,ncards)
    stich =score_stich(cards, cheated)
    stiche += stich

    if printmode:
      time.sleep(1)
      print(f"\n\n\nIt's turn {nturn}. Up to now, the points are:")
      for playerid,point in enumerate(stiche-stich):
        print("Group {}: {:.3f}".format(playerid,point), end =" ")
      print("\n\nThis turn, the cards played are:")
      for playerid,card in enumerate(cards):
        print("Group {}: {}".format(playerid,int(card)))
      print("\n\nAnd the points rewarded are:")
      for playerid,point in enumerate(stich):
        print("Group {}: {:.3f}".format(playerid,point), end =" ")

  score = score_game(stiche)
  if printmode:
    print("\n\nThe game ended. Final score:")
    for playerid,point in enumerate(stiche):
      print("Group {}: {:.3f}".format(playerid,point), end =" ")
    print("\n\nPoints for this game:")
    for playerid,point in enumerate(score):
      print("Group {}: {:.3f}".format(playerid,point), end =" ")    

  return score, history