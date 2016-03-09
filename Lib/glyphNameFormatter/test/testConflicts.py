import glyphNameFormatter
reload(glyphNameFormatter)
from glyphNameFormatter.unicodeRangeNames import getRangeByName, getAllRangeNames

#   Find duplicate names for different unicodes

def findConflict():
    names = {}
    lines = []
    for rangeName in getAllRangeNames():
        start, end = getRangeByName(rangeName)
        for uniNumber in range(start, end+1):
            glyphName = glyphNameFormatter.GlyphName(uniNumber)
            if glyphName.hasName():
                # lines.append("%04X\t%s\t%s" % (uniNumber, glyphName.getName(), glyphName.uniName))
                name = glyphName.getName()
                if not name in names:
                    names[name] = []
                names[name].append((uniNumber, glyphName.uniRangeName))
    n = names.keys()
    n.sort()
    for name in n:
        if len(names[name]) > 1:
            l = "\n%s" % (name)
            print l
            lines.append(l)
            for g in names[name]:
                line = "\t%04X\t%s\t%s"%(g[0], name, g[1])
                print line
                lines.append(line)

    path = "./../names/conflict.txt"
    f = open(path, 'w')
    f.write("\n".join(lines))
    f.close()

if __name__ == "__main__":
    findConflict()
