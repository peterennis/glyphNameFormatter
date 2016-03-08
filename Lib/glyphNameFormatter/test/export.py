from glyphNameFormatter import GlyphName
from glyphNameFormatter.unicodeRangeNames import getAllRangeNames, getRangeByName

data = [
    "# format",
    "# <glyphName> <hex unicode>"
]

for rangeName in getAllRangeNames():
    for u in range(*getRangeByName(rangeName)):
        g = GlyphName(uniNumber=u)
        name = g.getName()
        if name is None:
            continue
        data.append("%s %04X" % (name, u))

path = "./../names/glyphNamesToUnicode"

f = open(path, "w")
f.write("\n".join(data))
f.close()
