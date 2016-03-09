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

* Glyph names should, as much as possible, only have script tags to disambiguate. Otherwise all names are equal. So `gaf` rather than `arGaf` for `ARABIC LETTER GAF`, or `Uk` rather than `Ukcyrillic` for `CYRILLIC CAPITAL LETTER UK`.
* Script specific prefix or suffix.
* Short script prefix or suffix.
* Disambiguation prefix or suffix can be added after clash detection with all names.
* If a name needs to include a language, this is added to the end: `yehfarsi.isol` for	`ARABIC LETTER FARSI YEH ISOLATED FORM`
* If an AGD name has a language but it is not needed for disambiguation and Unicode does not mention it, it can be ignored. For instance `kgreenlandic` can just be	`kra`.

## Making lists

Run `test/buildRanges.py` to make all the name lists. They will be deposited in `names/ranges`. There will be other methods and other lists, but for now this is the place to make things.
You can also run each of the range scripts in `rangeProcessors/` and they will print a nice readable table with the processed name, unicode value, original name. There is also a column for names from the Adobe AGL if it has a different name for that entry. 

Run `test/analyseConflicts.py` to get an overview of all name clashes and how they are addressed. The results are in a text file in [names/conflict.txt](https://github.com/LettError/glyphNameFormatter/blob/master/Lib/glyphNameFormatter/names/conflict.txt)

Run `test/export.py` to generate a text file with <name> <unicode> pairs, exclusively with the available range processors. The results are in [names/glyphNamesToUnicode.txt](https://github.com/LettError/glyphNameFormatter/blob/master/Lib/glyphNameFormatter/names/glyphNamesToUnicode.txt)

Run `testAGDcoverage.py` to generate an overview of all glyphranges that are needed to match the Adobe Glyph Dictionary. It also calculates how far we are along.

## Range Processors

Given the rather large task of handling thousands of exceptions and tweaks, the package has a modules that each take care of a single unicode range. This makes it easier to work in different places at once. Also testing is easier.

The `GlyphName` class is initialised with a single unicode number. It then finds the unicode name. Based on the range name it tries to find a module with a corresponding name in `rangeProcessors/`. If it finds such a module it will run the `process()` function and apply it. The `process()` function will try to transform the unicode name by editing or replacing parts of the name.

Each range processor has a handy debugginh print function that will show an overview of the unicode value, the generated name, a comparison with the AGD name and the unicode names.

### On the internals

* `GlyphName.uniNumber` integer, the unicode number we're working on.
* `GlyphName.uniName` string, the original unicode character name
* `GlyphName.processedUniName` string, the edited name.
* `GlyphName.suffixParts` list of name parts that are added at the end. Please use:
* `GlyphName.suffix(namePart)` use this method to add name parts to the suffix list.
* `GlyphName.replace(oldPattern, [newPattern])` If no newPattern is given it will assume it is `""` and delete `oldPattern`
* `GlyphName.edit(oldPattern, [*suffixes])` This is more elaborate: it will remove `oldPattern` from the name, and then append any number of suffix strings to `GlyphName.suffixParts`. When the processing is done all strings in suffixParts are appended to the end of the glyph name.
