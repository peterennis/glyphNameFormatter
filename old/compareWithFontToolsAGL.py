from fontTools.agl import AGL2UV
import unicodedata


path = u"generatedGlyphNames.txt"

f = open(path, "r")
data = f.readlines()
f.close()

agl = {}
for line in data:
    if line:
        parts = line.split("\t")
        n = parts[0]
        u = int(parts[1], 16)
        agl[n] = u
    
print len(AGL2UV)
print len(agl)

code = ["agl = {"]
lines = []
for g, u in AGL2UV.items():
    if g not in agl:
        lines.append("\t".join(["%04X" % u, g, unicodedata.name(unichr(u))]))
        code.append("0x%04X: \"%s\"," % (u, g))
    elif u != agl[g]:
        lines.append("\t".join(["%04X - - - - - - >" % u, g, unicodedata.name(unichr(u))]))
        code.append("0x%04X: \"%s\"," % (u, g))

lines.sort()
code.append("}")
path = "./test/compare_with_AGL.txt"
f = open(path, 'w')
f.write("\n".join(lines))
f.close()


code.sort()
path = "./test/codeAGL.txt"
f = open(path, 'w')
f.write("\n".join(code))
f.close()
