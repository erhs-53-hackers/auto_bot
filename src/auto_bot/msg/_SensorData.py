"""autogenerated by genpy from auto_bot/SensorData.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import auto_bot.msg

class SensorData(genpy.Message):
  _md5sum = "3768a5727c61039a823fe378ddf355cb"
  _type = "auto_bot/SensorData"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """auto_bot/Xdata[480] sensorData

================================================================================
MSG: auto_bot/Xdata
float32[640] xdata 

"""
  __slots__ = ['sensorData']
  _slot_types = ['auto_bot/Xdata[480]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       sensorData

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SensorData, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.sensorData is None:
        self.sensorData = [auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata()]
    else:
      self.sensorData = [auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata(),auto_bot.msg.Xdata()]

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      for val1 in self.sensorData:
        buff.write(_struct_640f.pack(*val1.xdata))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.sensorData is None:
        self.sensorData = None
      end = 0
      self.sensorData = []
      for i in range(0, 480):
        val1 = auto_bot.msg.Xdata()
        start = end
        end += 2560
        val1.xdata = _struct_640f.unpack(str[start:end])
        self.sensorData.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      for val1 in self.sensorData:
        buff.write(val1.xdata.tostring())
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.sensorData is None:
        self.sensorData = None
      end = 0
      self.sensorData = []
      for i in range(0, 480):
        val1 = auto_bot.msg.Xdata()
        start = end
        end += 2560
        val1.xdata = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=640)
        self.sensorData.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_640f = struct.Struct("<640f")
