from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()

for i in range(20):
    mc.setBlock(x+1,y+1,z+1,1)