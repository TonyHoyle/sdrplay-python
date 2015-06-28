%module mir_sdr

%{
#include <stdlib.h>
#include "SDRPlay/mir_sdr.h"
%}

#define STATIC_LIB
%include "SDRPlay/mir_sdr.h"
