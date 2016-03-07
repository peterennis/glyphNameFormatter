# -*- coding: UTF-8 -*-
# default, final, catchall handler

def process(self):
    self.condense(self.uniName)
    self.uniNameProcessed = "needsfix_" + self.uniNameProcessed
    return False