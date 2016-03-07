import unicodedata

import unicodeRangeNames
reload(unicodeRangeNames)

from unicodeRangeNames import getRangeName, getRangeProcessor
from preferredAGLNames import preferredAGLNames

class GlyphName(object):

    prefSpelling_dieresis = "dieresis"
    languageTags = {
        'latin': "lt",
        'arabic': 'ar',
        'ipa': 'ipa',
        'greek': 'gr',
        'hebrew': 'hb',
        'boxdrawings': 'bxd',
        'cyrillic': 'cy',
        'hangul': 'ko',
        'japan': 'jp',
        'CJK': 'cjk'
    }

    def __init__(self, niceName=None, uniNumber=None, verbose=False, includeCJK=False):
        self.niceName = niceName
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
        self.latinCentric = True    # admit latincentric naming, if we can leave out latin tags, go for it
        self._log = []
        self.verbose = verbose
        self.includeCJK = includeCJK
        self.isCJK = False
        self.lookup()
        self.process()

    def lookup(self):
        # look up all the external references we need.
        if self.uniNumber is None:
            return
        self.uniLetter = unichr(self.uniNumber)
        try:
            self.uniName = unicodedata.name(self.uniLetter)
            self.uniNameProcessed = self.uniName
        except ValueError:
            pass
        self.uniRangeName = getRangeName(self.uniNumber)

    def hasName(self):
        if not self.uniName:
            return False
        return True

    def hashWords(self):
        parts = {}
        if not self.uniName:
            return parts
        for p in self.uniName.split(" "):
            for q in p.split("-"):
                try:
                    int("0x"+q, 16)
                except ValueError:
                    if not q in parts:
                        parts[q] = 0
                    parts[q] += 1
        return parts

    def has(self, namePart):
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
            ("LATIN SMALL LETTER", ""),
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

    def getName(self, extension=True):
        # return the name, add extensions or not.
        if not extension:
            if self.mustAddScript:
                # we don't want a script extension,
                # but we've been warned that it might be necessary
                # for disambiguation
                if self.scriptTag != self.languageTags['latin'] and self.scriptTag != "":
                    return "%s-%s"%(self.scriptTag, self.uniNameProcessed)
                else:
                    return self.uniNameProcessed
            else:
                # hope for the best then
                return self.uniNameProcessed
        else:
            if self.scriptTag:
                return "%s-%s"%(self.scriptTag, self.uniNameProcessed)
            else:
                return self.uniNameProcessed

    def __repr__(self):
        return "%s\t\t%05x\t\t%s"%(self.getName(extension=False), self.uniNumber, self.uniName)

    def process(self):
        processor = getRangeProcessor(self.uniNumber)
        if processor:
            processor(self)


g = GlyphName(uniNumber=0x0041)

print str(g)


g = GlyphName(uniNumber=0x0145)
print str(g)