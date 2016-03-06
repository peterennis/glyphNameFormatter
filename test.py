
from glyphNameFormatter import GlyphName

INCLUDECJK = False

def compareWithAGDResults():
    # generate all the names in the first plane
    glyphs = {}
    for uniNumber in range(1, 0xffff):
        glyphName = GlyphName(uniNumber=uniNumber, verbose=False, includeCJK=INCLUDECJK)
        if glyphName.hasName():
            if not INCLUDECJK and glyphName.isCJK:
                continue
        glyphs[uniNumber] = glyphName
    # read the AGD file
    agd = {}
    path = "./test/AGD_name_uni.txt"
    f = open(path, 'r')
    lines = f.read()
    f.close()
    lines = lines.split("\n")
    for l in lines:
        name, uni = l.split("\t")
        uni = int(uni, 16)
        agd[uni] = name
    print "glyphs in AGD:", len(agd)
    print "glyphs in uni:", len(glyphs)

    missingAGD = []
    same = []
    different = []

    for uniNumber in range(1, 0xffff):
        a = agd.get(uniNumber)
        u = glyphs.get(uniNumber)
        if a is None and u is None:
            continue
        if a is None and u is not None:
            missingAGD.append(uniNumber)
            continue
        if u is None:
            continue
        uName = u.uniNameProcessed
        if a == uName:
            same.append(uniNumber)
        else:
            different.append(uniNumber)

    same.sort()
    print "matching names in AGD and uni", len(same)

    onlyShow = [
        "Basic Latin",
        "Latin-1 Supplement",
        "Latin Extended-A",
        "Latin Extended-B"
    ]
    print 
    print len(different), "differing names"
    for uniNumber in different:
        if uniNumber in agd:
            g = glyphs[uniNumber]
            if g.uniRangeName in onlyShow:
                print agd[uniNumber], "\t", g.uniNameProcessed, "\t", g.uniName, "\t", g.uniRangeName


compareWithAGDResults()