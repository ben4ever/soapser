from spyne import 
import soapser.model as mod

class receiveItemBarCodeService(ServiceBase):
    @srpc(TXml, _returns=(Boolean, ResponseHeader))
    def receiveItemBarCode(t_xml):
        pass
