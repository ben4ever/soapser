from spyne import srpc, ServiceBase

from soapser import xml_writer
import soapser.model as mod


class receiveItemBarCodeService(ServiceBase):
    @srpc(mod.ReceiveItemBarCode, _returns=mod.ReceiveItemBarCodeOutput,
          _body_style='bare')
    def receiveItemBarCode(content):
        xml_writer.write_receiveItemBarCode(content)
        return mod.ReceiveItemBarCodeOutput(
            receiveItemBarCodeResult=True,
            responseHeader=mod.ResponseHeader(
                ReturnType='ItemCrossReference',
                ReturnCode='Success',
                ReturnMessage='ItemCrossReference Interface Process Completed '
                              'Successfully')
            )


class receiveItemMasterService(ServiceBase):
    @srpc(mod.ReceiveItemMaster, _returns=mod.ReceiveItemMasterOutput,
          _body_style='bare')
    def receiveItemMaster(content):
        xml_writer.write_receiveItemMaster(content)
        return mod.ReceiveItemMasterOutput(
            receiveItemMasterResult=True,
            responseHeader=mod.ResponseHeader(
                ReturnType='Item Master',
                ReturnCode='Success',
                ReturnMessage='Item Master Interface Process Completed '
                              'Successfully')
            )
