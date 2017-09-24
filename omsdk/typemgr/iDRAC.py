from omdrivers.enums.iDRAC.iDRAC import *
from omsdk.typemgr.ClassType import ClassType
from omsdk.typemgr.ArrayType import ArrayType
from omsdk.typemgr.BuiltinTypes import *

class SNMP(ClassType):

    def __init__(self, mode, parent = None):
        super().__init__(mode, None, 'SNMP', parent)

    def my_create(self):
        self.AgentCommunity_SNMP = StringField(None, 'SNMPCommunity', parent=self)
        self.DiscoveryPort_SNMP = PortField(161, 'SNMPPort', parent=self)
        self.AgentEnable_SNMP = \
                EnumTypeField(None, AgentEnable_SNMPTypes, 'SNMPEnabled', parent=self)
        self.SNMPProtocol_SNMP = \
                EnumTypeField(None, SNMPProtocol_SNMPTypes, 'SNMPVersions', parent=self)
        self.AlertPort_SNMP = PortField(162, 'SNMPTrapPort', parent=self)
        self.TrapFormat_SNMP = \
            EnumTypeField(None, TrapFormat_SNMPTypes, 'SNMPTrapFormat', parent=self)
        self.Ports = SuperFieldType(self.AlertPort_SNMP, self.DiscoveryPort_SNMP)

class NIC(ClassType):

    def __init__(self, mode, parent = None):
        super().__init__(mode, None, 'SNMP', parent)

    def my_create(self):
        self.Selection_NIC = EnumTypeField(None, Selection_NICTypes)
        self.Failover_NIC = EnumTypeField(None, Failover_NICTypes)

    def my_accept_value(self):
        #if self.Selection_NIC == SelectionTypes.Dedicated:
        #    self.Failover_NIC = None
        #    self.AutoDedicatedNIC_NIC = AutoDedicatedNICTypes.Enabled
        if self.Selection_NIC == self.Failover_NIC:
            return False
        return True                

class SysLog(ClassType):

    def __init__(self, mode, parent = None):
        super().__init__(mode, None, 'SNMP', parent)

    def my_accept_value(self):
        powerlog_enable = 'Enabled'
        if powerlog_interval <= 0:
            powerlog_interval = 0
            powerlog_enable = 'Disabled'

class Time(ClassType):
    def __init__(self, mode, parent = None):
        super().__init__(mode, None, 'Time', parent)

    # return self._get_scp_comp_field('iDRAC.Embedded.1', 'Time.1#TimeZone')
    # (self.config.arspec.iDRAC.Timezone_Time, tz, self.TimeZone),
    # (self.config.arspec.iDRAC.DayLightOffset_Time, 0, 0),
    # (self.config.arspec.iDRAC.TimeZoneOffset_Time, 0, 0) ])

class Users(ClassType):

    UserName = 'UserName_Users'

    def __init__(self, mode, parent = None):
        super().__init__(mode, None, 'SNMP', parent)

    @property
    def Key(self):
        return self.UserName_Users

    @property
    def Index(self):
        return self.UserName_Users._index

    def my_create(self):
        self.UserName_Users = StringField(None)
        self.Password_Users = StringField(None)
        self.Privilege_Users = EnumTypeField(None, Privilege_UsersTypes)
        self.IpmiLanPrivilege_Users = EnumTypeField(None, IpmiLanPrivilege_UsersTypes)
        self.Enable_Users = EnumTypeField(None, Enable_UsersTypes)
        self.SolEnable_Users = EnumTypeField(None, SolEnable_UsersTypes)
        self.ProtocolEnable_Users = EnumTypeField(None, ProtocolEnable_UsersTypes)
        self.AuthenticationProtocol_Users = EnumTypeField(None, AuthenticationProtocol_UsersTypes)
        self.PrivacyProtocol_Users = EnumTypeField(None, PrivacyProtocol_UsersTypes)

class iDRAC(ClassType):

    def __init__(self, mode, parent = None):
        super().__init__(mode, 'Component', None, parent, False)

    def my_create(self):
        self.SNMP = SNMP(mode='create', parent=self)
        #self.Users = ArrayType(Users)

class System(ClassType):

    def __init__(self, mode, parent = None):
        super().__init__(mode, 'System', None, parent, False)

    def my_create(self):
        self.iDRAC = iDRAC(mode='create', parent=self)