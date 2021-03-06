# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from inertial_sense/RTKInfo.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class RTKInfo(genpy.Message):
  _md5sum = "0f06cd1205181677917f42a40817ccb4"
  _type = "inertial_sense/RTKInfo"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """Header header

float32[3] BaseLLA 			# base position in lat-lon-altitude (deg, deg, m)
uint32 cycle_slip_count 	# number of cycle slips detected
uint32 roverObs				# number of observations from rover (GPS, Glonass, Gallileo, Beidou, Qzs)
uint32 baseObs				# number of observations from base (GPS, Glonass, Gallileo, Beidou, Qzs)
uint32 roverEph				# number of ephemeris messages from rover (GPS, Glonass, Gallileo, Beidou, Qzs)
uint32 baseEph				# number of ephemeris messages from rover (GPS, Glonass, Gallileo, Beidou, Qzs)
uint32 baseAntcount			# number of base station antenna position measurements


================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id
"""
  __slots__ = ['header','BaseLLA','cycle_slip_count','roverObs','baseObs','roverEph','baseEph','baseAntcount']
  _slot_types = ['std_msgs/Header','float32[3]','uint32','uint32','uint32','uint32','uint32','uint32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,BaseLLA,cycle_slip_count,roverObs,baseObs,roverEph,baseEph,baseAntcount

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RTKInfo, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.BaseLLA is None:
        self.BaseLLA = [0.] * 3
      if self.cycle_slip_count is None:
        self.cycle_slip_count = 0
      if self.roverObs is None:
        self.roverObs = 0
      if self.baseObs is None:
        self.baseObs = 0
      if self.roverEph is None:
        self.roverEph = 0
      if self.baseEph is None:
        self.baseEph = 0
      if self.baseAntcount is None:
        self.baseAntcount = 0
    else:
      self.header = std_msgs.msg.Header()
      self.BaseLLA = [0.] * 3
      self.cycle_slip_count = 0
      self.roverObs = 0
      self.baseObs = 0
      self.roverEph = 0
      self.baseEph = 0
      self.baseAntcount = 0

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
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      buff.write(_get_struct_3f().pack(*self.BaseLLA))
      _x = self
      buff.write(_get_struct_6I().pack(_x.cycle_slip_count, _x.roverObs, _x.baseObs, _x.roverEph, _x.baseEph, _x.baseAntcount))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 12
      self.BaseLLA = _get_struct_3f().unpack(str[start:end])
      _x = self
      start = end
      end += 24
      (_x.cycle_slip_count, _x.roverObs, _x.baseObs, _x.roverEph, _x.baseEph, _x.baseAntcount,) = _get_struct_6I().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      buff.write(self.BaseLLA.tostring())
      _x = self
      buff.write(_get_struct_6I().pack(_x.cycle_slip_count, _x.roverObs, _x.baseObs, _x.roverEph, _x.baseEph, _x.baseAntcount))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 12
      self.BaseLLA = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      _x = self
      start = end
      end += 24
      (_x.cycle_slip_count, _x.roverObs, _x.baseObs, _x.roverEph, _x.baseEph, _x.baseAntcount,) = _get_struct_6I().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_3f = None
def _get_struct_3f():
    global _struct_3f
    if _struct_3f is None:
        _struct_3f = struct.Struct("<3f")
    return _struct_3f
_struct_6I = None
def _get_struct_6I():
    global _struct_6I
    if _struct_6I is None:
        _struct_6I = struct.Struct("<6I")
    return _struct_6I
