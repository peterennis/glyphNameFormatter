#coding: utf-8
import os

import importlib
import time

import subprocess

from glyphNameFormatter import GlyphName, __version__
from glyphNameFormatter.unicodeRangeNames import getAllRangeNames, getRangeByName, rangeNameToModuleName
from glyphNameFormatter.data.scriptPrefixes import SCRIPTSEPARATOR, SCRIPTASPREFIX
from glyphNameFormatter.exporters.analyseConflicts import findConflict


def getExportVersionNumber():
    commitNumber = subprocess.check_output(["git", "rev-list", "HEAD", "--count"], cwd=os.path.dirname(__file__))
    commitNumber = commitNumber.strip()
    return "%s - git commit: %s" % (__version__, commitNumber)


def generateFlat(path, onlySupported=True, scriptSeparator=None, scriptAsPrefix=None, findConflicts=True):
    if findConflicts:
        findConflict(makeModule=True)

    data = [
        "# Glyph Name Formatted Unicode List - GNFUL",
        "# GlyphNameFormatter version %s" % getExportVersionNumber(),
        "# Generated on %s" % time.strftime("%Y %m %d %H:%M:%S"),
        "# <glyphName> <hex unicode>",
    ]
    if scriptSeparator is not None:
        data.append("# Separator \"%s\"" % scriptSeparator)
    if scriptAsPrefix is not None:
        data.append("# Prefixed \"%s\"" % scriptAsPrefix)
    data.append("#")
    for rangeName in getAllRangeNames():
        if onlySupported:
            moduleName = rangeNameToModuleName(rangeName)
            try:
                module = importlib.import_module('glyphNameFormatter.rangeProcessors.%s' % moduleName)
            except:
                continue
        data.append("# %s" % rangeName)
        for u in range(*getRangeByName(rangeName)):
            g = GlyphName(uniNumber=u)
            name = g.getName(extension=True, scriptSeparator=scriptSeparator, scriptAsPrefix=scriptAsPrefix)
            if name is None:
                continue
            data.append("%s %04X" % (name, u))

    f = open(path, "w")
    f.write("\n".join(data))
    f.close()

if __name__ == "__main__":

    # generate a flat export
    generateFlat("./../names/glyphNamesToUnicode.txt")

    # and because this is a generator we can make any flavor we want:
    for separator, sn in [
            (":", "colon"),
            ("-", "hyphen")
            ]:
        for asPrefix, pn in [
                (True, "prefixed"),
                (False, "suffixed")
                ]:
            for onlySupported, sp in [
                    (True, "AGDonly"),
                    (False, "full")    # large files, proceed at own leisurely pace.
                    ]:
                path = "./../names/glyphNamesToUnicode_%s_%s_%s.txt" % (sp, sn, pn)
                generateFlat(path, onlySupported=onlySupported, scriptSeparator=separator, scriptAsPrefix=asPrefix, findConflicts=False)
