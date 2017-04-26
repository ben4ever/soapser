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
            Action_Type='read',
            Sequence_Number=1,
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
            Action_Type='read',
            Sequence_Number=1,
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


def test_receiveItemMaster_soap():
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
        <s0:receiveItemMaster xmlns:s0="Flow/Services/Custom">
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
              <s0:Item>
                <s0:ItemCode>ic</s0:ItemCode>
                <s0:IsStyle>is</s0:IsStyle>
                <s0:ActionType>at</s0:ActionType>
                <s0:ActivationDate>ad</s0:ActivationDate>
                <s0:TargetExclusive>te</s0:TargetExclusive>
                <s0:OnlineExclusive>oe</s0:OnlineExclusive>
                <s0:EssentialItem>ei</s0:EssentialItem>
                <s0:LongDescription>ld</s0:LongDescription>
                <s0:ShortDescription>sd</s0:ShortDescription>
                <s0:PrimaryBarcode>pb</s0:PrimaryBarcode>
                <s0:HazmatCode>hc</s0:HazmatCode>
                <s0:BulkyItem>bi</s0:BulkyItem>
                <s0:ItemWeight>iw</s0:ItemWeight>
                <s0:ItemHeight>ih</s0:ItemHeight>
                <s0:ItemLength>il</s0:ItemLength>
                <s0:ItemWidth>iw</s0:ItemWidth>
                <s0:ItemVolume>iv</s0:ItemVolume>
                <s0:WeightUOM>wu</s0:WeightUOM>
                <s0:DimensionUOM>du</s0:DimensionUOM>
                <s0:VolumeUOM>vu</s0:VolumeUOM>
                <s0:IsPerishable>ip</s0:IsPerishable>
                <s0:ItemPackageList>
                  <s0:ItemPackage>
                    <s0:PackageType>pt</s0:PackageType>
                    <s0:Description>d</s0:Description>
                    <s0:Quantity>q</s0:Quantity>
                    <s0:UnitWeight>uw</s0:UnitWeight>
                    <s0:UnitWidth>uw</s0:UnitWidth>
                    <s0:UnitLength>ul</s0:UnitLength>
                    <s0:UnitHeight>uh</s0:UnitHeight>
                    <s0:UnitVolume>uv</s0:UnitVolume>
                    <s0:WeigthUOM>wu</s0:WeigthUOM>
                    <s0:DimensionUOM>du</s0:DimensionUOM>
                    <s0:VolumeUOM>vu</s0:VolumeUOM>
                    <s0:IsPrimary>ip</s0:IsPrimary>
                    <s0:BusinessPartnerNumber>bpn</s0:BusinessPartnerNumber>
                    <s0:Ti>ti</s0:Ti>
                    <s0:Hi>hi</s0:Hi>
                  </s0:ItemPackage>
                </s0:ItemPackageList>
                <s0:ProductHeirarchy>
                  <s0:Variant>v</s0:Variant>
                  <s0:Product>p</s0:Product>
                  <s0:MerchandiseStyle>ms</s0:MerchandiseStyle>
                  <s0:Range>r</s0:Range>
                  <s0:MajorClass>mc</s0:MajorClass>
                  <s0:ClassGroup>cg</s0:ClassGroup>
                  <s0:Department>d</s0:Department>
                  <s0:BusinessGroup>bg</s0:BusinessGroup>
                  <s0:Section>s</s0:Section>
                  <s0:Company>c</s0:Company>
                </s0:ProductHeirarchy>
                <s0:ItemBarCodeList>
                  <s0:ItemBarCode>
                    <s0:IsPrimary>ip</s0:IsPrimary>
                    <s0:Barcode>b</s0:Barcode>
                    <s0:Quantity>q</s0:Quantity>
                    <s0:ActionType>at</s0:ActionType>
                    <s0:BarcodeType>bt</s0:BarcodeType>
                  </s0:ItemBarCode>
                  <s0:ItemBarCode>
                    <s0:IsPrimary>ip</s0:IsPrimary>
                    <s0:Barcode>b</s0:Barcode>
                    <s0:Quantity>q</s0:Quantity>
                    <s0:ActionType>at</s0:ActionType>
                    <s0:BarcodeType>bt</s0:BarcodeType>
                  </s0:ItemBarCode>
                </s0:ItemBarCodeList>
                <s0:PerishableAttribute>
                  <s0:ShelfDays>sd</s0:ShelfDays>
                  <s0:ExpireDateReqd>edr</s0:ExpireDateReqd>
                  <s0:MinReceivedToExpireDays>mrted</s0:MinReceivedToExpireDays>
                  <s0:MaxReceivedToExpireDays>mrted</s0:MaxReceivedToExpireDays>
                </s0:PerishableAttribute>
                <s0:WarehouseAttributes>
                  <s0:SecureProduct>sp</s0:SecureProduct>
                  <s0:Conveyable>c</s0:Conveyable>
                  <s0:PutawayType>pt</s0:PutawayType>
                  <s0:CrushCode>cc</s0:CrushCode>
                  <s0:VolatilityCode>vc</s0:VolatilityCode>
                </s0:WarehouseAttributes>
                <s0:Slotting>
                  <s0:LocationCode>lc</s0:LocationCode>
                  <s0:SlottingRequired>sr</s0:SlottingRequired>
                </s0:Slotting>
                <s0:Slotting>
                  <s0:LocationCode>lc</s0:LocationCode>
                  <s0:SlottingRequired>sr</s0:SlottingRequired>
                </s0:Slotting>
                <s0:ItemPromotion>
                  <s0:OnPromo>op</s0:OnPromo>
                  <s0:PromoStartWeek>psw</s0:PromoStartWeek>
                </s0:ItemPromotion>
                <s0:ItemAttributes>
                  <s0:AttributeTypeId>ati</s0:AttributeTypeId>
                  <s0:AttributeTypeDesc>atd</s0:AttributeTypeDesc>
                  <s0:AttributeHeaderId>ahi</s0:AttributeHeaderId>
                  <s0:AttributeHeaderDesc>ahd</s0:AttributeHeaderDesc>
                  <s0:AttributeCodeId>aci</s0:AttributeCodeId>
                  <s0:AttributeCode>ac</s0:AttributeCode>
                  <s0:AttributeCodeDesc>acd</s0:AttributeCodeDesc>
                </s0:ItemAttributes>
                <s0:ItemAttributes>
                  <s0:AttributeTypeId>ati</s0:AttributeTypeId>
                  <s0:AttributeTypeDesc>atd</s0:AttributeTypeDesc>
                  <s0:AttributeHeaderId>ahi</s0:AttributeHeaderId>
                  <s0:AttributeHeaderDesc>ahd</s0:AttributeHeaderDesc>
                  <s0:AttributeCodeId>aci</s0:AttributeCodeId>
                  <s0:AttributeCode>ac</s0:AttributeCode>
                  <s0:AttributeCodeDesc>acd</s0:AttributeCodeDesc>
                </s0:ItemAttributes>
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
              </s0:Item>
            </s0:Message>
          </s0:tXml>
        </s0:receiveItemMaster>
      </soap11env:Body>
    </soap11env:Envelope>
    """

    app = Application([rpc.receiveItemMasterService], NAMESPACE,
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
            <s0:receiveItemMasterResponse xmlns:s0="Flow/Services/Custom">
              <s0:receiveItemMasterResult>true</s0:receiveItemMasterResult>
              <s0:responseHeader>
                <s0:ReturnType>rt1</s0:ReturnType>
                <s0:ReturnCode>rc1</s0:ReturnCode>
                <s0:ReturnMessage>rm1</s0:ReturnMessage>
              </s0:responseHeader>
            </s0:receiveItemMasterResponse>
          </soap11env:Body>
        </soap11env:Envelope>"""
    if not LXMLOutputChecker().check_output(expected, response, PARSE_XML):
        raise Exception("Got: %s but expected: %s" % (response, expected))
