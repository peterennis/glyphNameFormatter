import os

path = os.path.dirname(__file__)

# =======
# = AGD =
# =======

unicode2name_AGD = {}
name2unicode_AGD = {}

f = open(os.path.join(path, "AGD_name_uni.txt"), "r")
lines = f.readlines()
f.close()

# format
# glyphName hexUnicode
for line in lines:
    if line:
        name, uni = line.split()
        uni = int(uni, 16)
        unicode2name_AGD[uni] = name
        name2unicode_AGD[name] = uni


# ==================
# = unicode blocks =
# ==================

unicodeRangeNames = {}

f = open(os.path.join(path, "unicodeBlocks.txt"))
lines = f.readlines()
f.close()

# format
# Start Code..End Code; Block Name
for line in lines:
    if line.startswith("#"):
        # a comment
        continue
    line = line.strip()
    if not line:
        # empty line
        continue
    rangeValues, rangeName = line.split(";")
    rangeName = rangeName.strip()
    start, end = rangeValues.split("..")
    start = int(start, 16)
    end = int(end, 16)

    unicodeRangeNames[(start, end)] = rangeName
