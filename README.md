# glyphNameFormatter

Experimental system for generating glyph name lists from unicode data. 

* Unicode has long and descriptive names for each character.
* Font editors need glyph names to easily identify the glyphs, short, unique, can't use space
* Raw Unicode names are unsuitable for this purpose in font editors
* Font editors then use their own lists that map names to unicode values.
* These lists only cover the glyphs that were needed in production, so there are often holes in the coverage.
* These lists should not dictate what is useful or not in a font but offer reliable unicode to name mapping.
* Adobe standardized some lists years ago, standard, but incomplete and immutable

### Rules

* Glyph names should, as much as possible, only have script prefixes to disambiguate. Otherwise all names are equal. So `gaf` rather than `arGaf` for `ARABIC LETTER GAF`, or `Uk` rather than `Ukcyrillic` for `CYRILLIC CAPITAL LETTER UK`.
* Script prefixes rather than suffixes to prevent interference with extensions as `.init`.
* Short script prefixes. `cy-Psi` rather than `Psicyrillic`.
* Disambiguation prefixes can be added after clash detection.
* If a name needs to include a language, this is added to the end: `yehfarsi.isol` for	`ARABIC LETTER FARSI YEH ISOLATED FORM`
* If an AGD name has a language but it is not needed for disambiguation and Unicode does not mention it, it can be ignored. For instance `kgreenlandic` can just be	`kra`.

## Making lists

Run `buildRanges.py` to make all the name lists. They will be deposited in `names/`. There will be other methods and other lists, but for now this is the place to make things.
You can also run each of the range scripts in `rangeProcessors/` and they will print a nice readable table with the processed name, unicode value, original name. There is also a column for names from the Adobe AGL if it has a different name for that entry. For instance `basic_latin.py` will generate

