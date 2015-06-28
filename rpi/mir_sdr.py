# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_mir_sdr', [dirname(__file__)])
        except ImportError:
            import _mir_sdr
            return _mir_sdr
        if fp is not None:
            try:
                _mod = imp.load_module('_mir_sdr', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _mir_sdr = swig_import_helper()
    del swig_import_helper
else:
    import _mir_sdr
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


mir_sdr_Success = _mir_sdr.mir_sdr_Success
mir_sdr_Fail = _mir_sdr.mir_sdr_Fail
mir_sdr_InvalidParam = _mir_sdr.mir_sdr_InvalidParam
mir_sdr_OutOfRange = _mir_sdr.mir_sdr_OutOfRange
mir_sdr_GainUpdateError = _mir_sdr.mir_sdr_GainUpdateError
mir_sdr_RfUpdateError = _mir_sdr.mir_sdr_RfUpdateError
mir_sdr_FsUpdateError = _mir_sdr.mir_sdr_FsUpdateError
mir_sdr_HwError = _mir_sdr.mir_sdr_HwError
mir_sdr_AliasingError = _mir_sdr.mir_sdr_AliasingError
mir_sdr_AlreadyInitialised = _mir_sdr.mir_sdr_AlreadyInitialised
mir_sdr_NotInitialised = _mir_sdr.mir_sdr_NotInitialised
mir_sdr_BW_0_200 = _mir_sdr.mir_sdr_BW_0_200
mir_sdr_BW_0_300 = _mir_sdr.mir_sdr_BW_0_300
mir_sdr_BW_0_600 = _mir_sdr.mir_sdr_BW_0_600
mir_sdr_BW_1_536 = _mir_sdr.mir_sdr_BW_1_536
mir_sdr_BW_5_000 = _mir_sdr.mir_sdr_BW_5_000
mir_sdr_BW_6_000 = _mir_sdr.mir_sdr_BW_6_000
mir_sdr_BW_7_000 = _mir_sdr.mir_sdr_BW_7_000
mir_sdr_BW_8_000 = _mir_sdr.mir_sdr_BW_8_000
mir_sdr_IF_Zero = _mir_sdr.mir_sdr_IF_Zero
mir_sdr_IF_0_450 = _mir_sdr.mir_sdr_IF_0_450
mir_sdr_IF_1_620 = _mir_sdr.mir_sdr_IF_1_620
mir_sdr_IF_2_048 = _mir_sdr.mir_sdr_IF_2_048

def mir_sdr_Init(*args):
  return _mir_sdr.mir_sdr_Init(*args)
mir_sdr_Init = _mir_sdr.mir_sdr_Init

def mir_sdr_Uninit():
  return _mir_sdr.mir_sdr_Uninit()
mir_sdr_Uninit = _mir_sdr.mir_sdr_Uninit

def mir_sdr_ReadPacket(*args):
  return _mir_sdr.mir_sdr_ReadPacket(*args)
mir_sdr_ReadPacket = _mir_sdr.mir_sdr_ReadPacket

def mir_sdr_SetRf(*args):
  return _mir_sdr.mir_sdr_SetRf(*args)
mir_sdr_SetRf = _mir_sdr.mir_sdr_SetRf

def mir_sdr_SetFs(*args):
  return _mir_sdr.mir_sdr_SetFs(*args)
mir_sdr_SetFs = _mir_sdr.mir_sdr_SetFs

def mir_sdr_SetGr(*args):
  return _mir_sdr.mir_sdr_SetGr(*args)
mir_sdr_SetGr = _mir_sdr.mir_sdr_SetGr

def mir_sdr_SetGrParams(*args):
  return _mir_sdr.mir_sdr_SetGrParams(*args)
mir_sdr_SetGrParams = _mir_sdr.mir_sdr_SetGrParams

def mir_sdr_SetDcMode(*args):
  return _mir_sdr.mir_sdr_SetDcMode(*args)
mir_sdr_SetDcMode = _mir_sdr.mir_sdr_SetDcMode

def mir_sdr_SetDcTrackTime(*args):
  return _mir_sdr.mir_sdr_SetDcTrackTime(*args)
mir_sdr_SetDcTrackTime = _mir_sdr.mir_sdr_SetDcTrackTime

def mir_sdr_SetSyncUpdateSampleNum(*args):
  return _mir_sdr.mir_sdr_SetSyncUpdateSampleNum(*args)
mir_sdr_SetSyncUpdateSampleNum = _mir_sdr.mir_sdr_SetSyncUpdateSampleNum

def mir_sdr_SetSyncUpdatePeriod(*args):
  return _mir_sdr.mir_sdr_SetSyncUpdatePeriod(*args)
mir_sdr_SetSyncUpdatePeriod = _mir_sdr.mir_sdr_SetSyncUpdatePeriod

def mir_sdr_ApiVersion(*args):
  return _mir_sdr.mir_sdr_ApiVersion(*args)
mir_sdr_ApiVersion = _mir_sdr.mir_sdr_ApiVersion

def mir_sdr_ResetUpdateFlags(*args):
  return _mir_sdr.mir_sdr_ResetUpdateFlags(*args)
mir_sdr_ResetUpdateFlags = _mir_sdr.mir_sdr_ResetUpdateFlags
# This file is compatible with both classic and new-style classes.

