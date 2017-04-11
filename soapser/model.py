from spyne import Boolean, ComplexModel, Integer, String

from soapser import NAMESPACE


class Extensions(ComplexModel):
    __namespace__ = NAMESPACE

    FieldCode = String
    FieldCodeDesc = String
    FieldValue = String


class ItemBarCode(ComplexModel):
    __namespace__ = NAMESPACE

    IsPrimary = String
    ItemCode = String
    Barcode = String
    Quantity = String(min_occurs=1)
    ActionType = String
    BarcodeType = String
    Extensions = Extensions.customize(max_occurs='unbounded')


class ItemBarCodeList(ComplexModel):
    __namespace__ = NAMESPACE

    # TODO. unbounded or inf?
    perms = ItemBarCode.customize(max_occurs='unbounded')


class Message(ComplexModel):
    __namespace__ = NAMESPACE

    perms = ItemBarCodeList


class Header(ComplexModel):
    __namespace__ = NAMESPACE

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
    Internal_Date_Time_Stamp = String(min_occurs=1)


class TXml(ComplexModel):
    __namespace__ = NAMESPACE

    Header = Header
    Message = Message


class ResponseHeader(ComplexModel):
    __namespace__ = NAMESPACE

    ReturnType = String(min_occurs=1)
    ReturnCode = String(min_occurs=1)
    ReturnMessage = String(min_occurs=1)


class ReceiveItemBarCodeOutput(ComplexModel):
    __namespace__ = NAMESPACE

    receiveItemBarCodeResult = Boolean(min_occurs=1)
    responseHeader = ResponseHeader
