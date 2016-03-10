
def process(self):
    self.replace("HEBREW LIGATURE YIDDISH DOUBLE VAV", "vav_vav")   # yiddish ?
    self.replace("HEBREW LIGATURE YIDDISH VAV YOD", "vav_yod")  # yiddish ?
    self.replace("HEBREW LIGATURE YIDDISH DOUBLE YOD", "yod_yod")
    self.replace("HEBREW MARK UPPER DOT", "dotupper")
    self.replace("HEBREW MARK LOWER DOT", "dotlower")
    self.replace("HEBREW PUNCTUATION GERESH", "gereshpunctuation")
    self.replace("HEBREW PUNCTUATION GERSHAYIM", "gershayimpunctuation")
    self.replace("HEBREW ACCENT SEGOL", "segolta")

    # used in alphabetic presentation forms
    self.edit("WIDE", "wide")
    self.edit("JUDEO-SPANISH", 'judeospanish')
    self.edit("HEBREW LIGATURE YIDDISH YOD YOD PATAH", "yod_yod_patah")
    self.edit("ALTERNATIVE", "alt")

    self.edit("ACCENT", "")
    self.edit("FINAL", "final")    # .fina
    self.edit("POINT", "")   # point? or nikud?
    if self.has("YIDDISH"):
        if self.replace("YIDDISH"):
            self.suffix("yiddish")
    if self.has("PUNCTUATION"):
        self.replace("PUNCTUATION")

    self.edit("HEBREW LETTER")
    self.edit('HEBREW')
    self.edit("LETTER")

    self.lower()
    self.compress()


if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Hebrew")
