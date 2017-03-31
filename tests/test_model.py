import pytest

from spyne.application import Application
from spyne.decorator import srpc
from spyne.server.null import NullServer
from spyne.service import ServiceBase

from soapser.model import Extensions


class TestItemBarCode:
    def test_extensions(self):
        ext = Extensions(FieldCode='fc', FieldCodeDesc='fcd', FieldValue='fv')

        class ExtensionsService(ServiceBase):
            @srpc(Extensions, _returns=Extensions)
            def send(e):
                return e

        server = NullServer(Application([ExtensionsService], 'some_tns'))
        assert server.service.send(ext) == ext
