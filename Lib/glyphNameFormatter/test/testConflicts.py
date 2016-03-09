import glyphNameFormatter
reload(glyphNameFormatter)
from glyphNameFormatter.unicodeRangeNames import getRangeByName, getAllRangeNames
from glyphNameFormatter.data import unicode2name_AGD

#   Find duplicate names for different unicodes

includeScriptPrefix = False

def findConflict():
    names = {}
    lines = []
    for rangeName in getAllRangeNames():
        start, end = getRangeByName(rangeName)
        for uniNumber in range(start, end+1):
            glyphName = glyphNameFormatter.GlyphName(uniNumber, includeScriptPrefix=includeScriptPrefix)
            if glyphName.hasName():
                # lines.append("%04X\t%s\t%s" % (uniNumber, glyphName.getName(), glyphName.uniName))
                name = glyphName.getName()
                if not name in names:
                    names[name] = []
                names[name].append((uniNumber, glyphName.uniRangeName))
    n = names.keys()
    n.sort()

    conflictNames = []
    conflictUniNumbers = []
    for name in n:
        if len(names[name]) > 1:
            conflictNames.append(name)
            l = "\n%s" % (name)
            print l
            lines.append(l)
            for g in names[name]:
                conflictUniNumbers.append(g[0])
                AGLname = unicode2name_AGD.get(g[0], "-")
                line = "        %04X%20s%20s%40s"%(g[0], name, AGLname, g[1])
                print line
                lines.append(line)
    stats =  "# %d names with conflicts, affecting %d unicodes"%(len(conflictNames), len(conflictUniNumbers))
    print stats
    lines.append(stats)


    path = "./../names/conflict.txt"
    f = open(path, 'w')
    f.write("\n".join(lines))
    f.close()

if __name__ == "__main__":
    findConflict()
