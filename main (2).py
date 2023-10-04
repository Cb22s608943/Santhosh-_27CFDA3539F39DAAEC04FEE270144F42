class player:
  def play(self):
    print('the player is playing cricket')
class batsman(player):
  def play(self):
    print("the batsman is batting")
class bowler(player):
  def play(self):
    print("the bowler is bowling")
#create objects of both batsman and bowler classes
batsman=batsman()
bowler=bowler()
#call the play() method for each object
batsman.play()
bowler.play()


    
    