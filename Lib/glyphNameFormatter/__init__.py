# -*- coding: UTF-8 -*-
from __future__ import print_function

import unicodedata

from data.scriptConflictNames import scriptConflictNames
from data.preferredAGLNames import preferredAGLNames
from data.scriptPrefixes import scriptPrefixes, addScriptPrefix, SCRIPTSEPARATOR, SCRIPTASPREFIX

from unicodeRangeNames import getRangeName, getRangeProcessor, getRangeProcessorByRangeName

from tools import unicodeToChar


__version__ = "0.1"


def debug(uniNumber):
    # trace the processing of a specific number
    glyphName = GlyphName(uniNumber=uniNumber, verbose=True)
    glyphName.process()
    print("debug: %04x" % uniNumber)
    print("name:", glyphName.getName())
    for step in glyphName._log:
        print("\t", step)


class GlyphName(object):

    prefSpelling_dieresis = "dieresis"

    def __init__(self, uniNumber=None, verbose=False):
        self.uniNumber = uniNumber
        self.uniLetter = None
        self.uniName = ""
        self.uniNameProcessed = self.uniName
        self.uniRangeName = "No Range"
        self.letterCase = None
        self.isLigature = False
        self.scriptTag = ""
        self.languageSuffix = []
        self.suffixParts = []
        self.finalParts = []
        self.mustAddScript = False  # set to True if we need to add script to disambiguate
        self.statsPrefixRequested = False
        self._log = []
        self.verbose = verbose

        self.lookup()
        self.process()

    def lookup(self):
        # look up all the external references we need.
        if self.uniNumber is None:
            return
        try:
            self.uniLetter = unicodeToChar(self.uniNumber)
        except:
            print("GlyphName valueerror for %04X" % self.uniNumber)
            return
        try:
            self.uniName = unicodedata.name(self.uniLetter)
            self.uniNameProcessed = self.uniName
            self.bidiType = unicodedata.bidirectional(self.uniLetter)
        except ValueError:
            self.uniName = None
            self.uniLetter = None
            self.bidiType = None
        self.uniRangeName = getRangeName(self.uniNumber)

    def hasName(self):
        if not self.uniName:
            return False
        return True

    def has(self, namePart):
        if self.uniName is None:
            return False
        if namePart in self.uniName:
            return True
        return False

    def handleCase(self):
        upperCaseIndicators = [
            # from complex to simple
            ("LETTER SMALL CAPITAL", "small"),
            ("SMALL CAPITAL LETTER", "smallcapital"),
            ("CAPITAL LETTER", ""),
            ("MODIFIER LETTER CAPITAL", "mod"),
            ("MODIFIER LETTER SMALL CAPITAL", "modsmall"),
            ("CAPITAL", ""),
        ]
        lowercaseIndicators = [
            # from complex to simple
            # ("LATIN SMALL LETTER", ""),
            ("SMALL LETTER", ""),
            ("MODIFIER LETTER SMALL", "mod"),
            ("SMALL", ""),
        ]
        for upperNames, suffix in upperCaseIndicators:
            if self.has(upperNames):
                start = self.uniNameProcessed.find(upperNames)
                if start == -1:
                    continue
                before = after = self.uniNameProcessed[start + len(upperNames):].strip()
                if not before:
                    continue
                elif len(before) == 1:
                    after = before.upper()
                else:
                    after = before[0].upper()+before[1:].lower()
                self.edit(upperNames, suffix)
                self.replace(before, after)
        for lowerNames, suffix in lowercaseIndicators:
            if self.has(lowerNames):
                start = self.uniNameProcessed.find(lowerNames)
                if start == -1:
                    continue
                before = after = self.uniNameProcessed[start + len(lowerNames):].strip()
                after = after.lower()
                self.edit(lowerNames, suffix)
                self.replace(before, after)

    def getName(self, extension=True, scriptSeparator=None, scriptAsPrefix=None):
        # return the name, add extensions or not.
        self.requestedScriptSeparator = SCRIPTSEPARATOR
        self.requestedScriptAsPrefix = SCRIPTASPREFIX
        if scriptSeparator is not None:
            self.requestedScriptSeparator = scriptSeparator
        if scriptAsPrefix is not None:
            self.requestedScriptAsPrefix = scriptAsPrefix
        if self.uniName is None:
            # nothing to see here.
            return None
        if extension is False:
            return self.uniNameProcessed
        if self.mustAddScript:
            # we don't want a script extension,
            # but we've been warned that it might be necessary
            # for disambiguation
            if self.scriptTag != scriptPrefixes['latin'] and self.scriptTag != "":
                if self.mustAddScript and self.scriptTag:
                    return addScriptPrefix(self.uniNameProcessed,
                                self.scriptTag,
                                scriptSeparator=self.requestedScriptSeparator,
                                scriptAsPrefix=self.requestedScriptAsPrefix,
                                )
            else:
                return self.uniNameProcessed
        else:
            # hope for the best then
            return self.uniNameProcessed

    def __repr__(self):
        return "%s\t\t%05x\t\t%s" % (self.getName(extension=False), self.uniNumber, self.uniName)

    def process(self):
        # try to find appropriate formatters and
        if self.uniNumber in preferredAGLNames:
            self.uniNameProcessed = preferredAGLNames[self.uniNumber]
        # get the processor
        processor = getRangeProcessor(self.uniNumber)
        if processor:
            # set the script
            self.scriptTag = scriptPrefixes[getRangeName(self.uniNumber)]
            processor(self)
            # make the final name
            self.uniNameProcessed = self.uniNameProcessed + "".join(self.suffixParts) + "".join(self.finalParts)
        if self.uniNameProcessed in scriptConflictNames:
            # the final name has a duplicate in another script
            # take disambiguation action
            self.mustAddScript = True

    def processAs(self, rangeName):
        if not rangeName.lower().startswith("helper"):
            self.scriptTag = scriptPrefixes[rangeName]
        processor = getRangeProcessorByRangeName(rangeName)
        processor(self)

    def edit(self, pattern, *suffix):
        # look for pattern
        # remove the pattern from the name
        # add any suffix patterns to the suffixParts
        """
        a method that does the same as this:
        if self.has("PATTERN"):
            if self.replace("PATTERN"):
                self.suffix("suffix")
                self.suffix("suffix")
        """
        if self.replace(pattern):
            [self.suffix(s) for s in suffix]

    def compress(self):
        # remove the spaces from the name
        self.uniNameProcessed = self.uniNameProcessed.replace(" ", "")

    def lower(self):
        # whole name to lowercase
        self.uniNameProcessed = self.uniNameProcessed.lower()

    def suffix(self, namePart):
        # add a suffix part
        if namePart not in self.suffixParts:
            self.suffixParts.append(namePart)

    def scriptPrefix(self):
        self.statsPrefixRequested = True
        self.mustAddScript = True

    def final(self, namePart):
        # add a final part, for things that have the really last, like name extensions
        if namePart not in self.finalParts:
            self.finalParts.append(namePart)

    def editSuffix(self, lookFor, replaceWith):
        for n, i in enumerate(self.suffixParts):
            if i == lookFor:
                self.suffixParts[n] = replaceWith

    def editToFinal(self, namePart, *finals):
        # similar to edit(), but the parts are added the finalParts, not suffixParts
        # if you want to be really sure the parts end up at the end
        if self.replace(namePart):
            [self.final(s) for s in finals]

    def log(self, lookFor, replaceWith, before, after):
        self._log.append((lookFor, replaceWith, before, after))

    def replace(self, lookFor, replaceWith=""):
        after = self.uniNameProcessed.replace(lookFor, replaceWith)
        if self.uniNameProcessed == after:
            return False
        before = self.uniNameProcessed
        self.uniNameProcessed = self.uniNameProcessed.replace(lookFor, replaceWith)
        self.uniNameProcessed = self.uniNameProcessed.replace("  ", " ")
        self.uniNameProcessed = self.uniNameProcessed.strip()
        self.log(lookFor, replaceWith, before, self.uniNameProcessed)
        return True

    def condense(self, part, combiner=""):
        # remove spaces, remove hyphens, change to lowercase
        if part is None:
            return
        editPart = part.replace(" ", combiner)
        editPart = editPart.replace("-", "")
        editPart = editPart.lower()
        self.replace(part, editPart)


