from __future__ import print_function
import os
import sys
import tempfile
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

JOININGTYPES_FILE = "joiningTypes.txt"
ASURL = "http://www.unicode.org/Public/{version}/ucd/ArabicShaping.txt"

print(ASURL.format(version=version))

tempdir = tempfile.mkdtemp()
filename = os.path.join(tempdir, JOININGTYPES_FILE)
print(">> Downloading {} to {}".format(os.path.basename(ASURL), filename))
if options.unicode_version:
    version = options.unicode_version
else:
    version = UNICODE_VERSION
url = urlopen(ASURL.format(version=version))
with open(filename, "wb") as fp:
    blocksize = 8192
    while True:
        buffer = url.read(blocksize)
        if not buffer:
            break
        fp.write(buffer)
# fp.rewind()
# print(len(fp))
