%module mir_sdr

%{
#include <stdlib.h>
#include <mirsdrapi-rsp.h>
%}

#define STATIC_LIB
%include "/usr/local/include/mirsdrapi-rsp.h"
