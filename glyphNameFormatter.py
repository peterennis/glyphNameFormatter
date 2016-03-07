import unicodedata
from unicodeRangeNames import *

#
#   this is an experimental approach
#   to generating a list of glyph names
#   from the standard unicode names
#
#
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
    ambiguousNames =[
        "A",
        "Abreve",
        "Adieresis",
        "E",
        "Edieresis",
        "Gamma",
        "I",
        "Idieresis",
        "Igrave",
        "Imacron",
        "Iota",
        "Koppa",
        "O",
        "Odieresis",
        "Omega",
        "Psi",
        "Schwa",
        "U",
        "Udblacute",
        "Udieresis",
        "Umacron",
        "Upsilon",
        "a", "ae",
        "abreve",
        "adieresis",
        "comma",
        "delta",
        "e",
        "edieresis",
        'gamma',
        "i",
        "idieresis",
        "igrave",
        "imacron",
        'iota',
        "koppa",
        "o", "oe",
        "odieresis",
        "omega",
        "pe",
        'phi',
        "psi",
        "question",
        "u",
        "udblacute",
        "udieresis",
        "umacron",
        'upsilon',
        "yu",
        "ve",

        "numbersign",
        "semicolon",
        'zero', 'one', 'two', 'three', 'four', 'five', 'six',
        'seven', 'eight', 'nine',
        'percent'
    ]
    preferredAGLNames = {
        0x0040: "at",
        0x00A5: "yen",
        # 0x00B5: "mu",
        0x0133: "ij",
        0x014B: "eng",
        0x02C6: "circumflex",
        0x02C7: "caron",
        0x02D8: "breve",
        0x02D9: "dotaccent",
        0x02DA: "ring",
        0x02DB: "ogonek",
        0x02DC: "tilde",
        0x02DD: "hungarumlaut",
        0x0300: "gravecomb",
        0x0301: "acutecomb",
        0x0303: "tildecomb",
        0x0309: "hookabovecomb",
        0x0323: "dotbelowcomb",
        # 0x03B4: "delta",
        # 0x03BD: "nu",
        # 0x03C0: "pi",
        0x2012: "figuredash",
        0x2013: "endash",
        0x2014: "emdash",
        0x2017: "underscoredbl",
        0x2018: "quoteleft",
        0x2019: "quoteright",
        0x201A: "quotesinglbase",
        0x201B: "quotereversed",
        0x201C: "quotedblleft",
        0x201D: "quotedblright",
        0x201E: "quotedblbase",
        0x2020: "dagger",
        0x2021: "daggerdbl",
        0x2022: "bullet",
        0x2024: "onedotenleader",
        0x2025: "twodotenleader",
        0x2026: "ellipsis",
        0x2030: "perthousand",
        0x2032: "minute",
        0x2033: "second",
        0x2039: "guilsinglleft",
        0x203A: "guilsinglright",
        0x203C: "exclamdbl",
        0x2044: "fraction",
        0x20A1: "colonmonetary",
        0x20A3: "franc",
        0x20A4: "lira",
        0x20A7: "peseta",
        0x20AB: "dong",
        0x20AC: "Euro",
        0x2111: "Ifraktur",
        0x2118: "weierstrass",
        0x211C: "Rfraktur",
        0x211E: "prescription",
        0x2122: "trademark",
        # 0x2126: "Omega",
        0x212E: "estimated",
        0x2135: "aleph",
        0x2153: "onethird",
        0x2154: "twothirds",
        0x215B: "oneeighth",
        0x215C: "threeeighths",
        0x215D: "fiveeighths",
        0x215E: "seveneighths",
        0x2200: "universal",
        0x2202: "partialdiff",
        0x2203: "existential",
        0x2205: "emptyset",
        # 0x2206: "Delta",
        0x2207: "gradient",
        0x2208: "element",
        0x2209: "notelement",
        0x220B: "suchthat",
        0x220F: "product",
        0x2211: "summation",
        0x2212: "minus",
        0x2217: "asteriskmath",
        0x221A: "radical",
        0x221D: "proportional",
        0x221E: "infinity",
        0x221F: "orthogonal",
        0x2220: "angle",
        0x2227: "logicaland",
        0x2228: "logicalor",
        0x2229: "intersection",
        0x222A: "union",
        0x222B: "integral",
        0x2234: "therefore",
        0x223C: "similar",
        0x2245: "congruent",
        0x2248: "approxequal",
        0x2260: "notequal",
        0x2261: "equivalence",
        0x2264: "lessequal",
        0x2265: "greaterequal",
        0x2282: "propersubset",
        0x2283: "propersuperset",
        0x2284: "notsubset",
        0x2286: "reflexsubset",
        0x2287: "reflexsuperset",
        0x2295: "circleplus",
        0x2297: "circlemultiply",
        0x22A5: "perpendicular",
        0x22C5: "dotmath",
        0x2302: "house",
        0x2310: "revlogicalnot",
        0x2320: "integraltp",
        0x2321: "integralbt",
        0x2329: "angleleft",
        0x232A: "angleright",
        # 0x2500: "SF100000",
        # 0x2502: "SF110000",
        # 0x250C: "SF010000",
        # 0x2510: "SF030000",
        # 0x2514: "SF020000",
        # 0x2518: "SF040000",
        # 0x251C: "SF080000",
        # 0x2524: "SF090000",
        # 0x252C: "SF060000",
        # 0x2534: "SF070000",
        # 0x253C: "SF050000",
        # 0x2550: "SF430000",
        # 0x2551: "SF240000",
        # 0x2552: "SF510000",
        # 0x2553: "SF520000",
        # 0x2554: "SF390000",
        # 0x2555: "SF220000",
        # 0x2556: "SF210000",
        # 0x2557: "SF250000",
        # 0x2558: "SF500000",
        # 0x2559: "SF490000",
        # 0x255A: "SF380000",
        # 0x255B: "SF280000",
        # 0x255C: "SF270000",
        # 0x255D: "SF260000",
        # 0x255E: "SF360000",
        # 0x255F: "SF370000",
        # 0x2560: "SF420000",
        # 0x2561: "SF190000",
        # 0x2562: "SF200000",
        # 0x2563: "SF230000",
        # 0x2564: "SF470000",
        # 0x2565: "SF480000",
        # 0x2566: "SF410000",
        # 0x2567: "SF450000",
        # 0x2568: "SF460000",
        # 0x2569: "SF400000",
        # 0x256A: "SF540000",
        # 0x256B: "SF530000",
        # 0x256C: "SF440000",
        0x2580: "upblock",
        0x2584: "dnblock",
        0x2588: "block",
        0x258C: "lfblock",
        0x2590: "rtblock",
        0x2591: "ltshade",
        0x2592: "shade",
        0x2593: "dkshade",
        0x25A0: "filledbox",
        # 0x25A1: "H22073",
        # 0x25AA: "H18543",
        # 0x25AB: "H18551",
        0x25AC: "filledrect",
        0x25B2: "triagup",
        0x25BA: "triagrt",
        0x25BC: "triagdn",
        0x25C4: "triaglf",
        0x25CA: "lozenge",
        0x25CB: "circle",
        # 0x25CF: "H18533",
        0x25D8: "invbullet",
        0x25D9: "invcircle",
        0x25E6: "openbullet",
        0x263A: "smileface",
        0x263B: "invsmileface",
        0x263C: "sun",
        0x2640: "female",
        0x2642: "male",
        0x2660: "spade",
        0x2663: "club",
        0x2665: "heart",
        0x2666: "diamond",
        0x266A: "musicalnote",
        0x266B: "musicalnotedbl",
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

    def processStructure(self):
        if self.verbose:
            print "processStructure"
        if self.has("LIGATURE"):
            self.isLigature = True

    def processCase(self):
        if self.verbose:
            print "processCase"
        if self.has("CAPITAL LETTER"):
            self.letterCase = "uppercase"
        if self.has("SMALL LETTER"):
            self.letterCase = "lowercase"

    def processShape(self):
        if self.verbose:
            print "processShape"
        self.edit("LITTLE", "little")
        self.edit("BIG", "big")
        self.edit("ROUND", "round")

        self.edit("SHORT", "short")
        self.edit("STRAIGHT", "straight")
        self.edit("BARRED", "barred")
        self.edit('OPEN', "open")
        self.edit('CLOSED', "closed")
        self.edit('REVERSED', "reversed")
        self.edit("MONOCULAR", "monocular")
        self.edit("SIDEWAYS", 'sideways')
        self.edit("BOTTOM HALF", 'bottomhalf')
        self.edit("TOP HALF", 'tophalf')

        self.edit("WITH TITLO", "titlo")
        self.edit("TITLO", "titlo")
        self.edit("WITH TAIL", "tail")
        self.edit("WITH TICK", "tick")
        self.edit("WITH DESCENDER", "descender")
        self.edit("WITH UPTURN", "up")
        self.edit("WITH STROKE", "stroke")
        self.edit("WITH VERTICAL STROKE", "verticalstroke")
        self.edit("WITH DIAGONAL STROKE", "diagonalstroke")
        self.edit("WITH HIGH STROKE", "highstroke")
        self.edit("WITH SWASH TAIL", "swash", "tail")
        self.edit("WITH COMMA BELOW", "commaaccent")
        self.edit("WITH PALATAL HOOK", "palatalhook")

    def processDiacritics(self):
        if self.verbose:
            print "processDiacritics"
        # WITH ___ AND ___
        self.edit("WITH CIRCUMFLEX AND HOOK ABOVE", "circumflex", "hoi")
        self.edit("WITH CIRCUMFLEX AND DOT BELOW", "circumflex", "dotbelow")
        self.edit("WITH DOT BELOW AND DOT ABOVE", "dotbelow", "dotabove")
        self.edit("WITH CIRCUMFLEX AND TILDE", "circumflex", "tilde")
        self.edit("WITH CARON AND DOT ABOVE", "caron", "dot")
        self.edit("WITH ACUTE AND DOT ABOVE", "acute", "dotaccent")
        self.edit("WITH HORN AND GRAVE", "horn", 'grave')
        self.edit("WITH HORN AND ACUTE", "horn", 'acute')
        self.edit("WITH HORN AND TILDE", "horn", 'tilde')
        self.edit("WITH HORN AND HOOK ABOVE", "horn", "hoi")
        self.edit("WITH HORN AND DOT BELOW", "horn", "dotbelow")
        self.edit("WITH BREVE AND TILDE", "breve", "tilde")
        self.edit("WITH BREVE AND ACUTE", "breve", "acute")
        self.edit("WITH BREVE AND HOOK ABOVE", "breve", "hoi")
        self.edit("WITH BREVE AND DOT BELOW", "breve", "dotbelow")
        self.edit("WITH BREVE BELOW", "breve", "below")
        self.edit("WITH TILDE AND DIAERESIS", "tilde", self.prefSpelling_dieresis)
        self.edit("WITH BREVE AND GRAVE", "breve", "grave")
        self.edit("WITH DOT BELOW AND MACRON", "macron", "dot")
        self.edit("WITH DIAERESIS AND GRAVE", self.prefSpelling_dieresis, "grave")
        self.edit("WITH DIAERESIS AND ACUTE", self.prefSpelling_dieresis, "acute")
        self.edit("WITH DIAERESIS AND TILDE", self.prefSpelling_dieresis, "tilde")
        self.edit("WITH TILDE BELOW", "tilde", "below")
        self.edit('WITH CIRCUMFLEX AND ACUTE', 'circumflex', 'acute')
        self.edit('WITH CIRCUMFLEX AND GRAVE', 'circumflex', 'grave')
        self.edit("WITH CIRCUMFLEX BELOW", "circumflex", "below")
        self.edit("WITH CEDILLA AND ACUTE", "cedilla", "acute")
        self.edit("WITH CEDILLA AND BREVE", "cedilla", 'breve')
        self.edit("WITH MACRON AND DIAERESIS", "macron", self.prefSpelling_dieresis)
        self.edit("WITH MACRON AND ACUTE", "macron", "acute")
        self.edit("WITH MACRON AND GRAVE", "macron", "grave")
        self.edit("WITH TILDE AND ACUTE", "tilde", "acute")
        self.edit("WITH TILDE AND MACRON", "tilde", "macron")
        self.edit("WITH DIAERESIS AND MACRON", self.prefSpelling_dieresis, "macron")
        self.edit("WITH DOT ABOVE AND MACRON", "dot", "macron")
        # PRECEDED BY ___
        self.edit("PRECEDED BY APOSTROPHE", "apostrophe")
        # WITH ___ 
        self.edit("WITH INVERTED BREVE", "inverted", "breve")
        self.edit("WITH TOPBAR", "topbar")
        self.edit("WITH MIDDLE DOT", "dot")
        self.edit("WITH DOUBLE ACUTE", "dblacute")
        self.edit("WITH DOUBLE GRAVE ACCENT", "dblgrave")
        self.edit("WITH DOUBLE GRAVE", "dblgrave")
        self.edit("WITH DOT ABOVE", "dot")
        self.edit("WITH DOT BELOW", "dotbelow")
        self.edit("WITH GRAVE", "grave")
        self.edit("GRAVE", "grave")
        self.edit("WITH HORN", "horn")
        self.edit("WITH BREVE", "breve")
        self.edit("BREVE", "breve")
        self.edit("WITH DIAERESIS BELOW", self.prefSpelling_dieresis, "below")
        self.edit("WITH DIAERESIS", self.prefSpelling_dieresis)
        self.edit("DIAERESIS", self.prefSpelling_dieresis)
        self.edit("WITH MACRON", "macron")
        self.edit("MACRON", "macron")
        self.edit("WITH ACUTE", "acute")
        self.edit("ACUTE", "acute")
        self.edit("WITH CARON", "caron")
        self.edit("CARON", "caron")
        self.edit("WITH CIRCUMFLEX", "circumflex")
        self.edit("CIRCUMFLEX", "circumflex")
        self.edit("WITH TILDE", "tilde")
        self.edit("TILDE", "tilde")
        self.edit("WITH CEDILLA", "cedilla")
        self.edit("CEDILLA", "cedilla")
        self.edit("WITH OGONEK", "ogonek")
        self.edit("OGONEK", "ogonek")
        self.edit("WITH RING ABOVE AND ACUTE","ring","acute")
        self.edit("WITH RING ABOVE", "ring")
        self.edit("WITH RING BELOW", "ringbelow")
        self.edit("WITH RIGHT HALF RING", "right", "halfring")
        self.edit("WITH RETROFLEX HOOK", "retroflex")
        self.edit("WITH LINE BELOW", "linebelow")
        self.edit("WITH BAR", "bar")
        self.edit("WITH MACRON", "macron")
        self.edit("WITH MIDDLE TILDE", 'middletilde')
        self.edit("WITH HOOK TAIL", "hook", "tail")
        self.edit("WITH MIDDLE HOOK", "middlehook")
        self.edit("WITH LOOP", "loop")
        self.edit("WITH LEFT HOOK", "hook", "left")
        self.edit("WITH HOOK ABOVE", "hoi")
        self.edit("WITH HOOK", "hook")
        self.edit("AND HOOK", "hook")
        self.edit("HOOK", "hook")
        self.edit("WITH CURL", "curl")
        if self.has("BAR") and not self.has("AKBAR") and not self.has("TOPBAR") and not self.has("BARRED"):
            if self.replace("BAR"):
                self.suffix("bar")

    def processArabic(self):
        if self.verbose:
            print "processArabic"
        self.scriptTag = self.languageTags['arabic']

        # AGD compatible
        self.edit("ARABIC SMALL HIGH LIGATURE QAF WITH LAM WITH ALEF MAKSURA", "qam_lamalefabove")
        self.edit("ARABIC SMALL HIGH LIGATURE SAD WITH LAM WITH ALEF MAKSURA", "sad_lamalefabove")
        self.edit("ARABIC SIGN SAFHA", "Safha")
        self.edit("ARABIC DATE SEPARATOR", "Date")
        self.edit("ARABIC POETIC VERSE SIGN", "Poetic")
        self.edit("ARABIC SIGN MISRA", "Misra")
        self.edit("ARABIC LETTER DAL WITH INVERTED V", "dalinvertedv")
        self.edit("ARABIC LETTER REH WITH INVERTED V", "rehinvertedv")
        self.edit("ARABIC SMALL WAW", "wawsmall")
        self.edit("ARABIC SMALL YEH", "yehsmall")
        self.edit("WITH DOT BELOW AND DOT ABOVE", "dotbelowdotabove")
        self.edit("WITH DOT MOVED BELOW", 'dotbelowright')
        self.edit("WITH DOT ABOVE", "dotabove")
        self.edit("WITH TWO DOTS ABOVE", 'twoabove')
        self.edit("WITH TWO DOTS BELOW", 'twobelow')
        self.edit("WITH THREE DOTS BELOW AND THREE DOTS ABOVE", 'threebelowthreeabove')
        self.edit("WITH THREE DOTS BELOW", 'threebelow')
        self.edit("WITH THREE DOTS ABOVE", 'threeabove')
        self.edit("HIGH THREE DOTS", "threeabove")
        self.edit("HIGH HAMZA", "highhamza")
        self.edit("ARABIC SMALL HIGH LAM ALEF", "lamalefabove")
        self.edit("ARABIC SMALL HIGH MEEM INITIAL FORM", "meemabove.init")
        self.edit("WITH HAMZA ABOVE", "hamza")
        self.edit("WITH YEH ABOVE", 'yehabove')
        self.edit("ARABIC MADDAH ABOVE", "maddah")
        self.edit("ARABIC SUBSCRIPT ALEF", "alefbelow")
        self.edit("ARABIC VOWEL SIGN DOT BELOW", "dotbelow")
        self.edit("ARABIC REVERSED DAMMA", "dammareversed")
        self.edit("ARABIC FATHA WITH TWO DOTS", "fathadotted")
        self.edit("ARABIC LETTER ALEF WITH MADDA ABOVE", "alefmadda")
        self.edit("ARABIC LETTER ALEF WITH HAMZA ABOVE", "alefhamza")
        self.edit("ARABIC LETTER WAW WITH HAMZA ABOVE", "wawhamza")
        self.edit("ARABIC LETTER ALEF WITH HAMZA BELOW", "alefhamzabelow")
        self.edit("ARABIC-INDIC DIGIT")
        self.edit("ARABIC PERCENT SIGN", "percent")
        self.edit("ARABIC DECIMAL SEPARATOR", "Decimal")
        self.edit("ARABIC THOUSANDS SEPARATOR", "Thousands")
        self.edit("ARABIC LETTER DOTLESS BEH", 'behdotless')
        self.edit("ARABIC LETTER DOTLESS QAF", 'qafdotless')
        self.edit("ARABIC SIGN SINDHI AMPERSAND", "ampersand","sindhi")
        self.edit("ARABIC SIGN SINDHI POSTPOSITION MEN", "Men", "post" ,"sindhi" )
        self.edit("WITH RING", "ring")
        self.edit("WITH TAIL", "tail")
        self.edit("ARABIC LETTER TEH WITH THREE DOTS ABOVE DOWNWARDS", 'tehthreedownabove')
        self.edit("ARABIC LETTER HAH WITH TWO DOTS VERTICAL ABOVE", "hahtwodotsverticalabove")
        self.edit("ARABIC SMALL HIGH UPRIGHT RECTANGULAR ZERO", 'zerosquareabove')
        self.edit("WITH DOT BELOW", "dotbelow")
        self.edit("WITH FOUR DOTS ABOVE", 'fourdotsabove')
        self.edit("END OF AYAH", "ayahend")
        self.edit("ARABIC START OF RUB EL HIZB", "rubElHizbstart")
        self.edit("LOW SEEN", "seenlow")
        self.edit("PLACE OF SAJDAH", 'Sajdah')
        self.edit("EMPTY CENTRE LOW STOP", "stopabove")
        self.edit("EMPTY CENTRE HIGH STOP", "stopbelow")
        self.edit("ROUNDED HIGH STOP WITH FILLED CENTRE", 'stopblackabove')
        self.edit("ARABIC SMALL HIGH DOTLESS HEAD OF KHAH", "khahdotlessabove")
        self.edit("ARABIC SMALL LOW MEEM", "meembelow")
        self.edit("MARK NOON GHUNNA", "noonghunnamark")
        self.edit("WITH INVERTED V", "vinverted")
        self.edit("INVERTED", 'inverted')
        self.edit("SUPERSCRIPT", "above")

        self.edit("EXTENDED", "Far")
        self.replace("ARABIC")

        lowercaseOk = True
        self.replace("ZERO WIDTH NO-BREAK SPACE", "zerowidthnbspace")
        self.edit("AFGHANI SIGN", "afghani")
        self.edit("UIGHUR", "uighur")
        self.edit("KAZAKH", "kazakh")
        self.edit("KIRGHIZ", "kirghiz")
        self.edit("FARSI", "farsi")

        self.edit("SMALL HIGH", "small", "above")
        if self.has("LETTER"):
            self.replace("LETTER")
        if self.has('LIGATURE'):
            self.replace("LIGATURE")
        self.edit('INITIAL FORM', ".init")
        self.edit('MEDIAL FORM', ".medi")
        self.edit('FINAL FORM', ".fina")
        self.edit('ISOLATED FORM', ".isol")
        self.replace("QUESTION MARK", "question")
        self.edit("SIGN SANAH", "Sanah")
        self.edit("FOOTNOTE MARKER", "Footnote")
        if self.has("LIGATURE"):
            self.replace("WITH", "_")
        else:
            self.replace("WITH", "")
        self.replace("SALLALLAHOU ALAYHE WASALLAM", "sallallahou_alayhe_wasallam")
        if self.replace("BISMILLAH AR-RAHMAN AR-RAHEEM", "bismillah_arRahman_arRaheem"):
            lowercaseOk = False
        if lowercaseOk:
            self.lower()
        self.compress()

    def processBoxDrawing(self):
        if self.verbose:
            print "processBoxDrawing"
        self.scriptTag = self.languageTags['boxdrawings']
        self.replace("BOX DRAWINGS")
        self.replace("AND")
        self.replace("TO")
        self.replace("VERTICAL", "vert")
        self.replace("HORIZONTAL", "horz")
        self.replace("DIAGONAL", "diag")
        self.replace("DOUBLE", "dbl")
        self.replace("TRIPLE", "trpl")
        self.replace("QUADRUPLE", "quad")
        self.replace("QUAD", "quad")
        self.replace("UPPER", "up")
        self.replace("SINGLE", "sng")
        self.replace("DOWN", "dn")
        self.replace("LOWER", "dn")
        self.lower()
        self.compress()

    def processCyrillic(self):
        if self.verbose:
            print "processCyrillic"
        self.scriptTag = self.languageTags['cyrillic']
        if self.has("CYRILLIC"):
            self.replace("CYRILLIC")
        self.replace("CAPITAL LIGATURE EN GHE", "En_Ghe")
        self.replace("SMALL LIGATURE EN GHE", "en_ghe")
        self.replace("CAPITAL LIGATURE A IE", "A_IE")
        self.replace("SMALL LIGATURE A IE", "a_ie")
        self.processShape()
        self.processDiacritics()
        self.edit("IOTIFIED", "iotified")
        if self.has("HARD SIGN"):
            self.replace("HARD SIGN", "hard")
        if self.has("SOFT SIGN"):
            self.replace("SOFT SIGN", "soft")
        self.edit("COMBINING", "comb")
        if self.has("SMALL LIGATURE"):
            self.replace("SMALL LIGATURE", "ligsmall")
        elif self.has("CAPITAL LIGATURE"):
            self.replace("CAPITAL LIGATURE", "liga")
        if self.has("PALOCHKA"):
            self.replace("PALOCHKA", "Palochka")
        self.edit("KOMI", 'komi')
        self.edit("BYELORUSSIAN-UKRAINIAN", "ukran")
        self.edit("UKRAINIAN", "ukran")
        self.edit("ABKHASIAN", "abkhaz")
        self.edit("BASHKIR", "bashkir")
        self.edit("KHAKASSIAN", "khakas")
        self.edit("ALEUT", "aleut")

        # hard exceptions, or, further coding
        if self.has("HUNDRED THOUSANDS SIGN"):
            self.replace("HUNDRED THOUSANDS SIGN", "hundredthousands")
        if self.has("MILLIONS SIGN"):
            self.replace("MILLIONS SIGN", "millions")
        if self.has("THOUSANDS SIGN"):
            self.replace("THOUSANDS SIGN", "thousands")
        if self.has("POKRYTIE"):
            self.replace("POKRYTIE", "pokrytie")
        if self.has("PALATALIZATION"):
            self.replace("PALATALIZATION", "palatalization")
        self.edit("DASIA PNEUMATA", "dasia", "pneumata")
        self.edit("PSILI PNEUMATA", "psili", "pneumata")
        if self.has("WITH"):
            self.replace("WITH")
        self.handleCase()
        self.compress()

    def processMisc(self):
        if self.verbose:
            print "processMisc"
        # appear in the arabic list
        self.replace("ORNATE LEFT PARENTHESIS", "parenthesisornateleft")
        self.replace("ORNATE RIGHT PARENTHESIS", "parenthesisornateright")
        if self.has("RIAL SIGN"):
            if self.replace("RIAL SIGN"):
                self.suffix("rial")

    def processCJK(self):
        self.scriptTag = self.languageTags['CJK']
        self.uniNameProcessed = self.uniName.replace(" ", "")
        self.uniNameProcessed = self.uniNameProcessed.replace("-", "_")
        self.lower()

    def processKatakanaHiragana(self):
        self.scriptTag = self.languageTags['japan']
        self.condense("COMBINING KATAKANA-HIRAGANA VOICED SOUND MARK")
        self.condense("COMBINING KATAKANA-HIRAGANA SEMI-VOICED SOUND MARK")
        self.edit("KATAKANA-HIRAGANA VOICED SOUND MARK", 'voicedmarkkana')
        self.edit("KATAKANA-HIRAGANA SEMI-VOICED SOUND MARK", 'semivoicedmarkkana')
        self.edit("KATAKANA ITERATION MARK", "iterationkatakana")
        self.edit("KATAKANA VOICED ITERATION MARK", "voicediterationkatakana")
        self.edit("HIRAGANA VOICED ITERATION MARK", 'voicediterationhiragana')
        self.edit("HIRAGANA ITERATION MARK", "iterationhiragana")
        self.condense("KATAKANA-HIRAGANA DOUBLE HYPHEN")
        self.edit("KATAKANA-HIRAGANA PROLONGED SOUND MARK", 'prolongedkana')
        
        self.edit("MIDDLE DOT", 'dot')
        self.edit("SMALL", "small")
        self.edit("DIGRAPH", "digraph")
        self.edit("KATAKANA", "katakana")
        self.edit("HIRAGANA", "hiragana")
        self.edit("LETTER", "")
        self.compress()
        self.lower()

    def processHangul(self):
        self.scriptTag = self.languageTags['hangul']
        if self.has("HANGUL SYLLABLE"):
            self.replace("HANGUL SYLLABLE")
        self.lower()
        self.compress()

    def processLatin(self):
        if self.verbose:
            print "processLatin"
        # compatible with AGD
        self.edit("LATIN CAPITAL LETTER T WITH STROKE", "Tbar")
        self.edit("LATIN SMALL LETTER T WITH STROKE", "tbar")
        self.edit("WITH DOUBLE ACUTE", "hungarumlaut")
        self.edit("LATIN CAPITAL LETTER O WITH STROKE", "Oslash")
        self.edit("LATIN SMALL LETTER O WITH STROKE", "oslash")
        self.edit("LATIN CAPITAL LETTER H WITH STROKE", "Hbar")
        self.edit("LATIN SMALL LETTER H WITH STROKE", "hbar")
        self.edit("LATIN CAPITAL LETTER D WITH STROKE", "Dcroat")
        self.edit("LATIN SMALL LETTER D WITH STROKE", "dcroat")
        self.edit("LATIN SMALL LETTER F WITH HOOK", "florin")
        self.edit("CIRCUMFLEX ACCENT", "asciicircum")
        self.edit("LATIN CAPITAL LETTER O WITH MIDDLE TILDE", "Obar")
        self.edit("LATIN CAPITAL LETTER L WITH STROKE", "Lslash")
        self.edit("LATIN SMALL LETTER L WITH STROKE", "lslash")
        self.edit("LATIN CAPITAL LETTER UPSILON", self.languageTags['latin']+"-upsilon")
        self.edit("LATIN CAPITAL LETTER IOTA", self.languageTags['latin']+"-iota")
        self.edit("LATIN CAPITAL LETTER GAMMA", self.languageTags['latin']+"-gamma")
        self.replace("SOFT HYPHEN", "hyphensoft")
        # sort these before anything else
        self.replace("BROKEN BAR", "brokenbar")
        self.replace("LATIN LETTER WYNN", "wynn")
        self.replace("LATIN LETTER DENTAL CLICK", "clickdental")
        self.replace("LATIN LETTER LATERAL CLICK", "clicklateral")
        self.replace("LATIN LETTER ALVEOLAR CLICK", "clickalveolar")
        self.replace("LATIN LETTER RETROFLEX CLICK", "clickretroflex")
        self.replace("LATIN LETTER INVERTED GLOTTAL STOP WITH STROKE", 'glottalinvertedstroke')
        self.replace("LATIN CAPITAL LETTER SMALL Q WITH HOOK TAIL", "Qsmallhooktail")
        self.replace("LATIN SMALL LETTER AE", "ae")   # case gets wrong
        self.replace("LATIN CAPITAL LETTER AE", "AE")   # case gets wrong
        self.replace("LATIN SMALL LETTER DOTLESS I", "dotlessi")
        self.replace("SMALL LIGATURE OE", "oe")
        self.replace("CAPITAL LIGATURE OE", "OE")
        self.replace("CAPITAL LIGATURE IJ", "IJ")
        self.replace("SMALL LIGATURE IJ", "ij")
        self.replace("LATIN SMALL LETTER DOTLESS J", "dotlessj")
        self.replace("LATIN LETTER TWO WITH STROKE", "twostroke")
        self.replace("COPYRIGHT SIGN", "copyright")  # triggers "right"
        self.edit("LEFT-POINTING DOUBLE ANGLE QUOTATION MARK", "guillemet","left")  # or guillemot ?
        self.edit("RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK", "guillemet","right")  # or guillemot ?
        self.replace("FEMININE ORDINAL INDICATOR", "ordfeminine")
        self.replace("MASCULINE ORDINAL INDICATOR", "ordmasculine")
        self.replace("FULL STOP", "period")
        self.replace("LOW LINE", "underscore")
        # self.replace("LATIN CAPITAL LETTER O WITH CIRCUMFLEX AND HOOK ABOVE", "Ocircumflexhookabove")
        # self.replace("LATIN SMALL LETTER O WITH CIRCUMFLEX AND HOOK ABOVE", "ocircumflexhookabove")
        # self.replace("LATIN CAPITAL LETTER E WITH CIRCUMFLEX AND HOOK ABOVE", "Ecircumflexhookabove")
        # self.replace("LATIN SMALL LETTER E WITH CIRCUMFLEX AND HOOK ABOVE", "ecircumflexhookabove")
        self.replace("LATIN CAPITAL LETTER O WITH MIDDLE TILDE", "Omiddletilde")
        self.replace("LATIN CAPITAL LETTER O WITH OGONEK AND MACRON", "Oogonekmacron")
        self.replace("LATIN SMALL LETTER O WITH OGONEK AND MACRON", "oogonekmacron")
        self.replace("LATIN CAPITAL LETTER A WITH RING ABOVE AND ACUTE",  "Aringacute")
        self.replace("LATIN SMALL LETTER A WITH RING ABOVE AND ACUTE",  "aringacute")
        self.replace("LATIN CAPITAL LETTER O WITH STROKE AND ACUTE", "Oslashacute")
        self.replace("LATIN SMALL LETTER O WITH STROKE AND ACUTE", "oslashacute")
        self.replace("LATIN LETTER REVERSED ESH LOOP", "eshreversedloop")
        self.replace("LATIN CAPITAL LETTER MIDDLE-WELSH LL", "LLmiddlewelsh")
        self.replace("LATIN SMALL LETTER MIDDLE-WELSH LL", "llmiddlewelsh")
        self.edit("MIDDLE-WELSH", "middlewelsh")
        self.edit("WITH LONG RIGHT LEG", "long", "right", "leg")
        self.edit("AFRICAN", "african")
        self.edit("TURNED", "turned")
        self.edit("OPEN", "open")
        self.replace("OPEN O", "")
        self.edit("ACUTE ACCENT", "acute")
        self.edit("CIRCUMFLEX ACCENT", "circumflex")
        self.edit("GRAVE ACCENT", "grave")
        self.edit("STOP", "stop")
        self.edit("DIGRAPH", "digraph")
        self.replace('LATIN LETTER YR', "yr")
        self.edit("LATIN CAPITAL LETTER DZ WITH CARON", "D", "Z", "caron")
        self.edit("LATIN CAPITAL LETTER D WITH SMALL LETTER Z", "Dz")
        self.edit("LATIN CAPITAL LETTER DZ", "DZ")
        self.edit("WITH SMALL LETTER Z WITH CARON", "z", "caron")
        self.edit("LATIN CAPITAL LETTER LJ", "LJ")
        self.edit("LATIN SMALL LETTER LJ", "lj")
        self.edit("LATIN CAPITAL LETTER L WITH SMALL LETTER J", "Lj")
        self.edit("LATIN CAPITAL LETTER NJ", "NJ")
        self.edit("LATIN CAPITAL LETTER N WITH SMALL LETTER J", "Nj")
        self.edit("QUOTATION MARK", "quotedbl")

        # process
        self.processShape()
        self.edit("LATIN")
        self.scriptTag = self.languageTags['latin']
        self.processDiacritics()

        if self.has("SHARP S"):
            self.replace("SHARP S", "germandbls")
        # hard exceptions
        self.replace("COMMERCIAL AT", "at")
        self.edit("NO-BREAK SPACE", "nbspace")
        self.edit("SPACE", "space")
            # INVERTED QUESTION MARK
        self.replace("EXCLAMATION MARK", "exclam")
        self.replace("QUESTION MARK", "question")
        self.replace("NUMBER SIGN", "numbersign")
        self.replace("DOLLAR SIGN", "dollar")
        self.replace("PERCENT SIGN", "percent")
        self.replace("PLUS SIGN", "plus")
        self.replace("SEMICOLON", "semicolon")
        self.replace("MULTIPLICATION SIGN", "multiply")
        self.replace("DIVISION SIGN", "divide")
        self.replace("COLON", "colon")
        self.replace("COMMA", "comma")
        self.replace("EQUALS SIGN", "equal")
        self.replace("LESS-THAN SIGN", "less")
        self.replace("GREATER-THAN SIGN", "greater")
        self.replace("REVERSE SOLIDUS", "backslash")
        self.replace("SOLIDUS", "slash")
        self.replace("VERTICAL LINE", "bar")
        self.replace("HYPHEN-MINUS", "hyphen")
        self.replace("AMPERSAND", "ampersand")
        self.replace("ASTERISK", "asterisk")
        self.replace("APOSTROPHE", "quotesingle")
        self.replace("NOT SIGN", "logicalnot")
        self.replace("REGISTERED SIGN", "registered")
        self.replace("DEGREE SIGN", "degree")
        self.replace("PLUS-MINUS SIGN", "plusminus")
        self.replace("SUPERSCRIPT ONE", "onesuperior")
        self.replace("SUPERSCRIPT TWO", "twosuperior")
        self.replace("SUPERSCRIPT THREE", "threesuperior")
        self.replace("MICRO SIGN", "mu.math")
        self.replace("PILCROW SIGN", "paragraph")
        self.replace("MIDDLE DOT", 'periodcentered')
        self.replace("VULGAR FRACTION ONE QUARTER", "onequarter")
        self.replace("VULGAR FRACTION ONE HALF", "onehalf")
        self.replace("VULGAR FRACTION THREE QUARTERS", "threequarters")

        self.replace("SQUARE BRACKET", "bracket")
        self.replace("CURLY BRACKET", "brace")
        self.replace("PARENTHESIS", "parenthesis")
        if self.has("LEFT"):
            self.replace("LEFT")
            self.suffix("left")
        if self.has("RIGHT") and not self.has("COPYRIGHT"):
            self.replace("RIGHT")
            self.suffix("right")

        # digits
        self.replace("DIGIT ZERO", "zero")  
        self.replace("ZERO", "zero")  
        self.replace("DIGIT ONE", "one")   
        self.replace("ONE", "one")   
        self.replace("DIGIT TWO", "two")
        self.replace("TWO", "two")
        self.replace("DIGIT THREE", "three")
        self.replace("THREE", "three")
        self.replace("DIGIT FOUR", "four")  
        self.replace("FOUR", "four")  
        self.replace("DIGIT FIVE", "five")  
        self.replace("FIVE", "five")  
        self.replace("DIGIT SIX", "six")   
        self.replace("SIX", "six")   
        self.replace("DIGIT SEVEN", "seven")
        self.replace("SEVEN", "seven")
        self.replace("DIGIT EIGHT", "eight")
        self.replace("EIGHT", "eight")
        self.replace("DIGIT NINE", "nine")
        self.replace("NINE", "nine")

        self.replace("CENT SIGN", "cent")
        self.replace("POUND SIGN", "sterling")
        self.replace("CURRENCY SIGN", "currency")
        self.replace("YEN SIGN", "yen")
        self.replace("SECTION SIGN", "section")

        if self.has("INVERTED"):
            if self.replace("INVERTED"):
                self.suffix("down")

        if self.has("AND"):
            self.replace("AND")
        self.handleCase()
        self.compress()

    def processHebrew(self):
        self.scriptTag = self.languageTags['hebrew']

        self.replace("HEBREW LIGATURE YIDDISH DOUBLE VAV", "vav_vav")   # yiddish ?
        self.replace("HEBREW LIGATURE YIDDISH VAV YOD", "vav_yod")  # yiddish ?
        self.replace("HEBREW LIGATURE YIDDISH DOUBLE YOD", "yod_yod")
        self.replace("HEBREW MARK UPPER DOT", "dotupper")
        self.replace("HEBREW MARK LOWER DOT", "dotlower")
        self.edit("ACCENT", "accent")
        self.edit("FINAL", ".fina")    # .fina
        self.edit("POINT", "pt")   # point?
        if self.has("YIDDISH"):
            if self.replace("YIDDISH"):
                self.suffix("yiddish")
        if self.has("PUNCTUATION"):
            self.replace("PUNCTUATION")

        self.edit("HEBREW LETTER")
        self.edit('HEBREW')
        self.edit("LETTER")

        self.lower()
        self.compress()

    def processIPA(self):
        self.scriptTag = self.languageTags['ipa']
        self.processCase()

        self.edit("LATIN")
        self.edit("GREEK")
        self.edit("INVERTED", "inverted")
        # self.edit("MODIFIER LETTER", "modifier")
        self.replace('LETTER PHARYNGEAL VOICED FRICATIVE', "pharyngealvoicedfricative")
        self.edit("LETTER VOICED LARYNGEAL SPIRANT", "laryngealvoicedspirant")
        if self.has('BILABIAL PERCUSSIVE'):
            if self.replace("BILABIAL PERCUSSIVE"):
                self.suffix("percussivebilabial")
                self.replace("LETTER")

        if self.has('BIDENTAL PERCUSSIVE'):
            if self.replace("BIDENTAL PERCUSSIVE"):
                self.suffix("percussivebidental")
                self.replace("LETTER")

        if self.has('BILABIAL CLICK'):
            if self.replace("BILABIAL CLICK"):
                self.suffix("clickbilabial")
                self.replace("LETTER")

        if self.has("GLOTTAL STOP"):
            if self.replace("GLOTTAL STOP"):
                self.suffix("glottal")
                # self.suffix("stop")
                self.replace("LETTER")

        if self.has("WITH MIDDLE TILDE"):
            if self.replace("WITH MIDDLE TILDE"):
                self.suffix('middle')
                self.suffix('tilde')

        if self.has("WITH FISHHOOK"):
            if self.replace("WITH FISHHOOK"):
                self.suffix("fishhook")

        if self.has("SQUAT REVERSED"):
            if self.replace("SQUAT REVERSED"):
                self.suffix("squat")
                self.suffix("reversed")

        if self.has("AND TAIL"):
            if self.replace("AND TAIL"):
                self.suffix("tail")

        if self.has("TURNED"):
            if self.replace("TURNED"):
                self.suffix("turned")

        self.edit("STRETCHED", "stretch")
        self.processShape()
        self.processDiacritics()
        self.edit("LETTER AIN", "Ain")
        self.edit("WITH CROSSED-TAIL", "crossedtail")
        self.edit("STRETCHED", "stretched")
        self.edit("OPEN", "open")
        self.edit("DOTLESS", "dotless")
        self.edit("GREEK SUBSCRIPT", "greek", "subscript")
        self.edit("SUBSCRIPT", "subscript")
        self.edit("CYRILLIC", 'cyrillic')
        self.edit("HORN", "horn") # roundabout case change
        self.edit("WITH LONG LEG", "longleg")
        self.edit("WITH BELT", "belt")
        self.edit("DIAERESIZED", self.prefSpelling_dieresis)        
        self.handleCase()
        self.replace("DIGRAPH")
        self.replace("LETTER")
        self.compress()

    def processGreek(self):
        self.scriptTag = self.languageTags['greek']
        self.replace("GREEK")
        self.replace("UPSILON WITH HOOK SYMBOL", "upsilonhooksymbol")
        self.replace("UPSILON WITH ACUTE AND HOOK SYMBOL", "upsilonacutehooksymbol")
        self.replace("UPSILON WITH DIAERESIS AND HOOK SYMBOL", "upsilondieresishooksymbol")
        self.replace("SMALL REVERSED LUNATE SIGMA SYMBOL", "sigmalunatereversedsymbol")
        self.replace("SMALL DOTTED LUNATE SIGMA SYMBOL", "sigmalunatedottedsymbol")
        self.replace("SMALL REVERSED DOTTED LUNATE SIGMA SYMBOL", "sigmalunatedottedreversedsymbol")
        self.replace("LUNATE SIGMA SYMBOL", "sigmalunatesymbol")
        self.replace("LUNATE EPSILON SYMBOL", "epsilonlunatesymbol")
        self.replace("RHO WITH STROKE SYMBOL", "rhostrokesymbol")
        self.replace("ANO TELEIA", "anoteleia")

        self.replace("DIGAMMA", "Digamma")
        self.replace("KOPPA", "Koppa")
        self.replace("LETTER STIGMA", "Stigma")
        self.replace("LETTER SAMPI", "Sampi")
        self.replace("YOT", "yot")

        self.edit("COPTIC", "coptic")
        self.edit("LUNATE", "lunate")
        self.edit("LETTER ARCHAIC", "archaic")

        self.processShape()
        self.processDiacritics()

        self.replace("QUESTION MARK", "question")

        self.edit("NUMERAL SIGN", "numeral", "sign")
        self.edit("LOWER", "lower")
        self.edit("FINAL", "final")
        self.edit("WITH HOOK", "hook")

        self.edit("UPSILON SYMBOL", "upsilonsymbol")
        self.edit("PHI SYMBOL", "phi.math")
        self.edit("CAPITAL KAI SYMBOL", "Kaisymbol")
        self.edit("KAI SYMBOL", "kaisymbol")
        self.edit("PI SYMBOL", "pi.math")
        self.edit("THETA SYMBOL", "theta.math")
        self.edit("BETA SYMBOL", "betasymbol")
        self.edit("UPSILON SYMBOL", "upsilonsymbol")
        self.edit("KAPPA SYMBOL", "kappa.math")
        self.edit("RHO SYMBOL", "rhosymbol")
        if self.has("SIGMA SYMBOL"):
            if self.replace("SYMBOL"):
                self.suffix("symbol")

        # with / and 
        parts = ['PROSGEGRAMMENI',
            'YPOGEGRAMMENI',
            'PERISPOMENI',
            'VARIA',
            'PSILI',
            'DIALYTIKA',
            'VRACHY',
            'OXIA',
            'DASIA',
            "TONOS"
        ]


        for p in parts:
            if self.has("WITH "+p):
                if self.replace("WITH "+p):
                    self.suffix(p.lower())
        for p in parts:
            if self.has("AND "+p):
                if self.replace("AND "+p):
                    self.suffix(p.lower())
        for p in parts:
            self.replace(p, p.lower())

        # Aha!
        # print "voor", self.suffixParts
        self.editSuffix("ypogegrammeni", "iotasub")
        self.editSuffix("prosgegrammeni", "iotasub")
        self.editSuffix("koronis", "lenis")
        self.editSuffix("psili", "lenis")
        self.editSuffix("dasia", "asper")
        self.editSuffix("dialytika", "dieresis")
        self.editSuffix("varia", "grave")
        self.editSuffix("oxia", "acute")
        self.editSuffix("vrachy", "breve")
        self.editSuffix("perispomeni", "tilde")
        # print "\tna", self.suffixParts

        self.replace("KORONIS", "koronis")
        self.replace("LETTER")
        self.handleCase()
        self.compress()

    def processPrivateUse(self):
        self.uniNameProcessed = "privateUseArea_%04x"%self.uniNumber

    def _arrowAsNumber(self):
        self.uniNameProcessed = "arrow_%04x"%self.uniNumber

    def processArrows(self):

        # handle all the harpoon + barb names
        # Difficult to make a shorter name without losing information
        # LEFTWARDS HARPOON WITH BARB UP ABOVE LEFTWARDS HARPOON WITH BARB DOWN
        # UPWARDS HARPOON WITH BARB LEFT BESIDE UPWARDS HARPOON WITH BARB RIGHT
        # RIGHTWARDS HARPOON WITH BARB UP ABOVE RIGHTWARDS HARPOON WITH BARB DOWN
        # DOWNWARDS HARPOON WITH BARB LEFT BESIDE DOWNWARDS HARPOON WITH BARB RIGHT
        # LEFTWARDS HARPOON WITH BARB UP ABOVE RIGHTWARDS HARPOON WITH BARB UP
        # LEFTWARDS HARPOON WITH BARB DOWN ABOVE RIGHTWARDS HARPOON WITH BARB DOWN
        # RIGHTWARDS HARPOON WITH BARB UP ABOVE LEFTWARDS HARPOON WITH BARB UP
        # RIGHTWARDS HARPOON WITH BARB DOWN ABOVE LEFTWARDS HARPOON WITH BARB DOWN
        # etc.
        if  0x21b6 <= self.uniNumber <= 0x297b:
            self._arrowAsNumber()
            return

        self.edit("RIGHT-SIDE ARC CLOCKWISE ARROW", "rightsidearcclockwisearrow")
        self.edit("LEFT-SIDE ARC ANTICLOCKWISE ARROW", "leftsidearcanticlockarrow")
        self.edit("TOP ARC ANTICLOCKWISE ARROW", "toparcanticlockarrow")
        self.edit("BOTTOM ARC ANTICLOCKWISE ARROW", "bottomarcanticlockarrow")
        self.edit("TOP ARC CLOCKWISE ARROW WITH MINUS", "toparcclockarrowminus")
        self.condense("GAPPED CIRCLE ARROW")
        self.edit("CLOCKWISE ARROW", "clockarrow")
        self.edit("ANTICLOCKWISE ARROW", "anticlockarrow")
        self.edit("WITH MINUS", "minus")
        self.edit("WITH PLUS", "plus")
        self.condense("SEMICIRCULAR")

        self.edit("RISING DIAGONAL CROSSING FALLING DIAGONAL", "risingdiagonalXfallingdiagonal")
        self.edit("FALLING DIAGONAL CROSSING RISING DIAGONAL", "fallingdiagonalXrisingdiagonal")

        self.edit("ARROW POINTING RIGHTWARDS THEN CURVING UPWARDS", 'arrowrightthencurveup')
        self.edit("ARROW POINTING RIGHTWARDS THEN CURVING DOWNWARDS", 'arrowrightthendown')
        self.edit("ARROW POINTING DOWNWARDS THEN CURVING LEFTWARDS", 'arrowdownthenleft')
        self.edit("ARROW POINTING DOWNWARDS THEN CURVING RIGHTWARDS", 'arrowdownthenright')

        self.edit("UPWARDS HARPOON", "harpoonup")
        self.edit("DOWNWARDS HARPOON", "harpoondown")
        self.edit("LEFTWARDS HARPOON", "harpoonleft")
        self.edit("RIGHTWARDS HARPOON", "harpoonright")

        # self.edit("WITH BARB", "barb")
        self.edit("THREE RIGHTWARDS ARROWS", "threerightarrows")
        self.edit("RISING DIAGONAL CROSSING SOUTH EAST ARROW", "risingdiagonalXSEarrow")
        self.edit("WAVE ARROW POINTING DIRECTLY RIGHT", "wavearrowright")
        self.edit("NORTH EAST ARROW CROSSING NORTH WEST ARROW", "NEarrowXNWarrow")
        self.edit("SOUTH EAST ARROW CROSSING NORTH EAST ARROW", "SEarrowXNEarrow")
        self.edit("NORTH EAST ARROW CROSSING SOUTH EAST ARROW", "NEarrowXSEarrow")
        self.edit("NORTH WEST ARROW CROSSING NORTH EAST ARROW", "NEarrowXNEarrow")
        self.edit("LEFTWARDS HARPOON OVER RIGHTWARDS HARPOON", "leftharpoonoverrightharpoon")
        self.edit("RIGHTWARDS HARPOON OVER LEFTWARDS HARPOON", "rightharpoonoverleftharpoon")
        self.edit("RIGHTWARDS ARROW OVER LEFTWARDS ARROW", "rightarrowoverleftarrow")
        self.edit("UPWARDS ARROW LEFTWARDS OF DOWNWARDS ARROW", "uparrowleftofdownarrow")
        self.edit("DOWNWARDS ARROW LEFTWARDS OF UPWARDS ARROW", "downwarrowleftofuparrow")
        self.edit("LEFTWARDS ARROW OVER RIGHTWARDS ARROW", "leftarrowoverrightarrow")
        self.edit("PAIRED ARROWS", "arrowspaired")

        self.edit("WITH DOUBLE STROKE", "dblstroke")
        self.edit("WITH VERTICAL STROKE", "verticalstroke")
        self.edit("WITH DOUBLE VERTICAL STROKE", "verticalstroke")
        self.edit("WITH HORIZONTAL BAR", "horizontalbar")
        self.edit("WITH VERTICAL BAR", "verticalbar")
        self.edit("FALLING DIAGONAL CROSSING", "fallingdiagonalx")
        self.edit("ARROW-TAIL", "arrowtail")
        self.edit("FISH TAIL", 'fishtail')
        self.edit("OPEN-HEADED", "openhead")
        self.edit("TRIPLE ARROW", "triplearrow")
        self.edit("DOUBLE DASH ARROW", "dbldasharrow")
        self.edit("WHITE DOUBLE ARROW", "whitedblarrow")
        self.edit("DOUBLE", "dbl")
        self.edit("QUADRUPLE ARROW", "quadarrow")
        self.edit("WHITE ARROW", "whitearrow")
        self.edit("ON PEDESTAL", "onpedestal")
        self.edit("FROM WALL", "fromwall")
        self.edit("TO CORNER", "tocorner")
        self.edit("ARROW", "arrow")

        self.edit("LONG", "long")
        self.edit("LEFTWARDS", "left")
        self.edit("UPWARDS", "up")
        self.edit("RIGHTWARDS", "right")
        self.edit("DOWNWARDS", "down")
        self.edit("LEFT RIGHT", "leftright")
        self.edit("UP DOWN", "updown")
        self.edit("SQUIGGLE", "squiggle")
        self.edit("TRIPLE DASH", "tripledash")
        self.edit("DASHED", "dashed")
        self.edit("NORTH WEST", "NW")
        self.edit("NORTH EAST", "NE")
        self.edit("SOUTH WEST", "SW")
        self.edit("SOUTH EAST", "SE")
        self.edit("NORTH", "N")
        self.edit("WEST", "W")
        self.edit("SOUTH", "S")
        self.edit("EAST", "E")
        self.edit("WITH STROKE", 'stroke')
        self.edit("TWO HEADED", "twoheaded")
        self.edit("TWO-HEADED", "twoheaded")
        self.edit("WITH DIAGONAL STROKE", "diagonalstroke")
        self.edit("WITH HORIZONTAL STROKE", "horizontalstroke")
        self.edit("WITH CIRCLED PLUS", "circledplus")
        self.edit("WITH TAIL", "tail")
        self.edit("WAVE", 'wave')
        self.edit("TO BAR", "tobar")
        self.edit("FROM BAR", "frombar")
        self.edit("WITH BASE", "withbase")
        self.edit("WITH HOOK", "hook")
        self.edit("WITH LOOP", "loop")
        self.edit("ZIGZAG", "zigzag")
        self.edit("WITH TIP", "tip")
        self.edit("WITH CORNER", "corner")
        self.edit("WITH DOTTED STEM", "dottedstem")
        self.edit("TO BLACK DIAMOND", "blackdiamond")
        self.edit("RIGHT", "right")
        self.edit("LEFT", "left")
        self.edit("UP", "up")
        self.edit("DOWN", "down")
        self.edit("AND", "")

        self.edit("THROUGH X", "thruX")
        self.edit("WITH SMALL CIRCLE", "smallcircle")
        self.edit("THROUGH SMALL CIRCLE", "thrusmallcircle")
        self.edit("ANTICLOCKWISE CLOSED CIRCLE", "anticlockwiseclosedcircle")
        self.edit("CLOCKWISE CLOSED CIRCLE", "clockwiseclosedcircle")
        self.edit("ABOVE ALMOST EQUAL TO", "abovealmostequal")
        self.edit("ABOVE TILDE OPERATOR", 'tildeabove')
        self.edit("TILDE OPERATOR ABOVE", 'tildeabove')

    def processWidths(self):
        self.edit("FULLWIDTH", 'fullwidth')
        self.processLatin()

    def condense(self, part, combiner=""):
        # remove spaces, remove hyphens, change to lowercase
        editPart = part.replace(" ", combiner)
        editPart = editPart.replace("-", "")
        editPart = editPart.lower()
        self.replace(part, editPart)

    def process(self):
        # is this a preferred name
        if self.uniNumber in self.preferredAGLNames:
            self.uniNameProcessed = self.preferredAGLNames[self.uniNumber]
            # print "AGL pref", self.uniNameProcessed
            return
        # nope
        self.processStructure()
        self.processCase()
        self.processMisc()

        self.isCJK = self.uniRangeName in [
            "CJK Unified Ideographs",
            "CJK Unified Ideographs Extension A",
            "CJK Unified Ideographs",
            "CJK Unified Ideographs Extension A",
            "CJK Compatibility",
            "CJK Compatibility Forms",
            "CJK Compatibility Ideographs",
            "CJK Radicals Supplement",
            "CJK Symbols and Punctuation"]


        if self.uniRangeName == "Box Drawing":
            self.processBoxDrawing()
        elif self.uniRangeName in ['Cyrillic', 'Cyrillic Supplementary']:
            self.processCyrillic()
        elif self.uniRangeName in ["Arabic", 'Arabic Presentation Forms-A', 'Arabic Presentation Forms-B']:
            self.processArabic()
        elif self.uniRangeName == "Hebrew":
            self.processHebrew()
        elif self.uniRangeName in ["Basic Latin", 'Latin-1 Supplement', 'Latin Extended-A', 'Latin Extended-B', 'Latin Extended Additional', ]:
            self.processLatin()
        elif self.uniRangeName in ["IPA Extensions", "Phonetic Extensions"]:
            self.processIPA()
        elif self.uniRangeName in ["Hangul Syllables",]:
            self.processHangul()
        elif self.uniRangeName in [ "Katakana", "Katakana Phonetic Extensions", "Hiragana",]:
            self.processKatakanaHiragana()
        elif self.uniRangeName in ["Halfwidth and Fullwidth Forms"]:
            self.processWidths()
        elif self.isCJK and self.includeCJK:
            self.processCJK()
        elif self.uniRangeName in [
                "Arrows",
                "Supplemental Arrows-A",
                "Supplemental Arrows-B",
                ]:
            self.processArrows()
        elif self.uniRangeName in ["Private Use Area"]:
            self.processPrivateUse()
        elif self.uniRangeName in [ "Greek Extended", "Greek and Coptic",]:
            self.processGreek()
        else:
            # catchall
            self.compress()

        if self.verbose:
            print self.uniNameProcessed, self.suffixParts, self.finalParts
        self.uniNameProcessed = self.uniNameProcessed + "".join(self.suffixParts) + "-".join(self.finalParts)
        if self.uniNameProcessed in self.ambiguousNames:
            # the final name has a duplicate in another script
            # take disambiguation action
            self.mustAddScript = True

    def edit(self, pattern, *suffix):
        """
        a method that does the same as this:
        if self.has("PATTERN"):
            if self.replace("PATTERN"):
                self.suffix("suffix")
                self.suffix("suffix")
        """
        if self.has(pattern):
            if self.replace(pattern):
                [self.suffix(s) for s in suffix]

    def getExport(self, name=True, useExtension=False, uniNumber=True, uniName=True):
        # return a string fit for exporting
        t = []
        if name:
            t.append(self.getName(extension=useExtension))
        if uniNumber:
            t.append("%04x"%self.uniNumber)
        if uniName:
            t.append(self.uniName)
        return "\t".join(t)

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

    def editSuffix(self, lookFor, replaceWith):
        for n,i in enumerate(self.suffixParts):
            if i==lookFor:
                self.suffixParts[n]=replaceWith

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

    def __repr__(self):
        return "%s\t\t%05x\t\t%s"%(self.getName(extension=False), self.uniNumber, self.uniName)


skipped = {}
def generateAll(path):
    # generate all the names in the first plane
    lines = []
    uniqueNamesExtension = {}
    uniqueNamesNoExtension = {}
    for uniNumber in range(1, 0xffff):
        glyphName = GlyphName(uniNumber=uniNumber, verbose=False, includeCJK=INCLUDECJK)
        if glyphName.uniRangeName not in show:
            skipped[glyphName.uniRangeName]=True
            continue
        if glyphName.hasName():
            if not INCLUDECJK and glyphName.isCJK:
                continue
            lines.append(glyphName.getExport())
    f = open(path, 'w')
    f.write("\n".join(lines))
    f.close()

def testUniqueNames():
    # test if results are unique
    uniqueNamesExtension = {}
    uniqueNamesNoExtension = {}
    for uniNumber in range(1, 0xffff):
        glyphName = GlyphName(uniNumber=uniNumber, includeCJK=INCLUDECJK)
        if glyphName.hasName():
            # print glyphName.getName(extension=True), glyphName.getName(extension=False)
            thisName = glyphName.getName()
            if not thisName in uniqueNamesExtension:
                uniqueNamesExtension[thisName] = []
            uniqueNamesExtension[thisName].append(glyphName)

            thisName = glyphName.getName(extension=True)
            if not thisName in uniqueNamesNoExtension:
                uniqueNamesNoExtension[thisName] = []
            uniqueNamesNoExtension[thisName].append(glyphName)
    for k, v in uniqueNamesNoExtension.items():
        if len(v) > 1:
            print "Failed unique test without extension:", v

    for k, v in uniqueNamesExtension.items():
        if len(v) > 1:
            print "Failed unique test:", v


def debug(uniNumber):
    # trace the processing of a specific number
    glyphName = GlyphName(uniNumber=uniNumber, verbose=True)
    glyphName.process()
    print "debug %04x"%uniNumber
    print glyphName.getExport()
    for step in glyphName._log:
        print "\t", step

def findCapitals():
    # find all unicode names that refer to CAPITAL or SMALL
    parts = ["CAPITAL", 
        #"SMALL",
        ]
    caseNumbers = []
    for uniNumber in range(1, 0xffff):
        glyphName = GlyphName(uniNumber=uniNumber, verbose=False)


        if glyphName.uniRangeName not in show:
            continue
        for p in parts:
            if glyphName.has(p):
                caseNumbers.append(uniNumber)
    caseNumbers.sort()
    return caseNumbers


if __name__ == "__main__":
    from pprint import pprint

    INCLUDECJK = False

    show = [
        'Hangul Syllables',
        'Private Use Area',
        
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


        # "Halfwidth and Fullwidth Forms"
        # "Alphabetic Presentation Forms",

    ]




    #for n in findCapitals():
    #    print GlyphName(uniNumber=n)
        #print
        #debug(n)

    generateAll("generatedGlyphNames.txt")

    testUniqueNames()

    # check for duplicate names
    # print all the keys 
    # s = skipped.keys()
    # s.sort()
    # print "to do"
    # for cat in s:
    #     if cat in show:
    #         continue
    #     print "\t", cat