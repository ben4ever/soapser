from spyne import srpc, ServiceBase
import soapser.model as mod


class receiveItemBarCodeService(ServiceBase):
    @srpc(mod.TXml.customize(nillable=False),
          _returns=mod.ReceiveItemBarCodeOutput)
    def receiveItemBarCode(tXml):
        return mod.ReceiveItemBarCodeOutput(
            receiveItemBarCodeResult=True,
            responseHeader=mod.ResponseHeader(
                ReturnType='rt1', ReturnCode='rc1', ReturnMessage='rm1')
            )
