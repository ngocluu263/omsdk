import sys
from omsdk.http.sdkwsmanbase import WsManProtocolBase,WsManOptions
from winrm.transport import Transport
from winrm.protocol import Protocol
from omsdk.sdkprint import PrettyPrint
import traceback
import logging


logger = logging.getLogger(__name__)

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

class WmiOptions(WsManOptions):
    def __init__(self):
        if PY2:
            super(WmiOptions, self).__init__()
        else:
            super().__init__()
        self.read_timeout = 10
        self.connection_timeout = 9
        self.auth_method = 'ntlm'
        self.port = 5985

class WmiProtocol(WsManProtocolBase):
    def __init__(self, ipaddr, creds, pOptions):
        if PY2:
            super(WmiProtocol, self).__init__(ipaddr, creds, pOptions)
        else:
            super().__init__(ipaddr, creds, pOptions)
        self.ipaddr = ipaddr
        self.creds = creds
        self.pOptions = pOptions

        self.endpoint = 'https://' + ipaddr + ':' + str(pOptions.port)
        self.protocol = None
        self.transport = None

    def _proto_connect(self, reset=False):
        if reset:
            if self.transport and self.transport.session:
                self.transport.session.close()
            self.transport = None
        if not self.transport:
            try:
                self.protocol = Protocol(self.endpoint, transport='plaintext',
                   username=self.creds.username, password=self.creds.password)
                self.transport = self.protocol.transport
            except Exception as s:
                logger.debug(str(s))
                traceback.print_exc(s)

    def _proto_ship_payload(self, payload):
        try:
            return self.transport.send_message(payload)
        except Exception as ex:
            logger.debug(str(ex))
            traceback.print_exc(ex)

    def _proto_endpoint(self):
        return self.endpoint

    def _proto_reset(self):
        if self.transport and self.transport.session:
            self.transport.session.close()
        self.transport = None
        return True
