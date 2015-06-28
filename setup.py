from distutils.core import setup, Extension

# the c++ extension module
extension_mod = Extension("mir_sdr", ["mir_sdr_module.cc"])

setup(name = "mir_sdr", ext_modules=[extension_mod])
