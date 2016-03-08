from glyphNameFormatter.data.scriptPrefixes import scriptPrefixes

def process(self):
    self.scriptTag = scriptPrefixes['arabic']

    # If the Arabic ligature names comes with any of these terms then these rules apply on components:

    # Initial ligature: FIRST component is INIT and the REST are MEDI
    # Medial ligature: ALL the components are MEDI
    # Final ligature: the LAST component is FINA and the rest are MEDI
    # Isolate ligature: The LAST components is FINA, the fist components is INIT and the rest are MEDI


    if self.has("LIGATURE"):
        parts = self.uniName.split(" ")

        # get the type
        ligatureType = 'other'
        lastNameIndex=len(parts)
        if parts[-2] == "INITIAL" and parts[-1] == "FORM":
            ligatureType = "initial"
            lastNameIndex=-2
        elif parts[-2] == "MEDIAL" and parts[-1] == "FORM":
            ligatureType = "medial"
            lastNameIndex=-2
        elif parts[-2] == "FINAL" and parts[-1] == "FORM":
            ligatureType = "final"
            lastNameIndex=-2
        elif parts[-2] == "ISOLATED" and parts[-1] == "FORM":
            ligatureType = "isolated"
            lastNameIndex=-2
        ligatureMarkIndex = parts.index("LIGATURE")
        #print ligatureMarkIndex
        withCount = parts.count("WITH")
        ligatureParts = []
        if withCount == 0:
            # ligatures without named parts
            # print "0 parts", parts[ligatureMarkIndex:]
            nameParts = parts[ligatureMarkIndex+1:lastNameIndex]
            ligatureParts = [nameParts]
        elif withCount == 1:
            # ligatures with 1 named part
            withIndex1 = parts.index("WITH")
            nameParts1 = parts[ligatureMarkIndex+1:withIndex1]
            nameParts2 = parts[withIndex1+1:lastNameIndex]
            ligatureParts = [nameParts1, nameParts2]
        elif withCount == 2:
            # ligatures with 2 named part
            # pass
            withIndex1 = parts.index("WITH")
            withIndex2 = parts.index("WITH", withIndex1+1)
            nameParts1 = parts[ligatureMarkIndex+1:withIndex1]
            nameParts2 = parts[withIndex1+1:withIndex2]
            nameParts3 = parts[withIndex2+1:lastNameIndex]
            ligatureParts = [nameParts1, nameParts2, nameParts3]

        if len(ligatureParts)==1:
            # logotypes and so on
            # handle later
            print "\n", self.uniName
            print "\t", len(ligatureParts), ligatureParts[0]
            print "\t", ligatureType
            # camel case
            
        elif len(ligatureParts)>=2:
            if ligatureType == "initial":
                # Initial ligature: FIRST component is INIT and the REST are MEDI
                ligatureParts[0].append(".init")
                for part in ligatureParts[1:]:
                    part.append(".medi")
            elif ligatureType == "medial":
                # Medial ligature: ALL the components are MEDI
                for part in ligatureParts:
                    part.append(".medi")
            elif ligatureType == "final":
                # Final ligature: the LAST component is FINA and the rest are MEDI
                for part in ligatureParts[:-1]:
                    part.append(".medi")
                ligatureParts[-1].append(".fina")
            elif ligatureType == "isolated":
                # Isolate ligature: The LAST components is FINA, the fist components is INIT and the rest are MEDI
                for part in ligatureParts[1:-1]:
                    part.append(".medi")
                ligatureParts[-1].append(".fina")
                ligatureParts[0].append(".init")
            else:
                xx


    self.processAs("Arabic")
    # more specific edits needed


if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Arabic Presentation Forms-A")
