# -*- coding: UTF-8 -*-
# default, final, catchall handler

def process(self):
    print "default processor"
    self.condense(self.uniName)
    return False