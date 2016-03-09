from glyphNameFormatter.data.scriptPrefixes import scriptPrefixes


def process(self):
    # self.scriptTag = scriptPrefixes['armenian']
    self.edit("ARMENIAN")

    self.edit("APOSTROPHE", "apostrophe")
    self.edit("EMPHASIS MARK", "emphasismark")
    self.edit("QUESTION MARK", "question")
    self.edit("EXCLAMATION MARK", "exclam")
    self.edit("ABBREVIATION MARK", 'abbreviationmark')
    self.edit("MODIFIER LETTER LEFT HALF RING", "ringhalfleft")
    self.edit("SMALL LIGATURE ECH YIWN", "ech_yiwn")

    # used in alphabetic presentation forms
    self.edit("SMALL LIGATURE MEN NOW", "men_now")
    self.edit("SMALL LIGATURE MEN ECH", "men_ech")
    self.edit("SMALL LIGATURE MEN INI", "men_ini")
    self.edit("SMALL LIGATURE VEW NOW", "vew_now")
    self.edit("SMALL LIGATURE MEN XEH", "men_xeh")

    self.edit("COMMA", "comma")
    self.edit("FULL STOP", "period")
    self.edit("HYPHEN", "hyphen")
    self.handleCase()
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Armenian")
