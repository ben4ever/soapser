import pytest

from spyne.application import Application
from spyne.decorator import srpc
from spyne.server.null import NullServer
from spyne.service import ServiceBase

from soapser.model import Extensions, ItemBarCode


class TestItemBarCode:
    def test_extensions(self):
        e = Extensions(FieldCode='fc', FieldCodeDesc='fcd', FieldValue='fv')

        class ExtensionsService(ServiceBase):
            @srpc(Extensions, _returns=Extensions)
            def send(_e):
                return _e

        server = NullServer(Application([ExtensionsService], 'some_tns'))
        assert server.service.send(e) == e

    def test_item_bar_code(self):
        e_list = [
            Extensions(
                FieldCode='fc{}'.format(i),
                FieldCodeDesc='fcd{}'.format(i),
                FieldValue='fv{}'.format(i))
            for i in range(4)]

        ibc = ItemBarCode(IsPrimary='ip', ItemCode='ic', Barcode='b',
                          Quantity='q', ActionType='at', BarcodeType='bt',
                          Extensions=e_list)

        class ItemBarCodeService(ServiceBase):
            @srpc(ItemBarCode, _returns=ItemBarCode)
            def send(_ibc):
                return _ibc

        server = NullServer(Application([ItemBarCodeService], 'some_tns'))
        assert server.service.send(ibc) == ibc
