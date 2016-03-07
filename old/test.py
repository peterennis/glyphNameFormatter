
from glyphNameFormatter import *

debug(0x0028)

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
    totalAgdNameLengths = []
    totalUniNameLengths = []
    selectionAgdNameLengths = []
    selectionUniNameLengths = []
    lengthWarnings = []

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
        uName = u.getName(extension=False)
        if a == uName:
            same.append(uniNumber)
        else:
            different.append(uniNumber)
        # stats
        agdLen = len(a)
        uniLen = len(uName)
        if uniLen > agdLen:
            lengthWarnings.append("%04x\t%s\t%s\t%s"%(uniNumber, a, uName, u.uniRangeName))
        totalAgdNameLengths.append(agdLen)
        totalUniNameLengths.append(uniLen)
    same.sort()
    print "matching names in AGD and uni", len(same)

    onlyShow = [
     
        
        'Basic Latin',
        'Latin-1 Supplement',
        'Latin Extended-A',
        'Latin Extended-B',
        'Latin Extended Additional',
        'Cyrillic',
        'Cyrillic Supplementary',
        "Arabic",
        'Arabic Presentation Forms-A',
        'Arabic Presentation Forms-B',
        'Hebrew',
        "IPA Extensions",
        "Phonetic Extensions",
        "Box Drawing",

        "Greek and Coptic",
        "Greek Extended",

        "Arrows",
        "Supplemental Arrows-A",
        "Supplemental Arrows-B",

        "Katakana",
         "Katakana Phonetic Extensions",
        "Hiragana",

        "CJK Unified Ideographs",
        "CJK Unified Ideographs Extension A",
        "CJK Compatibility",
        "CJK Compatibility Forms",
        "CJK Compatibility Ideographs",
        "CJK Radicals Supplement",
        "CJK Symbols and Punctuation"



    ]


    differentCount = 0
    for uniNumber in different:
        g = glyphs[uniNumber]
        if g.uniRangeName in onlyShow:
            differentCount += 1

    print 
    print differentCount, "differing names"
    lines = []
    for uniNumber in different:
        if uniNumber in agd:
            g = glyphs[uniNumber]
            if g.uniRangeName in onlyShow:
                line = []
                line.append(hex(g.uniNumber))
                line.append(agd[uniNumber])
                line.append(g.getName(extension=False))
                line.append(g.uniName)
                lines.append("\t".join(line))
                selectionAgdNameLengths.append(len(agd[uniNumber]))
                selectionUniNameLengths.append(len(g.getName(extension=False)))
    path = "./test/compare_with_AGD.txt"
    f = open(path, 'w')
    f.write("\n".join(lines))
    f.close()

    path = "./test/lengthWarnings.txt"
    f = open(path, 'w')
    f.write("\n".join(lengthWarnings))
    f.close()

    print "average name length AGD total", sum(totalAgdNameLengths)/float(len(totalAgdNameLengths)), "(total %d)"%len(totalAgdNameLengths)
    print "average name length Uni total", sum(totalUniNameLengths)/float(len(totalUniNameLengths)), "(total %d)"%len(totalUniNameLengths)

    print "average name length AGD selection", sum(selectionAgdNameLengths)/float(len(selectionAgdNameLengths)), "(total %d)"%len(selectionAgdNameLengths)
    print "average name length Uni selection", sum(selectionUniNameLengths)/float(len(selectionUniNameLengths)), "(total %d)"%len(selectionUniNameLengths)

compareWithAGDResults()