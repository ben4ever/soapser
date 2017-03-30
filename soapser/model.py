from spyne import rpc, Boolean, ComplexModel, Integer, String, ServiceBase


class Extensions(ComplexModel):
    __namespace__ = 'Extensions'

    FieldCode = String(min_occurs=0)
    FieldCodeDesc = String(min_occurs=0)
    FieldValue = String(min_occurs=0)


class ItemBarCode(ComplexModel):
    __namespace__ = 'Message'

    IsPrimary = String(min_occurs=0)
    IsPrimary = String(min_occurs=0)
    ItemCode = String(min_occurs=0)
    Barcode = String(min_occurs=0)
    Quantity = String(nullable=True)
    ActionType = String(min_occurs=0)
    BarcodeType = String(min_occurs=0)
    Extensions = Extensions.customize(min_occurs=0, max_occurs='unbounded')


class ItemBarCodeList(ComplexModel):
    __namespace__ = 'Message'

    # TODO. unbounded or inf?
    perms = ItemBarCode.customize(min_occurs=0, max_occurs='unbounded')


class Message(ComplexModel):
    __namespace__ = 'Message'

    perms = ItemBarCodeList.customize(min_occurs=0)


class Header(ComplexModel):
    __namespace__ = 'Header'

    Message_Type = String(min_occurs=0)
    Company_ID = String(min_occurs=0)
    Version = String(min_occurs=0)
    Source = String(min_occurs=0)
    Destination = String(min_occurs=0)
    Action_Type = String(min_occurs=0, values=['read', 'write'])
    Sequence_Number = Integer(min_occurs=0)
    Batch_ID = String(min_occurs=0)
    Reference_ID = String(min_occurs=0)
    Msg_Locale = String(min_occurs=0)
    Msg_Time_Zone = String(min_occurs=0)
    Internal_Date_Time_Stamp = String(min_occurs=0, nullable=True)


class TXml(ComplexModel):
    __namespace__ = 'tXML'

    Header = Header.customize(min_occurs=0)
    Message = Message.customize(min_occurs=0)


class ResponseHeader(ComplexModel):
    __namespace__ = 'responseHeader'

    ReturnType = String(nullable=True)
    ReturnCode = String(nullable=True)
    ReturnMessage = String(nullable=True)


class ItemBarCodeService(ServiceBase):
    @rpc(TXml, _returns=(Boolean, ResponseHeader.customize(min_occurs=0)))
    def receiveItemBarCode(ctx, t_xml):
        pass
