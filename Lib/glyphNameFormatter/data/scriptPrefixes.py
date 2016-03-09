
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
        key = [c for c in key if c not in "aeiou"]
        # return the first four values
        return "".join(key[:4])

_scriptPrefixes = {
    'cjk': 'cjk',
    'arabic': 'ar',
    'armenian': 'am',
    'boxdrawings': 'bxd',
    'cyrillic': 'cy',
    'devanagari': 'dv',
    'greek': 'gr',
    'hangul': 'ko',
    'hebrew': 'hb',
    'hiragana': 'hi',
    'ipa': 'ipa',
    'kannada': "kn",
    'katakana': 'ka',
    'latin': "lt",
    'mongolian': 'mo',
    'tibetan': 'tb',
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
