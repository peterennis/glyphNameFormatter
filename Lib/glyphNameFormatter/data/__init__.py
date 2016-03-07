import os

path = os.path.dirname(__file__)

# AGD
unicode2name_AGD = {}
name2unicode_AGD = {}

f = open(os.path.join(path, "AGD_name_uni.txt"), "r")
lines = f.readlines()
f.close()

for line in lines:
    if line:
        name, uni = line.split()
        uni = int(uni, 16)
        unicode2name_AGD[uni] = name
        name2unicode_AGD[name] = uni
