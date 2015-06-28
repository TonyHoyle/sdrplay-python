%module mir_sdr

%include "cmalloc.i"

%{
#include <stdlib.h>
#include "sdrplay/mir_sdr.h"
%}


%allocators(short);

mir_sdr_ErrT mir_sdr_Init(int, double, double, mir_sdr_Bw_MHzT, mir_sdr_If_kHzT , int *OUTPUT);
mir_sdr_ErrT mir_sdr_ReadPacket(short *xi, short *xq, unsigned int *OUTPUT, int *OUTPUT, int *OUTPUT, int *OUTPUT);
mir_sdr_ErrT mir_sdr_ApiVersion(float *OUTPUT);

#define STATIC_LIB
%include "sdrplay/mir_sdr.h"

