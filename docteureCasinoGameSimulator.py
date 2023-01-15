import random as run
deck = []
for i in range(52):
  deck.append(i + 1)
class card:
  suit = ""
  type = ""
  color = ""
  def genCard(self, x):
    self.suit = x % 4
    self.type = x % 13
    self.color = x % 2
def winCheck(card1, card2):
  if(card1.color != card2.color):
    return 2
  elif(card1.suit == card2.suit):
    if(card2.type >= 3):
      return -2
    else:
      return -8
  elif(card1.type != card2.type and card1.color == card2.color and card1.suit != card2.suit):
    return 0
  elif(card1.type == card2.type and card1.color == card2.color and card1.suit != card2.suit):
    return -2
def chooseCard(deck):
  chosen = run.randint(0, 51)
  card1 = card()
  card1.genCard(deck[chosen])
  giveBack = deck.pop(chosen)
  card2 = card()
  card2.genCard(deck[run.randint(0, 50)])
  deck.append(giveBack)
  deck.sort()
  return card1, card2
howMany = int(input("How many tests?: "))
tokens = 0
for y in range(howMany):
  card1, card2 = chooseCard(deck)
  tokens = tokens + winCheck(card1, card2)
print(tokens)
print(tokens / howMany)
while(True):
  noStop = input("")
