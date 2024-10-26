import os

files = os.listdir("PATH/TO/MUSIC/FILES/")

for file in files:
    os.system("lame -b 32 PATH/TO/MUSIC/FILES/" + file + " " +  file)
