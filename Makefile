all: mir_sdr.so

mir_sdr_module.cc: mir_sdr.i
	swig -python -c++ -o mir_sdr_module.cc mir_sdr.i

mir_sdr.so: mir_sdr_module.cc
	python setup.py build_ext --inplace
	
clean:
	rm *.cc *.so
