import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

time.sleep(10)

x = 1023
y = 112
z = 1

mc.player.setTilePos(x, y, z)

time.sleep(5)

x = 124
y = 30
z = 134

mc.player.setTilePos(x, y, z)

time.sleep(5)

x = 102
y = 121
z = 132

mc.player.setTilePos(x, y, z)

