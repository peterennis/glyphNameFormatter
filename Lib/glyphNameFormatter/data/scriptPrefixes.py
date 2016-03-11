from glyphNameFormatter.tools import GlyphNameFormatterError

class ScriptPrefixesDict(dict):

    def __getitem__(self, key):
        # get the key
        value = dict.get(self, key, None)
        if value:
            # found it, return it
            return value
        # try with in lower case
        key = key.lower()
        # get the lower case key
        value = dict.get(self, key, None)
        if value:
            # found it, return it
            return value
        # get the existing keys
        existingKeys = dict.keys(self)
        # sort them by reversed lenght
        existingKeys.sort(key=len, reverse=True)
        for existingKey in existingKeys:
            # compare with lower case
            if existingKey.lower() in key:
                # found it
                return dict.__getitem__(self, existingKey)
        # fallback
        # remove all vowels
        key = [c for c in key if c not in "aeiou -"]
        # return the first four values
        return "".join(key[:4])


def addScriptPrefix(txt, tag=None, script=None):
    if tag is None and script is None:
        raise GlyphNameFormatterError("Need a script or a tag")
    if tag is None:
        tag = scriptPrefixes[script]
    if "%s" not in tag:
        tag = "%s-%%s" % tag
    return tag % txt

# script prefixes are abbreviations of a script
# optionally a pattern can be given:
# '%scyr' will add 'cyr' to the end

_scriptPrefixes = {
    'cjk': 'cjk',
    'arabic': 'ar',
    'armenian': 'am',
    'boxdrawings': 'bxd',
    'cyrillic': '%scyr',
    'devanagari': 'dv',
    'ethiopic': "et",
    'greek': 'gr',
    'hangul': 'ko',
    'hebrew': '%s-hb',
    'hiragana': 'hi',
    'ipa': 'ipa',
    'kannada': "kn",
    'katakana': 'ka',
    'javanese': 'ja',
    'malayalam': 'ma',
    'latin': "lt",
    'mongolian': 'mo',
    'tibetan': 'tb',
    'thai': 'ti',
    'miscellaneous': 'misc',
    'musical': 'music',
    'optical character recognition': 'ocr',
    'combining diacritical marks': "cmb",
    'vedic': 've',
}

scriptPrefixes = ScriptPrefixesDict(_scriptPrefixes)

if __name__ == "__main__":
    import doctest

    def _testScriptPrefixes():
        """
        >>> scriptPrefixes["latin"]
        'lt'
        >>> scriptPrefixes["randomScriptName"]
        'rndm'
        >>> scriptPrefixes["Greek and Coptic"]
        'gr'
        >>> scriptPrefixes["Enclosed CJK letters and months"]
        'cjk'
        """

    doctest.testmod()


    def testAllPrefixes():
        # let's not just assume all prefixes that end up the same
        # will also be able to disambiguate names.
        from glyphNameFormatter.unicodeRangeNames import getAllRangeNames
        prefixes = {}
        for n in getAllRangeNames():
            pf = scriptPrefixes[n]
            if not pf in prefixes:
                prefixes[pf] = []
            prefixes[pf].append(n)
        from pprint import pprint
        pprint(prefixes)
    testAllPrefixes()