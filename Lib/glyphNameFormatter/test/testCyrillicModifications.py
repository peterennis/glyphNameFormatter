from glyphNameFormatter import GlyphName

## simple test agians Ilya's corrections

path = "./../data/Erik_Cyrillic_Names_marks.txt"

f = open(path, "r")
lines = f.readlines()
f.close()

for line in lines:
    line =  line.strip()
    if not line:
        continue
    parts = [p for p in line.split("\t") if p]
    parts = line.split("\t")


    correctName = parts[2]
    uni = parts[3]
    if not uni:
        uni = parts[4]
    uni = int(uni, 16)

    g = GlyphName(uniNumber=uni)
    n = g.getName()
    if n != correctName:
        n = g.getName(extension=False)
        if n != correctName:
            print n.ljust(30), correctName.ljust(20), "%04X" % uni
