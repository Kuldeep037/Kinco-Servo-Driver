# generated from rosidl_generator_py/resource/_idl.py.em
# with input from arm_interfaces:msg/AppParams.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_AppParams(type):
    """Metaclass of message 'AppParams'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('arm_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'arm_interfaces.msg.AppParams')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__app_params
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__app_params
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__app_params
            cls._TYPE_SUPPORT = module.type_support_msg__msg__app_params
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__app_params

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AppParams(metaclass=Metaclass_AppParams):
    """Message class 'AppParams'."""

    __slots__ = [
        '_repeat',
        '_start',
        '_end',
        '_speed',
        '_torque',
        '_threshold',
        '_delay',
    ]

    _fields_and_field_types = {
        'repeat': 'int32',
        'start': 'double',
        'end': 'double',
        'speed': 'int32',
        'torque': 'int32',
        'threshold': 'int32',
        'delay': 'int32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.repeat = kwargs.get('repeat', int())
        self.start = kwargs.get('start', float())
        self.end = kwargs.get('end', float())
        self.speed = kwargs.get('speed', int())
        self.torque = kwargs.get('torque', int())
        self.threshold = kwargs.get('threshold', int())
        self.delay = kwargs.get('delay', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.repeat != other.repeat:
            return False
        if self.start != other.start:
            return False
        if self.end != other.end:
            return False
        if self.speed != other.speed:
            return False
        if self.torque != other.torque:
            return False
        if self.threshold != other.threshold:
            return False
        if self.delay != other.delay:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def repeat(self):
        """Message field 'repeat'."""
        return self._repeat

    @repeat.setter
    def repeat(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'repeat' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'repeat' field must be an integer in [-2147483648, 2147483647]"
        self._repeat = value

    @builtins.property
    def start(self):
        """Message field 'start'."""
        return self._start

    @start.setter
    def start(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'start' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'start' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._start = value

    @builtins.property
    def end(self):
        """Message field 'end'."""
        return self._end

    @end.setter
    def end(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'end' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'end' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._end = value

    @builtins.property
    def speed(self):
        """Message field 'speed'."""
        return self._speed

    @speed.setter
    def speed(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'speed' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'speed' field must be an integer in [-2147483648, 2147483647]"
        self._speed = value

    @builtins.property
    def torque(self):
        """Message field 'torque'."""
        return self._torque

    @torque.setter
    def torque(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'torque' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'torque' field must be an integer in [-2147483648, 2147483647]"
        self._torque = value

    @builtins.property
    def threshold(self):
        """Message field 'threshold'."""
        return self._threshold

    @threshold.setter
    def threshold(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'threshold' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'threshold' field must be an integer in [-2147483648, 2147483647]"
        self._threshold = value

    @builtins.property
    def delay(self):
        """Message field 'delay'."""
        return self._delay

    @delay.setter
    def delay(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'delay' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'delay' field must be an integer in [-2147483648, 2147483647]"
        self._delay = value
