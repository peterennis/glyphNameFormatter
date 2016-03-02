# glyphNameFormatter

Experimental. Oh maybe that needs a bigger font.

# EXPERIMENTAL

Beware. This is a wild goose / red herring.

## HOWEVER

* Unicode has long and descriptive names for each character.
* Font editors need glyph names to easily identify the glyphs, short, unique, can't use space
* Raw Unicode names are unsuitable for this purpose in font editors
* Font editors then use their own lists that map names to unicode values.
* These lists only cover the glyphs that were needed in production, so there are often holes in the coverage.
* These lists should not dictate what is useful or not in a font but offer reliable unicode to name mapping.
* Adobe standardized some lists years ago, standard, but incomplete and immutable


## SO..

What if we could /generate/ useful names using the Unicode database, more or less following the conventions?

The code is not going to be verypretty, basically a long list of rules, tests and exceptions.
Some rules would be very specific, but many would work on many names, so there will be an economy of scale. As we can do more with python than with regular expressions we can add rules until it looks good. But in the end it will generate a reliable, testable list of names.
Speed is not an issue, as long as it can generate final lists of names.

This initial version only generates the Latin, Arabic and Cyrillic ranges. Have a look at generatedGlyphNames.txt for output. Or just run the formatter and make a new one.

## Tests

* Tests need to be written to make sure it all behaves. 
* Names need to be unique
* Compare names to available and public name lists from existing font editors
* Fix rules to match those lists, or use this opportunity to fix bugs?
