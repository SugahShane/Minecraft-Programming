from mcpi.minecraft import Minecraft

mc = Minecraft.create()
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
width = 10
height = 90
length = 10
blockType = 17
air = 0


for i in range(width):
    for j in range(length):
        for k in range(height):
            if k == height - 1 or j == 0 or j == length - 1 or i == 0 or i == width - 1:
                mc.setBlock(x+i, y+k, z+j, blockType)

#mc.setBlocks(x, y, z, x + width, y + height, z + length, blockType)
