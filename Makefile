all: mir_sdr.so

mir_sdr_module.cc: mir_sdr.i
	swig -python -c++ -o mir_sdr_module.cc mir_sdr.i

mir_sdr.so: mir_sdr_module.cc
	python setup.py build_ext --inplace

install: mir_sdr.so
	python setup.py install
	
clean:
	rm *.cc *.so *.pyd
