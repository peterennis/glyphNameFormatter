# -*- coding: UTF-8 -*-
# default, final, catchall handler

from _processDiacritics import processDiacritics
from _processShape import processShape


def process(self):
    self.condense(self.uniName)
    return False


class GlyphNameProcessor(object):

    processDiacritics = processDiacritics
    processShape = processShape
