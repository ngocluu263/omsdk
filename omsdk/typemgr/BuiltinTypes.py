import re
from omsdk.typemgr.FieldType import FieldType
from omsdk.typemgr.ClassType import ClassType


class CompositeFieldType(FieldType):
    def __init__(self, *parts):
        super().__init__(None, tuple, 'Attribute', None, None, True)
        self.__dict__['_value'] = parts
        self._composite = True

    def clone(self, parent=None):
        return type(self)(*self.__dict__['_value'])

class RootClassType(ClassType):
    def __init__(self, fname, alias, parent = None):
        super().__init__(fname, alias, parent)

class CloneableFieldType(FieldType):
    def clone(self, parent=None):
        if isinstance(self, EnumTypeField):
            return type(self)(self._value, entype=self._type, alias=self._alias,
                  parent=parent, volatile=self._volatile,
                  modifyAllowed = self._modifyAllowed,
                  deleteAllowed = self._deleteAllowed,
                  rebootRequired = self._rebootRequired)
        else:
            return type(self)(self._value, alias=self._alias,
                  parent=parent, volatile=self._volatile,
                  modifyAllowed = self._modifyAllowed,
                  deleteAllowed = self._deleteAllowed,
                  rebootRequired = self._rebootRequired)

class PortField(CloneableFieldType):
    def __init__(self, init_value, alias =None, parent=None, volatile=False,
                 modifyAllowed=True, deleteAllowed=True, rebootRequired=False):
        super().__init__(init_value, int, 'Attribute', alias, parent,
                         volatile, modifyAllowed, deleteAllowed, rebootRequired)

    def my_accept_value(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError(str(value) + " should be an integer > 0")
        return True
        
class IntField(CloneableFieldType):
    def __init__(self, init_value, alias =None, parent=None, volatile=False,
                 modifyAllowed=True, deleteAllowed=True, rebootRequired=False):
        super().__init__(init_value, int, 'Attribute', alias, parent,
                         volatile, modifyAllowed, deleteAllowed, rebootRequired)

class BooleanField(CloneableFieldType):
    def __init__(self, init_value, alias=None, parent=None, volatile=False,
                 modifyAllowed=True, deleteAllowed=True, rebootRequired=False):
        super().__init__(init_value, bool, 'Attribute', alias, parent,
                         volatile, modifyAllowed, deleteAllowed, rebootRequired)

class StringField(CloneableFieldType):
    def __init__(self, init_value, alias=None, parent=None, volatile=False,
                 modifyAllowed=True, deleteAllowed=True, rebootRequired=False):
        super().__init__(init_value, str, 'Attribute', alias, parent,
                         volatile, modifyAllowed, deleteAllowed, rebootRequired)

class EnumTypeField(CloneableFieldType):
    def __init__(self, init_value, entype, alias=None, parent=None,
                 volatile=False, modifyAllowed=True, deleteAllowed=True,
                 rebootRequired=False):
        super().__init__(init_value, entype, 'Attribute', alias, parent,
                         volatile, modifyAllowed, deleteAllowed, rebootRequired)

class IPv4AddressField(CloneableFieldType):
    def __init__(self, init_value, alias=None, parent=None, volatile=False,
                modifyAllowed=True, deleteAllowed=True, rebootRequired=False):
        super().__init__(init_value, str, 'Attribute', alias, parent,
                         volatile, modifyAllowed, deleteAllowed, rebootRequired)

    def my_accept_value(self, value):
        if value is None:
            return True
        if isinstance(value, str):
            if not re.match('^\d+(\.\d+){3}$', value):
                return False
            for n in t.split('.'):
                if int(n) > 255:
                    return False
            return True
        else:
            return False

class IPv6AddressField(CloneableFieldType):
    def __init__(self, init_value, alias=None, parent=None, volatile=False,
                modifyAllowed=True, deleteAllowed=True, rebootRequired=False):
        super().__init__(init_value, str, 'Attribute', alias, parent,
                         volatile, modifyAllowed, deleteAllowed, rebootRequired)

class IPAddressField(CloneableFieldType):
    def __init__(self, init_value, alias=None, parent=None, volatile=False,
                modifyAllowed=True, deleteAllowed=True, rebootRequired=False):
        super().__init__(init_value, str, 'Attribute', alias, parent,
                         volatile, modifyAllowed, deleteAllowed, rebootRequired)

    # Accepts both IPv4 and IPv6

class MacAddressField(CloneableFieldType):
    def __init__(self, init_value, alias=None, parent=None, volatile=False,
                modifyAllowed=True, deleteAllowed=True, rebootRequired=False):
        super().__init__(init_value, str, 'Attribute', alias, parent,
                         volatile, modifyAllowed, deleteAllowed, rebootRequired)

    def my_accept_value(self, value):
        if value is None:
            return True
        ret = None
        if isinstance(value, str):
            ret = re.match('^[0-9a-f]{2}(:[0-9a-f]{2}){5}$', value, re.I)
        return ret is not None

class WWPNAddressField(CloneableFieldType):
    def __init__(self, init_value, alias=None, parent=None, volatile=False,
                modifyAllowed=True, deleteAllowed=True, rebootRequired=False):
        super().__init__(init_value, str, 'Attribute', alias, parent,
                         volatile, modifyAllowed, deleteAllowed, rebootRequired)

    def my_accept_value(self, value):
        if value is None:
            return True
        ret = None
        if isinstance(value, str):
            ret = re.match('^[0-9a-f]{2}(:[0-9a-f]{2}){7}$', value, re.I)
        return ret is not None
