from setuptools import setup, Extension

# the c++ extension module
extension_mod = Extension("_mir_sdr", ["mir_sdr_module.cc"], library_dirs=['sdrplay'], libraries=['mir_sdr'])

setup(name = "mir_sdr", 
      version='1.0.0',
      description='SDRPlay python wrappers',
      author='Tony Hoyle',
      author_email='tony@hoyle.me.uk',
      py_modules=['mir_sdr'],
      ext_modules=[extension_mod], 
      include_dirs=['sdrplay'])
