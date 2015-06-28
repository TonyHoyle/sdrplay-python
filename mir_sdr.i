%module mir_sdr

%{
#include <stdlib.h>
#include "sdrplay/mir_sdr.h"
%}

#define STATIC_LIB
%include "sdrplay/mir_sdr.h"
