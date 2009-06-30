from distutils.core import setup, Extension

setup(name        = "parsedates",
      version     = "1.0",
      ext_modules = [Extension("parsedates",  ["c_parse.c"]),
			         ])
