from spyne import srpc, Boolean, ServiceBase
import soapser.model as mod


class receiveItemBarCodeService(ServiceBase):
    @srpc(mod.TXml, _returns=ReceiveItemBarCodeOutput)
    def receiveItemBarCode(t_xml):
        return ReceiveItemBarCodeOutput(
            receiveItemBarCodeResult=True,
            ResponseHeader(ReturnType='rt1', ReturnCode='rc1',
                           ReturnMessage='rm1')
            )
