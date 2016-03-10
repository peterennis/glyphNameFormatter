
def process(self):


    self.replace("SQUARED", "2")
    self.replace("CUBED", "3")
    self.replace("C OVER KG", "coverkg")
    self.replace("M OVER S", "movers")
    self.replace("RAD OVER S", "radovers")
    self.replace("DAY", "day")
    self.replace("V OVER M", "voverm")
    self.replace("A OVER M", "aoverm")

    if 0x33E0 <= self.uniNumber <= 0x33FE:
        self.edit("IDEOGRAPHIC TELEGRAPH SYMBOL FOR", "telegraph")


    fullWidthSections = [
        (0x3371, 0x337A),
        (0x3380, 0x33DF)
    ]
    changed = False
    for start, end in fullWidthSections:
        if start <= self.uniNumber <= end:
            self.edit("SQUARE", "fullwidth")
            changed = True
    if not changed:
        self.edit("SQUARE", "square")

    mixedCases = {
        # longer
        'PA AMPS':  'pAamps',
        'HPA':      "hPa",
        'MU A':     'muA',
        "MU F":     "muF",
        "MU G":     "muG",
        "K OHM":    "kOhm",
        "M OHM":    "MOhm",
        "MW MEGA":  "MWmega",
        "KPA":       "kPa",
        "PPM":      "PPM",

        "KHZ":      "kHz",
        "MHZ":      "MHz",
        "GHZ":      "GHz",
        "THZ":      "THz",

        # shorter
        "HZ":       "Hz",
        "PA":       "Pa",
        'OV':       "oV",
        'NA':       "nA",
        "MA":       "mA",
        "KA":       "kA",
        "PF":       "pF",
        "NF":       "nF",
        "BQ":       "bQ",
        "SV":       "sV",
        "PH":       "pH",
        "GY":       "gY",
        "HP":       "HP",
        "PV":       "pV",
        "MW":       "MW",
        "KB":       "KB",
    }
    allowMixedCase = False
    for k, v in mixedCases.items():
        if self.has(k):
            self.replace(k, v)
            allowMixedCase = True
            break
    # but then do these anyway
    if 0x3300 <= self.uniNumber <= 0x3357:
        self.lower()

    self.processAs("Helper Digit Names")

    self.edit("-")
    if not allowMixedCase:
        self.lower()
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("CJK Compatibility")
