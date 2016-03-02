# glyphNameFormatter

Experimental.

* Unicode has long and descriptive names for each character.
* Font editors need glyph names to easily identify the glyphs, short, unique, can't use space
* Raw Unicode names are unsuitable for this purpose in font editors
* Font editors then use their own lists that map names to unicode values.
* Adobe standardized some lists years ago, standard, but incomplete and immutable
* What if we could generate useful names using the Unicode database, more or less following the conventions?

The code is not going to be verypretty, basically a long list of rules and tests.
Some very specific, some very broad. As we can do more with python than with regular expressions we can add rules until it looks good. But in the end it will generate a reliable, testable list of names.
Speed is not an issue, as long as it can generate final lists of names.

In the initial version only the Latin ranges, Arabic and Cyrillic have been provisionally added.

## Tests

* Tests need to be written to make sure it all behaves. 
* Names need to be unique
* Compare names to available and public name lists from existing font editors
* Fix rules to match the list, or use this opportunity to fix bugs
