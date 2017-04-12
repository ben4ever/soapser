from spyne import Application, NullServer

from soapser import rpc
import soapser.model as mod

def test_receiveItemBarCode():
    obj = [
            mod.TXml(
                Header=[mod.Header(Message_Type='mt1', Company_ID='ci1')],
                Message=[mod.Message(ItemBarCodeList=None)],
                ),
            mod.TXml(
                Header=[mod.Header(Message_Type='mt2', Company_ID='ci2')],
                Message=[mod.Message(ItemBarCodeList=None)],
                ),
        ]
    server = NullServer(
        Application([rpc.receiveItemBarCodeService], 'some_tns'))
    server.service.Flow_Services_Custom_receiveItemBarCode(obj)
