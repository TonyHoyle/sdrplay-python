#from distutils.core import Extension
from setuptools import setup, Extension

# the c++ extension module
extension_mod = Extension("_mir_sdr", ["mir_sdr_module.cc"], library_dirs=['SDRPlay'], libraries=['mir_sdr_api'])

setup(name = "_mir_sdr", ext_modules=[extension_mod], include_dirs=['SDRPlay'])