`
space                                                                   0020 	SPACE
exclam                                                                  0021 	EXCLAMATION MARK
quotedbl                                                                0022 	QUOTATION MARK
numbersign                                                              0023 	NUMBER SIGN
dollar                                                                  0024 	DOLLAR SIGN
percent                                                                 0025 	PERCENT SIGN
ampersand                                                               0026 	AMPERSAND
quotesingle                                                             0027 	APOSTROPHE
parenleft                                                               0028 	LEFT PARENTHESIS
parenrightright                                    parenright           0029 	RIGHT PARENTHESIS
asterisk                                                                002A 	ASTERISK
plus                                                                    002B 	PLUS SIGN
comma                                                                   002C 	COMMA
hyphen                                                                  002D 	HYPHEN-MINUS
period                                                                  002E 	FULL STOP
slash                                                                   002F 	SOLIDUS
zero                                                                    0030 	DIGIT ZERO
one                                                                     0031 	DIGIT ONE
two                                                                     0032 	DIGIT TWO
three                                                                   0033 	DIGIT THREE
four                                                                    0034 	DIGIT FOUR
five                                                                    0035 	DIGIT FIVE
six                                                                     0036 	DIGIT SIX
seven                                                                   0037 	DIGIT SEVEN
eight                                                                   0038 	DIGIT EIGHT
nine                                                                    0039 	DIGIT NINE
colon                                                                   003A 	COLON
semicolon                                                               003B 	SEMICOLON
less                                                                    003C 	LESS-THAN SIGN
equal                                                                   003D 	EQUALS SIGN
greater                                                                 003E 	GREATER-THAN SIGN
question                                                                003F 	QUESTION MARK
at                                                                      0040 	COMMERCIAL AT
A                                                                       0041 	LATIN CAPITAL LETTER A
B                                                                       0042 	LATIN CAPITAL LETTER B
C                                                                       0043 	LATIN CAPITAL LETTER C
D                                                                       0044 	LATIN CAPITAL LETTER D
E                                                                       0045 	LATIN CAPITAL LETTER E
F                                                                       0046 	LATIN CAPITAL LETTER F
G                                                                       0047 	LATIN CAPITAL LETTER G
H                                                                       0048 	LATIN CAPITAL LETTER H
I                                                                       0049 	LATIN CAPITAL LETTER I
J                                                                       004A 	LATIN CAPITAL LETTER J
K                                                                       004B 	LATIN CAPITAL LETTER K
L                                                                       004C 	LATIN CAPITAL LETTER L
M                                                                       004D 	LATIN CAPITAL LETTER M
N                                                                       004E 	LATIN CAPITAL LETTER N
O                                                                       004F 	LATIN CAPITAL LETTER O
P                                                                       0050 	LATIN CAPITAL LETTER P
Q                                                                       0051 	LATIN CAPITAL LETTER Q
R                                                                       0052 	LATIN CAPITAL LETTER R
S                                                                       0053 	LATIN CAPITAL LETTER S
T                                                                       0054 	LATIN CAPITAL LETTER T
U                                                                       0055 	LATIN CAPITAL LETTER U
V                                                                       0056 	LATIN CAPITAL LETTER V
W                                                                       0057 	LATIN CAPITAL LETTER W
X                                                                       0058 	LATIN CAPITAL LETTER X
Y                                                                       0059 	LATIN CAPITAL LETTER Y
Z                                                                       005A 	LATIN CAPITAL LETTER Z
bracketleft                                                             005B 	LEFT SQUARE BRACKET
backslash                                                               005C 	REVERSE SOLIDUS
bracketright                                                            005D 	RIGHT SQUARE BRACKET
asciicircum                                                             005E 	CIRCUMFLEX ACCENT
underscore                                                              005F 	LOW LINE
grave                                                                   0060 	GRAVE ACCENT
a                                                                       0061 	LATIN SMALL LETTER A
b                                                                       0062 	LATIN SMALL LETTER B
c                                                                       0063 	LATIN SMALL LETTER C
d                                                                       0064 	LATIN SMALL LETTER D
e                                                                       0065 	LATIN SMALL LETTER E
f                                                                       0066 	LATIN SMALL LETTER F
g                                                                       0067 	LATIN SMALL LETTER G
h                                                                       0068 	LATIN SMALL LETTER H
i                                                                       0069 	LATIN SMALL LETTER I
j                                                                       006A 	LATIN SMALL LETTER J
k                                                                       006B 	LATIN SMALL LETTER K
l                                                                       006C 	LATIN SMALL LETTER L
m                                                                       006D 	LATIN SMALL LETTER M
n                                                                       006E 	LATIN SMALL LETTER N
o                                                                       006F 	LATIN SMALL LETTER O
p                                                                       0070 	LATIN SMALL LETTER P
q                                                                       0071 	LATIN SMALL LETTER Q
r                                                                       0072 	LATIN SMALL LETTER R
s                                                                       0073 	LATIN SMALL LETTER S
t                                                                       0074 	LATIN SMALL LETTER T
u                                                                       0075 	LATIN SMALL LETTER U
v                                                                       0076 	LATIN SMALL LETTER V
w                                                                       0077 	LATIN SMALL LETTER W
x                                                                       0078 	LATIN SMALL LETTER X
y                                                                       0079 	LATIN SMALL LETTER Y
z                                                                       007A 	LATIN SMALL LETTER Z
braceleft                                                               007B 	LEFT CURLY BRACKET
bar                                                                     007C 	VERTICAL LINE
braceright                                                              007D 	RIGHT CURLY BRACKET
tilde                                              asciitilde           007E 	TILDE
`

## Range Processors

Given the rather large task of handling thousands of exceptions and tweaks, the package has a modules that each take care of a single unicode range. This makes it easier to work in different places at once. Also testing is easier.

The `GlyphName` class is initialised with a single unicode number. It then finds the unicode name. Based on the range name it tries to find a module with a corresponding name in `rangeProcessors/`. If it finds such a module it will run the `process()` function and apply it. The `process()` function will try to transform the unicode name by editing or replacing parts of the name.

### On the internals

* `GlyphName.uniNumber` integer, the unicode number we're working on.
* `GlyphName.uniName` string, the original unicode character name
* `GlyphName.processedUniName` string, the edited name.
* `GlyphName.suffixParts` list of name parts that are added at the end. Please use:
* `GlyphName.suffix(namePart)` use this method to add name parts to the suffix list.
* `GlyphName.replace(oldPattern, [newPattern])` If no newPattern is given it will assume it is `""` and delete `oldPattern`
* `GlyphName.edit(oldPattern, [*suffixes])` This is more elaborate: it will remove `oldPattern` from the name, and then append any number of suffix strings to `GlyphName.suffixParts`. When the processing is done all strings in suffixParts are appended to the end of the glyph name.
