from spyne import Application, NullServer

from soapser import rpc
import soapser.model as mod

def test_receiveItemBarCode():
    obj = [
        mod.TXml(
            Header=[
                mod.Header(
                    Message_Type='mt',
                    Company_ID='ci',
                    Version='v',
                    Source='s',
                    Destination='d',
                    Action_Type='at',
                    Sequence_Number='sn',
                    Batch_ID='bi',
                    Reference_ID='ri',
                    Msg_Locale='ml',
                    Msg_Time_Zone='mtz',
                    Internal_Date_Time_Stamp='idts',
                    ),
                ],
            Message=[
                mod.Message(
                    ItemBarCodeList=[
                        mod.ItemBarCode(
                            IsPrimary='ip',
                            ItemCode='ic',
                            Barcode='b',
                            Quantity='q',
                            ActionType='at',
                            BarcodeType='bt',
                            Extensions=[
                                mod.Extensions(
                                    FieldCode='fc',
                                    FieldCodeDesc='fcd',
                                    FieldValue='fv',
                                    ),
                                mod.Extensions(
                                    FieldCode='fc',
                                    FieldCodeDesc='fcd',
                                    FieldValue='fv',
                                    ),
                                ]
                            ),
                        mod.ItemBarCode(
                            IsPrimary='ip',
                            ItemCode='ic',
                            Barcode='b',
                            Quantity='q',
                            ActionType='at',
                            BarcodeType='bt',
                            Extensions=[
                                mod.Extensions(
                                    FieldCode='fc',
                                    FieldCodeDesc='fcd',
                                    FieldValue='fv',
                                    ),
                                mod.Extensions(
                                    FieldCode='fc',
                                    FieldCodeDesc='fcd',
                                    FieldValue='fv',
                                    ),
                                ]
                            ),
                        ]
                    ),
                ]
            ),
        ]
    server = NullServer(
        Application([rpc.receiveItemBarCodeService], 'some_tns'))
    server.service.receiveItemBarCode(obj)

def test_xml_checker():
    from io import BytesIO

    from lxml import etree
    from lxml.doctestcompare import LXMLOutputChecker, PARSE_XML
    from spyne import srpc, Array, Integer, ServiceBase
    from spyne.protocol.soap import Soap11
    from spyne.server.wsgi import WsgiApplication

    class SomeService(ServiceBase):
        @srpc(Integer, _body_style='bare', _returns=Array(Integer))
        def some_call(foo):
            return [10] * foo

    req = b"""
    <soap11env:Envelope  xmlns:soap11env="http://schemas.xmlsoap.org/soap/envelope/"
                    xmlns:tns="tns">
        <soap11env:Body>
            <tns:some_call>2</tns:some_call>
        </soap11env:Body>
    </soap11env:Envelope>
    """

    app = Application([SomeService], 'tns', in_protocol=Soap11(validator='lxml'), out_protocol=Soap11(validator='lxml'))
    server = WsgiApplication(app)
    response = etree.fromstring(b''.join(server({
        'QUERY_STRING': '',
        'PATH_INFO': '/call',
        'REQUEST_METHOD': 'POST',
        'CONTENT_TYPE': 'text/xml; charset=utf8',
        'wsgi.input': BytesIO(req)
    }, lambda a, b: None, "http://null")))

    response_str = etree.tostring(response, pretty_print=True)
    print(response_str)

    expected = b"""
        <soap11env:Envelope xmlns:soap11env="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tns="tns">
          <soap11env:Body>
            <tns:some_callResponse>
              <tns:integer>10</tns:integer>
              <tns:integer>10</tns:integer>
            </tns:some_callResponse>
          </soap11env:Body>
        </soap11env:Envelope>"""
    if not LXMLOutputChecker().check_output(expected, response_str, PARSE_XML):
        raise Exception("Got: %s but expected: %s" % (response_str, expected))
