import pytest

import requests_mock
from spyne import Application, Integer, NullServer, ServiceBase, srpc
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from zeep import Client

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

    @pytest.mark.skipif(True, reason=
        "This test is an attempt to get data validation working through "
        "`zeep` since `spyne`'s `NullServer` doesn't offer any data "
        "validation (see https://github.com/arskom/spyne/issues/318). With "
        "`spyne`, data validation is only possible with an actual server "
        "application like `WsgiApplication`. I hoped that `zeep` would do "
        "rigid data validation but it seems that it only does some very basic "
        "one for `minOccurs` and `maxOccurs` - for now (see release notes for "
        "0.25.0).\n"

        "Until proper data validation is implemented by `zeep`, this test is "
        "therefore redundant.")
    def test_wsdl_validation(self, tmpdir_factory):
        val = 10

        class IntegerService(ServiceBase):
            @srpc(Integer(ge=20), _returns=Integer)
            def send(_val):
                return _val

        app = Application([IntegerService], 'some_tns',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11(validator='lxml'))

        # We have to write the WSDL file using a `WsgiApplication` so
        # that we get a proper transport URL as it would be
        # `noconn://null.spyne` with NullServer.
        wsgi_app = WsgiApplication(app)
        wsgi_app.doc.wsdl11.build_interface_document('mock://foo')
        wsdl_file = tmpdir_factory.getbasetemp().join('wsdl')
        wsdl_file.write(wsgi_app.doc.wsdl11.get_interface_document())

        server = NullServer(app, ostr=True)
        c = Client(str(wsdl_file))
        with requests_mock.mock() as m:
            m.post('mock://foo', content=server.service.send(val)[0])
            # This should throw because of `Integer(ge=20)` but doesn't.
            assert c.service.send(10) == val
