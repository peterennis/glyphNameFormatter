from __future__ import print_function
import os
import time
import sys
import tempfile
from glyphNameFormatter.reader import u2c, u2n
from argparse import ArgumentParser, RawDescriptionHelpFormatter

try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

UNICODE_VERSION = "11.0.0"

parser = ArgumentParser(description=__doc__,
                        formatter_class=RawDescriptionHelpFormatter)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-u", "--unicode-version",
                   help="Unicode version to use for download and processing")
options = parser.parse_args()

if options.unicode_version:
    version = options.unicode_version
else:
    version = UNICODE_VERSION


CASEFOLDING_FILE = "CaseFolding.txt"
ASURL = "http://www.unicode.org/Public/{version}/ucd/CaseFolding.txt"

print(ASURL.format(version=version))

print(">> Downloading {} to {}".format(os.path.basename(ASURL), CASEFOLDING_FILE))
if options.unicode_version:
    version = options.unicode_version
else:
    version = UNICODE_VERSION
url = urlopen(ASURL.format(version=version))
with open(CASEFOLDING_FILE, "wb") as fp:
    blocksize = 8192
    while True:
        buffer = url.read(blocksize)
        if not buffer:
            break
        fp.write(buffer)
# fp.rewind()
# print(len(fp))


# coding: utf-8


def readCaseFolding(path):
    # makes caseTable.txt
    names = {}
    explanation = """Case Folding Table"""

    f = open(path, 'r')
    d = f.read()
    f.close()
    source = None
    table = []
    for l in d.split("\n"):
        if not l: continue
        if l.find("CaseFolding-")!=-1:
            source = l
            continue
        if l[0] == "#": continue
        parts = l.split(";")
        parts = [p.strip() for p in parts]
        if parts[1] not in ["C", 'T']:
            print("skipping", parts)
            continue
        parts[0] = u"0x"+parts[0]
        parts[2] = u"0x"+parts[2]
        #print(parts)
        try:
            uniFirst = parts[0] = int(parts[0],0)
            uniSecond = parts[2] = int(parts[2],0)
            catFirst = u2c(uniFirst)
            catSecond = u2c(uniSecond)
            table.append((uniFirst, uniSecond, catFirst, catSecond))
        except ValueError:
            print(parts)
    #     categories[uni] = parts[2]
    txt = []
    txt.append(explanation)
    txt.append("# Generated on %s" % time.strftime("%Y %m %d %H:%M:%S"))
    txt.append("# Source: %s"%source)
    txt.append("# <unicode uppercase> <unicode lowercase>")
    for uniFirst, uniSecond, catFirst, catSecond in table:
        if catFirst != None and catSecond != None:
            note = "\t#%s -> %s, %s -> %s" % (catFirst, catSecond, u2n(uniFirst), u2n(uniSecond))
        else:
            note = ""
        txt.append("%05X\t%05X%s"% (uniFirst, uniSecond, note))
    path = "caseTable.txt"
    f = open(path, 'w')
    f.write('\n'.join(txt))
    f.close()




if __name__ == "__main__":
    from pprint import pprint
    arabicRange = 1536, 125251
    path = "CaseFolding.txt"
    readCaseFolding(path)

    path = "caseTable.txt"

