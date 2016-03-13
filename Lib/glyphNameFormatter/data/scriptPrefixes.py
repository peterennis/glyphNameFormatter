import os
from xml.etree import ElementTree as ET

from glyphNameFormatter.tools import GlyphNameFormatterError


SCRIPTSEPARATOR = "-"
SCRIPTASPREFIX = True


def loadScripTags():
    data = {}
    path = os.path.dirname(__file__)
    path = os.path.join(path, "scriptTags.html")
    doc = ET.parse(path)
    table = doc.getroot()

    for row in table:
        for i in row[1:]:
            script, tag = [col.text for col in i]
            script = script.strip()
            tag = tag.strip()
            data[script.lower()] = tag
    return data


class ScriptPrefixesDict(dict):

    _fallbackScripPrefixes = loadScripTags()

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
        if key in self._fallbackScripPrefixes:
            return self._fallbackScripPrefixes[key]
        # generate one
        # remove all vowels
        key = [c for c in key if c not in "aeiou -"]
        # return the first four values
        return "".join(key[:4])


def addScriptPrefix(txt, tag=None, script=None, scriptSeparator=SCRIPTSEPARATOR, scriptAsPrefix=SCRIPTASPREFIX):
    if tag is None and script is None:
        raise GlyphNameFormatterError("Need a script or a tag")
    if tag is None:
        tag = scriptPrefixes[script]
    if "%s" not in tag:
        if scriptAsPrefix:
            order = (tag, scriptSeparator)
            tag = "%s%s%%s" % order
        else:
            order = (scriptSeparator, tag)
            tag = "%%s%s%s" % order
    if scriptAsPrefix:
        return tag % txt
    return tag % txt


# script prefixes are abbreviations of a script
# optionally a pattern can be given:
# '%scyr' will add 'cyr' to the end

_scriptPrefixes = {
    'cjk': 'cjk',
    'arabic': 'ar',
    'boxdrawings': 'bxd',
    'cyrillic': '%scyr',
    'greek': 'gr',
    'hangul': 'ko',
    'hebrew': '%%s%shb' % SCRIPTSEPARATOR,
    'hiragana': 'hira',
    'katakana': 'kata',
    'ipa': 'ipa',
    'latin': "lt",
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
        >>> scriptPrefixes["Tai Le"]
        'tale'
        """

    def _testAddScriptPrefix():
        """
        >>> addScriptPrefix("A", "latin", separator="", asPrefix=True)
        'latinA'
        >>> addScriptPrefix("A", "latin", separator="", asPrefix=False)
        'Alatin'
        >>> addScriptPrefix("A", "latin", separator="-", asPrefix=True)
        'latin-A'
        >>> addScriptPrefix("A", "latin", separator="-", asPrefix=False)
        'A-latin'
        >>> addScriptPrefix("A", "latin", separator=":", asPrefix=True)
        'latin:A'
        >>> addScriptPrefix("A", "latin", separator=":", asPrefix=False)
        'A:latin'
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