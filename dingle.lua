function __Playernew (x,y)
local Player = {}
Player.x = x
Player.y = y
function Player:getx ()
return(Player.x)
end
return(Player)
end
player = __Playernew(5,0)
print(player:getx())