if __name__ == "__main__":

    import doctest

    def _testGlyphName():
        # basic tests for the GlyphName object
        """
        >>> g = GlyphName(uniNumber=0x020)
        >>> assert g.uniName == "SPACE"
        >>> g.edit("SPACE", "space")
        >>> g.suffixParts
        ['space']
        >>> g.uniNameProcessed
        'space'
        >>> g.getName()
        'space'

        >>> g = GlyphName(uniNumber=0x021)
        >>> g.uniName
        'EXCLAMATION MARK'
        >>> g.getName()
        'exclam'

        >>> g = GlyphName(uniNumber=0x041)
        >>> g.uniName
        'LATIN CAPITAL LETTER A'
        >>> g.handleCase()
        >>> g.getName()
        'A'
        >>> g = GlyphName(uniNumber=0x061)
        >>> g.uniName
        'LATIN SMALL LETTER A'
        >>> g.handleCase()
        >>> g.getName()
        'a'
        >>> g = GlyphName(uniNumber=0x0ABD)
        >>> g.getName(scriptSeparator="$")  # no, this is not a proposal to use $ as a separator.
        'gujr$avagraha'
        >>> g.getName(scriptSeparator=":")
        'gujr:avagraha'
        >>> g.getName(scriptSeparator=":", scriptAsPrefix=True)
        'gujr:avagraha'
        >>> g.getName(scriptSeparator=":", scriptAsPrefix=False)
        'avagraha:gujr'
        """

    doctest.testmod()
