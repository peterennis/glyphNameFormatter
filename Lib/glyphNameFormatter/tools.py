import struct

def camelCase(pattern):
    if len(pattern)==0:
        return ""
    if "-" in pattern:
        t = ""
        for p in pattern.split("-"):
            t += camelCase(p)
        return t
    return pattern[0].upper()+pattern[1:].lower()


def unicodeToChar(uni):
    if uni < 0xFFFF:
        return unichr(uni)
    else:
        return struct.pack('i', uni).decode('utf-32')


def charToUnicode(char):
    if len(char) != 2:
        return ord(char)
    return 0x10000 + (ord(char[0]) - 0xD800) * 0x400 + (ord(char[1]) - 0xDC00)

if __name__ == "__main__":
    assert camelCase("aaaa") == "Aaaa"
    assert camelCase("aaaA") == "Aaaa"
    assert camelCase("aaaa-aaaa") == "AaaaAaaa"
    assert camelCase("aaaa-") == "Aaaa"
    assert camelCase("-") == ""
    assert camelCase("") == ""
