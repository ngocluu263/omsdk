from omsdk.sdkcenum import EnumWrapper
from omdrivers.types.iDRAC.BaseARType import *
from omdrivers.enums.iDRAC.NIC import *
import logging

logger = logging.getLogger(__name__)

class NIC(BaseARType):

    def my_create(self):
        self.BannerMessageTimeout = None
        self.BlnkLeds = "15"
        self.BootOptionROM = None
        self.BootOrderFirstFCoETarget = "0"
        self.BootOrderFourthFCoETarget = "0"
        self.BootOrderSecondFCoETarget = "0"
        self.BootOrderThirdFCoETarget = "0"
        self.BootRetryCnt = BootRetryCntTypes.NoRetry
        self.BootStrapType = BootStrapTypeTypes.AutoDetect
        self.ChapAuthEnable = ChapAuthEnableTypes.Disabled
        self.ChapMutualAuth = ChapMutualAuthTypes.Disabled
        self.ConnectFirstFCoETarget = ConnectFirstFCoETargetTypes.Disabled
        self.ConnectFirstTgt = ConnectFirstTgtTypes.Disabled
        self.ConnectSecondTgt = ConnectSecondTgtTypes.Disabled
        self.DhcpVendId = None
        self.EEEControl = None
        self.FCoEBootScanSelection = FCoEBootScanSelectionTypes.Disabled
        self.FCoEFabricDiscoveryRetryCnt = None
        self.FCoEFirstHddTarget = FCoEFirstHddTargetTypes.Disabled
        self.FCoELnkUpDelayTime = None
        self.FCoELunBusyRetryCnt = None
        self.FCoEOffloadMode = FCoEOffloadModeTypes.Disabled
        self.FCoETgtBoot = FCoETgtBootTypes.Disabled
        self.FirstFCoEBootTargetLUN = None
        self.FirstFCoEFCFVLANID = None
        self.FirstFCoEWWPNTarget = None
        self.FirstHddTarget = FirstHddTargetTypes.Disabled
        self.FirstTgtBootLun = None
        self.FirstTgtChapId = None
        self.FirstTgtChapPwd = None
        self.FirstTgtIpAddress = None
        self.FirstTgtIpVer = FirstTgtIpVerTypes.IPv4
        self.FirstTgtIscsiName = None
        self.FirstTgtTcpPort = None
        self.FlowControlSetting = FlowControlSettingTypes.Auto
        self.HairpinMode = HairpinModeTypes.Disabled
        self.HideSetupPrompt = HideSetupPromptTypes.Disabled
        self.IpAutoConfig = IpAutoConfigTypes.Disabled
        self.IpVer = IpVerTypes.IPv4
        self.IscsiInitiatorChapId = None
        self.IscsiInitiatorChapPwd = None
        self.IscsiInitiatorGateway = None
        self.IscsiInitiatorIpAddr = None
        self.IscsiInitiatorIpv4Addr = None
        self.IscsiInitiatorIpv4Gateway = None
        self.IscsiInitiatorIpv4PrimDns = None
        self.IscsiInitiatorIpv4SecDns = None
        self.IscsiInitiatorIpv6Addr = None
        self.IscsiInitiatorIpv6Gateway = None
        self.IscsiInitiatorIpv6PrimDns = None
        self.IscsiInitiatorIpv6SecDns = None
        self.IscsiInitiatorName = None
        self.IscsiInitiatorPrimDns = None
        self.IscsiInitiatorSecDns = None
        self.IscsiInitiatorSubnet = None
        self.IscsiInitiatorSubnetPrefix = None
        self.IscsiTgtBoot = IscsiTgtBootTypes.Disabled
        self.IscsiVLanId = None
        self.IscsiVLanMode = IscsiVLanModeTypes.Disabled
        self.IscsiViaDHCP = IscsiViaDHCPTypes.Disabled
        self.LegacyBootProto = None
        self.LnkSpeed = None
        self.LnkUpDelayTime = "0"
        self.LocalDCBXWillingMode = LocalDCBXWillingModeTypes.Enabled
        self.LogicalPortEnable = LogicalPortEnableTypes.Disabled
        self.LunBusyRetryCnt = None
        self.MTUParams = None
        self.MaxBandwidth = "100"
        self.MinBandwidth = "0"
        self.NPCP = NPCPTypes.Enabled
        self.NParEP = NParEPTypes.Disabled
        self.NetworkPartitioningMode = NetworkPartitioningModeTypes.SIP
        self.NicMode = None
        self.NicPartitioning = NicPartitioningTypes.Disabled
        self.NumberVFAdvertised = "0"
        self.PriorityGroup0BandwidthAllocation = None
        self.PriorityGroup0ProtocolAssignment = None
        self.PriorityGroup15BandwidthAllocation = None
        self.PriorityGroup15ProtocolAssignment = None
        self.PriorityGroup1BandwidthAllocation = None
        self.PriorityGroup1ProtocolAssignment = None
        self.PriorityGroup2BandwidthAllocation = None
        self.PriorityGroup2ProtocolAssignment = None
        self.PriorityGroup3BandwidthAllocation = None
        self.PriorityGroup3ProtocolAssignment = None
        self.PriorityGroup4BandwidthAllocation = None
        self.PriorityGroup4ProtocolAssignment = None
        self.PriorityGroup5BandwidthAllocation = None
        self.PriorityGroup5ProtocolAssignment = None
        self.PriorityGroup6BandwidthAllocation = None
        self.PriorityGroup6ProtocolAssignment = None
        self.PriorityGroup7BandwidthAllocation = None
        self.PriorityGroup7ProtocolAssignment = None
        self.PriorityGroupBandwidthAllocation = None
        self.RDMAApplicationProfile = None
        self.RDMANICModeOnPort = None
        self.SecondTgtBootLun = None
        self.SecondTgtChapId = None
        self.SecondTgtChapPwd = None
        self.SecondTgtIpAddress = None
        self.SecondTgtIpVer = SecondTgtIpVerTypes.IPv4
        self.SecondTgtIscsiName = None
        self.SecondTgtTcpPort = None
        self.SecondaryDeviceMacAddr = None
        self.TcpIpViaDHCP = TcpIpViaDHCPTypes.Disabled
        self.TcpTimestmp = TcpTimestmpTypes.Disabled
        self.TotalNumberLogicalPorts = TotalNumberLogicalPortsTypes.T_2
        self.UseIndTgtName = UseIndTgtNameTypes.Disabled
        self.UseIndTgtPortal = UseIndTgtPortalTypes.Disabled
        self.VFDistribution = None
        self.VLanId = None
        self.VLanMode = VLanModeTypes.Disabled
        self.VirtFIPMacAddr = "00:00:00:00:00:00"
        self.VirtIscsiMacAddr = "00:00:00:00:00:00"
        self.VirtMacAddr = "00:00:00:00:00:00"
        self.VirtWWN = "00:00:00:00:00:00:00:00"
        self.VirtWWPN = "00:00:00:00:00:00:00:00"
        self.VirtualizationMode = VirtualizationModeTypes.NONE
        self.WakeOnLan = None
        self.WakeOnLanLnkSpeed = WakeOnLanLnkSpeedTypes.AutoNeg
        self.WinHbaBootMode = WinHbaBootModeTypes.Disabled
        self.iScsiOffloadMode = iScsiOffloadModeTypes.Disabled
        return self

    def my_modify(self):
        self.BannerMessageTimeout = None
        self.BlnkLeds = "15"
        self.BootOptionROM = None
        self.BootOrderFirstFCoETarget = "0"
        self.BootOrderFourthFCoETarget = "0"
        self.BootOrderSecondFCoETarget = "0"
        self.BootOrderThirdFCoETarget = "0"
        self.BootRetryCnt = BootRetryCntTypes.NoRetry
        self.BootStrapType = BootStrapTypeTypes.AutoDetect
        self.ChapAuthEnable = ChapAuthEnableTypes.Disabled
        self.ChapMutualAuth = ChapMutualAuthTypes.Disabled
        self.ConnectFirstFCoETarget = ConnectFirstFCoETargetTypes.Disabled
        self.ConnectFirstTgt = ConnectFirstTgtTypes.Disabled
        self.ConnectSecondTgt = ConnectSecondTgtTypes.Disabled
        self.DhcpVendId = None
        self.EEEControl = None
        self.FCoEBootScanSelection = FCoEBootScanSelectionTypes.Disabled
        self.FCoEFabricDiscoveryRetryCnt = None
        self.FCoEFirstHddTarget = FCoEFirstHddTargetTypes.Disabled
        self.FCoELnkUpDelayTime = None
        self.FCoELunBusyRetryCnt = None
        self.FCoEOffloadMode = FCoEOffloadModeTypes.Disabled
        self.FCoETgtBoot = FCoETgtBootTypes.Disabled
        self.FirstFCoEBootTargetLUN = None
        self.FirstFCoEFCFVLANID = None
        self.FirstFCoEWWPNTarget = None
        self.FirstHddTarget = FirstHddTargetTypes.Disabled
        self.FirstTgtBootLun = None
        self.FirstTgtChapId = None
        self.FirstTgtChapPwd = None
        self.FirstTgtIpAddress = None
        self.FirstTgtIpVer = FirstTgtIpVerTypes.IPv4
        self.FirstTgtIscsiName = None
        self.FirstTgtTcpPort = None
        self.FlowControlSetting = FlowControlSettingTypes.Auto
        self.HairpinMode = HairpinModeTypes.Disabled
        self.HideSetupPrompt = HideSetupPromptTypes.Disabled
        self.IpAutoConfig = IpAutoConfigTypes.Disabled
        self.IpVer = IpVerTypes.IPv4
        self.IscsiInitiatorChapId = None
        self.IscsiInitiatorChapPwd = None
        self.IscsiInitiatorGateway = None
        self.IscsiInitiatorIpAddr = None
        self.IscsiInitiatorIpv4Addr = None
        self.IscsiInitiatorIpv4Gateway = None
        self.IscsiInitiatorIpv4PrimDns = None
        self.IscsiInitiatorIpv4SecDns = None
        self.IscsiInitiatorIpv6Addr = None
        self.IscsiInitiatorIpv6Gateway = None
        self.IscsiInitiatorIpv6PrimDns = None
        self.IscsiInitiatorIpv6SecDns = None
        self.IscsiInitiatorName = None
        self.IscsiInitiatorPrimDns = None
        self.IscsiInitiatorSecDns = None
        self.IscsiInitiatorSubnet = None
        self.IscsiInitiatorSubnetPrefix = None
        self.IscsiTgtBoot = IscsiTgtBootTypes.Disabled
        self.IscsiVLanId = None
        self.IscsiVLanMode = IscsiVLanModeTypes.Disabled
        self.IscsiViaDHCP = IscsiViaDHCPTypes.Disabled
        self.LegacyBootProto = None
        self.LnkSpeed = None
        self.LnkUpDelayTime = "0"
        self.LocalDCBXWillingMode = LocalDCBXWillingModeTypes.Enabled
        self.LogicalPortEnable = LogicalPortEnableTypes.Disabled
        self.LunBusyRetryCnt = None
        self.MTUParams = None
        self.MaxBandwidth = "100"
        self.MinBandwidth = "0"
        self.NPCP = NPCPTypes.Enabled
        self.NParEP = NParEPTypes.Disabled
        self.NetworkPartitioningMode = NetworkPartitioningModeTypes.SIP
        self.NicMode = None
        self.NicPartitioning = NicPartitioningTypes.Disabled
        self.NumberVFAdvertised = "0"
        self.PriorityGroup0BandwidthAllocation = None
        self.PriorityGroup0ProtocolAssignment = None
        self.PriorityGroup15BandwidthAllocation = None
        self.PriorityGroup15ProtocolAssignment = None
        self.PriorityGroup1BandwidthAllocation = None
        self.PriorityGroup1ProtocolAssignment = None
        self.PriorityGroup2BandwidthAllocation = None
        self.PriorityGroup2ProtocolAssignment = None
        self.PriorityGroup3BandwidthAllocation = None
        self.PriorityGroup3ProtocolAssignment = None
        self.PriorityGroup4BandwidthAllocation = None
        self.PriorityGroup4ProtocolAssignment = None
        self.PriorityGroup5BandwidthAllocation = None
        self.PriorityGroup5ProtocolAssignment = None
        self.PriorityGroup6BandwidthAllocation = None
        self.PriorityGroup6ProtocolAssignment = None
        self.PriorityGroup7BandwidthAllocation = None
        self.PriorityGroup7ProtocolAssignment = None
        self.PriorityGroupBandwidthAllocation = None
        self.RDMAApplicationProfile = None
        self.RDMANICModeOnPort = None
        self.SecondTgtBootLun = None
        self.SecondTgtChapId = None
        self.SecondTgtChapPwd = None
        self.SecondTgtIpAddress = None
        self.SecondTgtIpVer = SecondTgtIpVerTypes.IPv4
        self.SecondTgtIscsiName = None
        self.SecondTgtTcpPort = None
        self.SecondaryDeviceMacAddr = None
        self.TcpIpViaDHCP = TcpIpViaDHCPTypes.Disabled
        self.TcpTimestmp = TcpTimestmpTypes.Disabled
        self.TotalNumberLogicalPorts = TotalNumberLogicalPortsTypes.T_2
        self.UseIndTgtName = UseIndTgtNameTypes.Disabled
        self.UseIndTgtPortal = UseIndTgtPortalTypes.Disabled
        self.VFDistribution = None
        self.VLanId = None
        self.VLanMode = VLanModeTypes.Disabled
        self.VirtFIPMacAddr = "00:00:00:00:00:00"
        self.VirtIscsiMacAddr = "00:00:00:00:00:00"
        self.VirtMacAddr = "00:00:00:00:00:00"
        self.VirtWWN = "00:00:00:00:00:00:00:00"
        self.VirtWWPN = "00:00:00:00:00:00:00:00"
        self.VirtualizationMode = VirtualizationModeTypes.NONE
        self.WakeOnLan = None
        self.WakeOnLanLnkSpeed = WakeOnLanLnkSpeedTypes.AutoNeg
        self.WinHbaBootMode = WinHbaBootModeTypes.Disabled
        self.iScsiOffloadMode = iScsiOffloadModeTypes.Disabled
        return self

    def my_delete(self):
        self.BannerMessageTimeout = None
        self.BlnkLeds = "15"
        self.BootOptionROM = None
        self.BootOrderFirstFCoETarget = "0"
        self.BootOrderFourthFCoETarget = "0"
        self.BootOrderSecondFCoETarget = "0"
        self.BootOrderThirdFCoETarget = "0"
        self.BootRetryCnt = BootRetryCntTypes.NoRetry
        self.BootStrapType = BootStrapTypeTypes.AutoDetect
        self.ChapAuthEnable = ChapAuthEnableTypes.Disabled
        self.ChapMutualAuth = ChapMutualAuthTypes.Disabled
        self.ConnectFirstFCoETarget = ConnectFirstFCoETargetTypes.Disabled
        self.ConnectFirstTgt = ConnectFirstTgtTypes.Disabled
        self.ConnectSecondTgt = ConnectSecondTgtTypes.Disabled
        self.DhcpVendId = None
        self.EEEControl = None
        self.FCoEBootScanSelection = FCoEBootScanSelectionTypes.Disabled
        self.FCoEFabricDiscoveryRetryCnt = None
        self.FCoEFirstHddTarget = FCoEFirstHddTargetTypes.Disabled
        self.FCoELnkUpDelayTime = None
        self.FCoELunBusyRetryCnt = None
        self.FCoEOffloadMode = FCoEOffloadModeTypes.Disabled
        self.FCoETgtBoot = FCoETgtBootTypes.Disabled
        self.FirstFCoEBootTargetLUN = None
        self.FirstFCoEFCFVLANID = None
        self.FirstFCoEWWPNTarget = None
        self.FirstHddTarget = FirstHddTargetTypes.Disabled
        self.FirstTgtBootLun = None
        self.FirstTgtChapId = None
        self.FirstTgtChapPwd = None
        self.FirstTgtIpAddress = None
        self.FirstTgtIpVer = FirstTgtIpVerTypes.IPv4
        self.FirstTgtIscsiName = None
        self.FirstTgtTcpPort = None
        self.FlowControlSetting = FlowControlSettingTypes.Auto
        self.HairpinMode = HairpinModeTypes.Disabled
        self.HideSetupPrompt = HideSetupPromptTypes.Disabled
        self.IpAutoConfig = IpAutoConfigTypes.Disabled
        self.IpVer = IpVerTypes.IPv4
        self.IscsiInitiatorChapId = None
        self.IscsiInitiatorChapPwd = None
        self.IscsiInitiatorGateway = None
        self.IscsiInitiatorIpAddr = None
        self.IscsiInitiatorIpv4Addr = None
        self.IscsiInitiatorIpv4Gateway = None
        self.IscsiInitiatorIpv4PrimDns = None
        self.IscsiInitiatorIpv4SecDns = None
        self.IscsiInitiatorIpv6Addr = None
        self.IscsiInitiatorIpv6Gateway = None
        self.IscsiInitiatorIpv6PrimDns = None
        self.IscsiInitiatorIpv6SecDns = None
        self.IscsiInitiatorName = None
        self.IscsiInitiatorPrimDns = None
        self.IscsiInitiatorSecDns = None
        self.IscsiInitiatorSubnet = None
        self.IscsiInitiatorSubnetPrefix = None
        self.IscsiTgtBoot = IscsiTgtBootTypes.Disabled
        self.IscsiVLanId = None
        self.IscsiVLanMode = IscsiVLanModeTypes.Disabled
        self.IscsiViaDHCP = IscsiViaDHCPTypes.Disabled
        self.LegacyBootProto = None
        self.LnkSpeed = None
        self.LnkUpDelayTime = "0"
        self.LocalDCBXWillingMode = LocalDCBXWillingModeTypes.Enabled
        self.LogicalPortEnable = LogicalPortEnableTypes.Disabled
        self.LunBusyRetryCnt = None
        self.MTUParams = None
        self.MaxBandwidth = "100"
        self.MinBandwidth = "0"
        self.NPCP = NPCPTypes.Enabled
        self.NParEP = NParEPTypes.Disabled
        self.NetworkPartitioningMode = NetworkPartitioningModeTypes.SIP
        self.NicMode = None
        self.NicPartitioning = NicPartitioningTypes.Disabled
        self.NumberVFAdvertised = "0"
        self.PriorityGroup0BandwidthAllocation = None
        self.PriorityGroup0ProtocolAssignment = None
        self.PriorityGroup15BandwidthAllocation = None
        self.PriorityGroup15ProtocolAssignment = None
        self.PriorityGroup1BandwidthAllocation = None
        self.PriorityGroup1ProtocolAssignment = None
        self.PriorityGroup2BandwidthAllocation = None
        self.PriorityGroup2ProtocolAssignment = None
        self.PriorityGroup3BandwidthAllocation = None
        self.PriorityGroup3ProtocolAssignment = None
        self.PriorityGroup4BandwidthAllocation = None
        self.PriorityGroup4ProtocolAssignment = None
        self.PriorityGroup5BandwidthAllocation = None
        self.PriorityGroup5ProtocolAssignment = None
        self.PriorityGroup6BandwidthAllocation = None
        self.PriorityGroup6ProtocolAssignment = None
        self.PriorityGroup7BandwidthAllocation = None
        self.PriorityGroup7ProtocolAssignment = None
        self.PriorityGroupBandwidthAllocation = None
        self.RDMAApplicationProfile = None
        self.RDMANICModeOnPort = None
        self.SecondTgtBootLun = None
        self.SecondTgtChapId = None
        self.SecondTgtChapPwd = None
        self.SecondTgtIpAddress = None
        self.SecondTgtIpVer = SecondTgtIpVerTypes.IPv4
        self.SecondTgtIscsiName = None
        self.SecondTgtTcpPort = None
        self.SecondaryDeviceMacAddr = None
        self.TcpIpViaDHCP = TcpIpViaDHCPTypes.Disabled
        self.TcpTimestmp = TcpTimestmpTypes.Disabled
        self.TotalNumberLogicalPorts = TotalNumberLogicalPortsTypes.T_2
        self.UseIndTgtName = UseIndTgtNameTypes.Disabled
        self.UseIndTgtPortal = UseIndTgtPortalTypes.Disabled
        self.VFDistribution = None
        self.VLanId = None
        self.VLanMode = VLanModeTypes.Disabled
        self.VirtFIPMacAddr = "00:00:00:00:00:00"
        self.VirtIscsiMacAddr = "00:00:00:00:00:00"
        self.VirtMacAddr = "00:00:00:00:00:00"
        self.VirtWWN = "00:00:00:00:00:00:00:00"
        self.VirtWWPN = "00:00:00:00:00:00:00:00"
        self.VirtualizationMode = VirtualizationModeTypes.NONE
        self.WakeOnLan = None
        self.WakeOnLanLnkSpeed = WakeOnLanLnkSpeedTypes.AutoNeg
        self.WinHbaBootMode = WinHbaBootModeTypes.Disabled
        self.iScsiOffloadMode = iScsiOffloadModeTypes.Disabled
        return self
