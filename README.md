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

### Goals
*  Reduce the number of glyph specific rules.
*  Casing in the name should reflect the case of the letter, if it has one.
*  Average name length should not exceed that of the AGD. Statistics are calculated in the test.

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
