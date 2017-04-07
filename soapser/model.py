from spyne import rpc, Boolean, ComplexModel, Integer, String, ServiceBase


class Extensions(ComplexModel):
    __namespace__ = 'Extensions'

    FieldCode = String
    FieldCodeDesc = String
    FieldValue = String


class ItemBarCode(ComplexModel):
    __namespace__ = 'Message'

    IsPrimary = String
    ItemCode = String
    Barcode = String
    Quantity = String(nullable=True)
    ActionType = String
    BarcodeType = String
    Extensions = Extensions.customize(max_occurs='unbounded')


class ItemBarCodeList(ComplexModel):
    __namespace__ = 'Message'

    # TODO. unbounded or inf?
    perms = ItemBarCode.customize(max_occurs='unbounded')


class Message(ComplexModel):
    __namespace__ = 'Message'

    perms = ItemBarCodeList


class Header(ComplexModel):
    __namespace__ = 'Header'

    Message_Type = String
    Company_ID = String
    Version = String
    Source = String
    Destination = String
    Action_Type = String(values=['read', 'write'])
    Sequence_Number = Integer
    Batch_ID = String
    Reference_ID = String
    Msg_Locale = String
    Msg_Time_Zone = String
    Internal_Date_Time_Stamp = String(nullable=True)


class TXml(ComplexModel):
    __namespace__ = 'tXML'

    Header = Header
    Message = Message


class ResponseHeader(ComplexModel):
    __namespace__ = 'responseHeader'

    ReturnType = String(nullable=True)
    ReturnCode = String(nullable=True)
    ReturnMessage = String(nullable=True)
