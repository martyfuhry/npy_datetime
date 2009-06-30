from distutils.core import setup, Extension

setup(name        = "npy_datetime",
      version     = "1.0",
      ext_modules = [Extension("npy_datetime",  ["c_datetime.c"]),
			         ])
