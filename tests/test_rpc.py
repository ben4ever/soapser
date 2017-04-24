from spyne import Application, NullServer

from soapser import rpc
import soapser.model as mod

def test_receiveItemBarCode():
    obj = mod.TXml(
        Header=mod.Header(
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
        Message=mod.Message(
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
        )
    server = NullServer(
        Application([rpc.receiveItemBarCodeService], 'some_tns'))
    # Using ``_body_style='bare'`` seems to cause to always return
    # ``None``. Hence we can't check the response object.
    server.service.receiveItemBarCode(obj)


def test_receiveItemMaster():
    obj = mod.TXml(
        Header=mod.Header(
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
        Message=mod.Message(
            Item=[
                mod.Item(
                    ItemCode='ic',
                    IsStyle='is',
                    ActionType='at',
                    ActivationDate='ad',
                    TargetExclusive='te',
                    OnlineExclusive='oe',
                    EssentialItem='ei',
                    LongDescription='ld',
                    ShortDescription='sd',
                    PrimaryBarcode='pb',
                    HazmatCode='hc',
                    BulkyItem='bi',
                    ItemWeight='iw',
                    ItemHeight='ih',
                    ItemLength='il',
                    ItemWidth='iw',
                    ItemVolume='iv',
                    WeightUOM='wu',
                    DimensionUOM='du',
                    VolumeUOM='vu',
                    IsPerishable='ip',
                    ItemPackageList=[
                        mod.ItemPackage(
                            PackageType='pt',
                            Description='d',
                            Quantity='q',
                            UnitWeight='uw',
                            UnitWidth='uw',
                            UnitLength='ul',
                            UnitHeight='uh',
                            UnitVolume='uv',
                            WeigthUOM='wu',
                            DimensionUOM='du',
                            VolumeUOM='vu',
                            IsPrimary='ip',
                            BusinessPartnerNumber='bpn',
                            Ti='ti',
                            Hi='hi',
                            ),
                        ],
                    ProductHeirarchy=mod.ProductHeirarchy(
                        Variant='v',
                        Product='p',
                        MerchandiseStyle='ms',
                        Range='r',
                        MajorClass='mc',
                        ClassGroup='cg',
                        Department='d',
                        BusinessGroup='bg',
                        Section='s',
                        Company='c',
                        ),
                    ItemBarCodeList=[
                        mod.ItemBarCode(
                            IsPrimary='ip',
                            Barcode='b',
                            Quantity='q',
                            ActionType='at',
                            BarcodeType='bt',
                            ),
                        mod.ItemBarCode(
                            IsPrimary='ip',
                            Barcode='b',
                            Quantity='q',
                            ActionType='at',
                            BarcodeType='bt',
                            ),
                        ],
                    PerishableAttribute=mod.PerishableAttribute(
                        ShelfDays='sd',
                        ExpireDateReqd='edr',
                        MinReceivedToExpireDays='mrted',
                        MaxReceivedToExpireDays='mrted',
                        ),
                    WarehouseAttributes=mod.WarehouseAttributes(
                        SecureProduct='sp',
                        Conveyable='c',
                        PutawayType='pt',
                        CrushCode='cc',
                        VolatilityCode='vc',
                        ),
                    Slotting=[
                        mod.Slotting(
                            LocationCode='lc',
                            SlottingRequired='sr',
                            ),
                        mod.Slotting(
                            LocationCode='lc',
                            SlottingRequired='sr',
                            ),
                        ],
                    ItemPromotion=mod.ItemPromotion(
                        OnPromo='op',
                        PromoStartWeek='psw',
                        ),
                    ItemAttributes=[
                        mod.ItemAttributes(
                            AttributeTypeId='ati',
                            AttributeTypeDesc='atd',
                            AttributeHeaderId='ahi',
                            AttributeHeaderDesc='ahd',
                            AttributeCodeId='aci',
                            AttributeCode='ac',
                            AttributeCodeDesc='acd',
                            ),
                        mod.ItemAttributes(
                            AttributeTypeId='ati',
                            AttributeTypeDesc='atd',
                            AttributeHeaderId='ahi',
                            AttributeHeaderDesc='ahd',
                            AttributeCodeId='aci',
                            AttributeCode='ac',
                            AttributeCodeDesc='acd',
                            ),
                        ],
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
        )
    server = NullServer(
        Application([rpc.receiveItemMasterService], 'some_tns'))
    # Using ``_body_style='bare'`` seems to cause to always return
    # ``None``. Hence we can't check the response object.
    server.service.receiveItemMaster(obj)


def test_receiveItemBarCode_soap():
    from io import BytesIO

    from lxml import etree
    from lxml.doctestcompare import LXMLOutputChecker, PARSE_XML
    from spyne import srpc, Array, Integer, ServiceBase
    from spyne.protocol.soap import Soap11
    from spyne.server.wsgi import WsgiApplication

    from soapser import NAMESPACE

    req = b"""
    <soap11env:Envelope
        xmlns:soap11env="http://schemas.xmlsoap.org/soap/envelope/">
      <soap11env:Body>
        <s0:receiveItemBarCode xmlns:s0="Flow/Services/Custom">
          <s0:tXml>
            <s0:Header>
              <s0:Message_Type>mt</s0:Message_Type>
              <s0:Company_ID>ci</s0:Company_ID>
              <s0:Version>v</s0:Version>
              <s0:Source>s</s0:Source>
              <s0:Destination>d</s0:Destination>
              <s0:Action_Type>read</s0:Action_Type>
              <s0:Sequence_Number>1</s0:Sequence_Number>
              <s0:Batch_ID>bi</s0:Batch_ID>
              <s0:Reference_ID>ri</s0:Reference_ID>
              <s0:Msg_Locale>ml</s0:Msg_Locale>
              <s0:Msg_Time_Zone>mtz</s0:Msg_Time_Zone>
              <s0:Internal_Date_Time_Stamp>idts</s0:Internal_Date_Time_Stamp>
            </s0:Header>
            <s0:Message>
              <s0:ItemBarCodeList>
                <s0:ItemBarCode>
                  <s0:IsPrimary>ip</s0:IsPrimary>
                  <s0:ItemCode>ic</s0:ItemCode>
                  <s0:Barcode>b</s0:Barcode>
                  <s0:Quantity>q</s0:Quantity>
                  <s0:ActionType>at</s0:ActionType>
                  <s0:BarcodeType>bt</s0:BarcodeType>
                  <s0:Extensions>
                    <s0:FieldCode>fc</s0:FieldCode>
                    <s0:FieldCodeDesc>fcd</s0:FieldCodeDesc>
                    <s0:FieldValue>fv</s0:FieldValue>
                  </s0:Extensions>
                  <s0:Extensions>
                    <s0:FieldCode>fc</s0:FieldCode>
                    <s0:FieldCodeDesc>fcd</s0:FieldCodeDesc>
                    <s0:FieldValue>fv</s0:FieldValue>
                  </s0:Extensions>
                </s0:ItemBarCode>
              </s0:ItemBarCodeList>
            </s0:Message>
          </s0:tXml>
        </s0:receiveItemBarCode>
      </soap11env:Body>
    </soap11env:Envelope>
    """

    app = Application([rpc.receiveItemBarCodeService], NAMESPACE,
                      in_protocol=Soap11(validator='lxml'),
                      out_protocol=Soap11(validator='lxml'))
    server = WsgiApplication(app)
    response = b''.join(server({
        #'QUERY_STRING': '',
        #'PATH_INFO': '/call',
        'REQUEST_METHOD': 'POST',
        'CONTENT_TYPE': 'text/xml',
        'wsgi.input': BytesIO(req)
    }, lambda a, b: None, "http://null"))

    expected = b"""
        <soap11env:Envelope
            xmlns:soap11env="http://schemas.xmlsoap.org/soap/envelope/">
          <soap11env:Body>
            <s0:receiveItemBarCodeResponse xmlns:s0="Flow/Services/Custom">
              <s0:receiveItemBarCodeResult>true</s0:receiveItemBarCodeResult>
              <s0:responseHeader>
                <s0:ReturnType>rt1</s0:ReturnType>
                <s0:ReturnCode>rc1</s0:ReturnCode>
                <s0:ReturnMessage>rm1</s0:ReturnMessage>
              </s0:responseHeader>
            </s0:receiveItemBarCodeResponse>
          </soap11env:Body>
        </soap11env:Envelope>"""
    if not LXMLOutputChecker().check_output(expected, response, PARSE_XML):
        raise Exception("Got: %s but expected: %s" % (response, expected))
