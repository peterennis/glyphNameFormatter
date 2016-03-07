import glyphNameFormatter
reload(glyphNameFormatter)
from glyphNameFormatter.unicodeRangeNames import getRangeFromName, getAllRangeNames

skipped = {}
def generateRange(rangeName):
    # generate all the names in the range
    lines = []
    r = getRangeFromName(rangeName)
    if r is None:
        print "unknown range name", rangeName
        return
    start, end = r
    lines.append("# %s %04X - %04X"%(rangeName, start, end))
    for uniNumber in range(start, end+1):
        glyphName = glyphNameFormatter.GlyphName(uniNumber)
        if glyphName.hasName():
            lines.append("%04X\t%s\t%s"%(uniNumber, glyphName.getName(), glyphName.uniName))
    path = "./names/names_%s.txt"%rangeName.replace(" ", "_").lower()
    f = open(path, 'w')
    f.write("\n".join(lines))
    f.close()

if __name__ == "__main__":
    for rangeName in getAllRangeNames():
        generateRange(rangeName)
