from mcpi.minecraft import Minecraft

mc = Minecraft.create()
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
width = 10
height = 10
length = 10
air = 0


mc.setBlocks(x - width, y, z - length, x + width, y + height, z + length, air)
