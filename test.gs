class Player(x,y) {

  Player.x = x
  Player.y = y
  def Player:getx() {

    return (Player.x)

  }

  return (Player)

}
player = new Player(5,0)
print(player:getx())
