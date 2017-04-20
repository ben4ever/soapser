from spyne import srpc, ServiceBase

from soapser import xml_writer
import soapser.model as mod


class receiveItemBarCodeService(ServiceBase):
    @srpc(mod.ReceiveItemBarCode, _returns=mod.ReceiveItemBarCodeOutput,
          _body_style='bare')
    def receiveItemBarCode(content):
        xml_writer.write_xml(content)
        return mod.ReceiveItemBarCodeOutput(
            receiveItemBarCodeResult=True,
            responseHeader=mod.ResponseHeader(
                ReturnType='rt1', ReturnCode='rc1', ReturnMessage='rm1')
            )
