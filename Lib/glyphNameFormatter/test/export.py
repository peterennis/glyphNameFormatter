from glyphNameFormatter import GlyphName

from glyphNameFormatter.unicodeRangeNames import getAllRangeNames, getRangeByName, rangeNameToModuleName

import importlib


def generateFlat(path, onlySupported=True):
    data = [
        "# format",
        "# <glyphName> <hex unicode>"
    ]
    for rangeName in getAllRangeNames():
        if onlySupported:
            moduleName = rangeNameToModuleName(rangeName)
            try:
                module = importlib.import_module('glyphNameFormatter.rangeProcessors.%s' % moduleName)
            except:
                continue

        for u in range(*getRangeByName(rangeName)):
            g = GlyphName(uniNumber=u)
            name = g.getName()
            if name is None:
                continue
            data.append("%s %04X" % (name, u))

    f = open(path, "w")
    f.write("\n".join(data))
    f.close()

generateFlat(path="./../names/glyphNamesToUnicode")
