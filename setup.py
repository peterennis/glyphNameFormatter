#!/usr/bin/env python

from setuptools import setup
import re


version = ''
with open('Lib/glyphNameFormatter/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)


setup(name = "Glyph Name Formatter",
      version = version,
      description = "Generate list of glyphnames from unicode names.",
      author = "Erik van Blokland, Frederik Berlaen",
      author_email = "erik@letterror.com, frederik@typemytype.com",
      url = "https://github.com/LettError/glyphNameFormatter",
      license = "BSD 3 Clause",
      packages = [
              "glyphNameFormatter",
              "glyphNameFormatter.data",
              "glyphNameFormatter.rangeProcessors",
              "glyphNameFormatter.test",
      ],
      package_dir = {"":"Lib"},
)
