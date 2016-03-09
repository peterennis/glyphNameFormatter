from glyphNameFormatter.data.scriptPrefixes import scriptPrefixes

def process(self):
    self.replace("GREEK")


    self.edit("COPTIC", "coptic")

    self.edit("ARCHAIC", "archaic")
    self.edit("PAMPHYLIAN", "pamphylian")
    self.edit("YPOGEGRAMMENI", "iotalenis")

    self.replace("LETTER DIGAMMA", "Digamma")
    self.replace("LETTER KOPPA", "Koppa")
    self.replace("LETTER STIGMA", "Stigma")
    self.replace("LETTER SAMPI", "Sampi")
    self.replace("LETTER YOT", "yot")

    self.edit("LOWER NUMERAL SIGN", "lownumeralsign")
    self.edit("NUMERAL SIGN", "numeralsign")
    self.edit("QUESTION MARK", "question")

    self.edit("ANO TELEIA", "anoteleia")
    self.edit("SMALL REVERSED LUNATE SIGMA SYMBOL", "sigmalunatereversedsymbol")
    self.edit("SMALL DOTTED LUNATE SIGMA SYMBOL", "sigmalunatedottedsymbol")
    self.edit("SMALL REVERSED DOTTED LUNATE SIGMA SYMBOL", "sigmalunatedottedreversedsymbol")
    self.edit("CAPITAL REVERSED LUNATE SIGMA SYMBOL", "Sigmareversedlunatesymbol")
    self.edit("CAPITAL DOTTED LUNATE SIGMA SYMBOL", "Sigmalunatesymboldotted")
    self.edit("CAPITAL LUNATE SIGMA SYMBOL", "Sigmalunatesymbol")
    self.edit("LUNATE SIGMA SYMBOL", "sigmalunatesymbol")
    self.edit("REVERSED LUNATE EPSILON SYMBOL", "epsilonreversedlunatesymbol")
    self.edit("LUNATE EPSILON SYMBOL", "epsilonlunatesymbol")

    self.edit("RHO WITH STROKE SYMBOL", "rhostrokesymbol")
    self.edit("UPSILON SYMBOL", "upsilonsymbol")
    self.edit("PHI SYMBOL", "phi.math")
    self.edit("CAPITAL KAI SYMBOL", "Kaisymbol")
    self.edit("KAI SYMBOL", "kaisymbol")
    self.edit("PI SYMBOL", "pi.math")
    self.edit("CAPITAL THETA SYMBOL", "Thetasymbol")
    self.edit("THETA SYMBOL", "theta.math")
    self.edit("BETA SYMBOL", "betasymbol")
    self.edit("UPSILON SYMBOL", "upsilonsymbol")
    self.edit("KAPPA SYMBOL", "kappa.math")
    self.edit("RHO SYMBOL", "rhosymbol")
    if self.has("SIGMA SYMBOL"):
        if self.replace("SYMBOL"):
            self.suffix("symbol")
    # with
    self.edit("UPSILON WITH HOOK SYMBOL", "Upsilonhooksymbol")
    self.edit("UPSILON WITH ACUTE AND HOOK SYMBOL", "Upsilonacutehooksymbol")
    self.edit("UPSILON WITH DIAERESIS AND HOOK SYMBOL", "Upsilona%shooksymbol"%self.prefSpelling_dieresis)
    self.edit("TONOS", "tonos")

    self.processAs("Helper Greek Diacritics")

    self.handleCase()
    self.compress()


if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Greek and Coptic")
