import glyphNameFormatter
reload(glyphNameFormatter)
print glyphNameFormatter.__file__


skipped = {}
def generateAll(path, includeCJK=False):
    # generate all the names in the first plane
    lines = []
    uniqueNamesExtension = {}
    uniqueNamesNoExtension = {}
    for uniNumber in range(1, 0xff):
        glyphName = glyphNameFormatter.GlyphName(uniNumber=uniNumber, verbose=False, includeCJK=includeCJK)
        if glyphName.hasName():
            if (not includeCJK) and glyphName.isCJK:
                continue
            lines.append("%04X\t%s\t%s"%(uniNumber, glyphName.getName(extension=True), glyphName.uniName))
    f = open(path, 'w')
    f.write("\n".join(lines))
    f.close()

if __name__ == "__main__":
	generateAll("./names.txt")
	print 'done'