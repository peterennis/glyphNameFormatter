# -*- coding: UTF-8 -*-

def process(self):
    self.edit("LATIN")
    self.handleCase()
    self.compress()
    return True