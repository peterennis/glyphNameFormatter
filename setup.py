#!/usr/bin/env python

from distutils.core import setup

setup(name = "Glyph Name Formatter",
      version = "0.1",
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