# glyphNameFormatter

Experimental. 

* Unicode has long and descriptive names for each character.
* Unicode is not always right.
* Font editors need glyph names to easily identify the glyphs, short, unique, can't use space
* Raw Unicode names are unsuitable for this purpose in font editors
* Font editors then use their own lists that map names to unicode values.
* These lists only cover the glyphs that were needed in production, so there are often holes in the coverage.
* These lists should not dictate what is useful or not in a font but offer reliable unicode to name mapping.
* Adobe standardized some lists years ago, standard, but incomplete and immutable

## Rules

* Glyph names should, as much as possible, only have script prefixes to disambiguate. Otherwise all names are equal. So `gaf` rather than `arGaf` for `ARABIC LETTER GAF`, or `Uk` rather than `Ukcyrillic` for `CYRILLIC CAPITAL LETTER UK`.
* Script prefixes rather than suffixes to prevent interference with extensions as `.init`.
* Short script prefixes. `cy-Psi` rather than `Psicyrillic`.
* Disambiguation prefixes can be added after clash detection.
* If a name needs to include a language, this is added to the end: `yehfarsi.isol` for	`ARABIC LETTER FARSI YEH ISOLATED FORM`
* If an AGD name has a language but it is not needed for disambiguation and Unicode does not mention it, it can be ignored. For instance `kgreenlandic` can just be	`kra`.

## Goals
*  Reduce the number of glyph specific rules.
*  Casing in the name should reflect the case of the letter, if it has one.
*  Average name length should not exceed that of the AGD. Statistics are calculated in the test.
