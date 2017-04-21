from spyne import Boolean, ComplexModel, Integer, String

from soapser import NAMESPACE

StringNonNillable = String(nillable=False)
StringMinOcc1 = String(min_occurs=1)
ComplexModelOrdered = ComplexModel.customize(declare_order='declared',
                                             nillable=False)


class Extensions(ComplexModelOrdered):
    __namespace__ = NAMESPACE

    FieldCode = StringNonNillable(min_occurs=1)
    FieldCodeDesc = StringNonNillable
    FieldValue = StringNonNillable(min_occurs=1)


class ItemAttributes(ComplexModelOrdered):
    __namespace__ = NAMESPACE

    AttributeTypeId = StringMinOcc1
    AttributeTypeDesc = StringMinOcc1
    AttributeHeaderId = StringMinOcc1
    AttributeHeaderDesc = StringMinOcc1
    AttributeCodeId = StringMinOcc1
    AttributeCode = StringMinOcc1
    AttributeCodeDesc = StringMinOcc1


class Slotting(ComplexModelOrdered):
    __namespace__ = NAMESPACE

    LocationCode = StringMinOcc1
    SlottingRequired = StringMinOcc1


class ItemPromotion(ComplexModelOrdered):
    __namespace__ = NAMESPACE

    OnPromo = StringMinOcc1
    PromoStartWeek = StringMinOcc1


class WarehouseAttributes(ComplexModelOrdered):
    __namespace__ = NAMESPACE

    SecureProduct = StringMinOcc1
    Conveyable = StringMinOcc1
    PutawayType = StringMinOcc1
    CrushCode = StringMinOcc1
    VolatilityCode = StringMinOcc1


class PerishableAttribute(ComplexModelOrdered):
    __namespace__ = NAMESPACE

    ShelfDays = StringMinOcc1
    ExpireDateReqd = StringMinOcc1
    MinReceivedToExpireDays = StringMinOcc1
    MaxReceivedToExpireDays = StringMinOcc1


class ItemBarCode(ComplexModelOrdered):
    __namespace__ = NAMESPACE

    IsPrimary = StringNonNillable
    ItemCode = StringNonNillable
    Barcode = StringNonNillable
    Quantity = StringNonNillable(min_occurs=1)
    ActionType = StringNonNillable
    BarcodeType = StringNonNillable
    Extensions = Extensions.customize(max_occurs='unbounded')


class ProductHeirarchy(ComplexModelOrdered):
    __namespace__ = NAMESPACE

    Variant = StringMinOcc1
    Product = StringMinOcc1
    MerchandiseStyle = StringMinOcc1
    Range = StringMinOcc1
    MajorClass = StringMinOcc1
    ClassGroup = StringMinOcc1
    Department = StringMinOcc1
    BusinessGroup = StringMinOcc1
    Section = StringMinOcc1
    Company = StringMinOcc1


class ItemPackage(ComplexModelOrdered):
    __namespace__ = NAMESPACE

    PackageType = StringNonNillable
    Description = StringMinOcc1
    Quantity = StringMinOcc1
    UnitWeight = StringMinOcc1
    UnitWidth = StringMinOcc1
    UnitLength = StringMinOcc1
    UnitHeight = StringMinOcc1
    UnitVolume = StringMinOcc1
    WeigthUOM = StringMinOcc1
    DimensionUOM = StringMinOcc1
    VolumeUOM = StringMinOcc1
    IsPrimary = StringMinOcc1
    BusinessPartnerNumber = StringMinOcc1
    Ti = StringMinOcc1
    Hi = StringMinOcc1


class ItemBarCodeList(ComplexModelOrdered):
    __namespace__ = NAMESPACE

    ItemBarCode = ItemBarCode.customize(max_occurs='unbounded')


class ItemPackageList(ComplexModelOrdered):
    __namespace__ = NAMESPACE

    ItemPackage = ItemPackage.customize(max_occurs='unbounded')


class Item(ComplexModelOrdered):
    __namespace__ = NAMESPACE

    ItemCode = StringNonNillable
    IsStyle = StringMinOcc1
    ActionType = StringMinOcc1
    ActivationDate = StringMinOcc1
    TargetExclusive = StringMinOcc1
    OnlineExclusive = StringMinOcc1
    EssentialItem = StringMinOcc1
    LongDescription = StringMinOcc1
    ShortDescription = StringMinOcc1
    PrimaryBarcode = StringMinOcc1
    HazmatCode = StringMinOcc1
    BulkyItem = StringMinOcc1
    ItemWeight = StringMinOcc1
    ItemHeight = StringMinOcc1
    ItemLength = StringMinOcc1
    ItemWidth = StringMinOcc1
    ItemVolume = StringMinOcc1
    WeightUOM = StringMinOcc1
    DimensionUOM = StringMinOcc1
    VolumeUOM = StringMinOcc1
    IsPerishable = StringMinOcc1
    ItemPackageList = ItemPackageList
    ProductHeirarchy = ProductHeirarchy
    ItemBarCodeList = ItemBarCodeList
    PerishableAttribute = PerishableAttribute
    WarehouseAttributes = WarehouseAttributes
    Slotting = Slotting.customize(max_occurs='unbounded')
    ItemPromotion = ItemPromotion
    ItemAttributes = ItemAttributes.customize(max_occurs='unbounded')
    Extensions = Extensions.customize(max_occurs='unbounded')


class Message(ComplexModelOrdered):
    __namespace__ = NAMESPACE

    ItemBarCodeList = ItemBarCodeList
    Item = Item.customize(max_occurs='unbounded')


class Header(ComplexModelOrdered):
    __namespace__ = NAMESPACE

    Message_Type = StringNonNillable
    Company_ID = StringNonNillable
    Version = StringNonNillable
    Source = StringNonNillable
    Destination = StringNonNillable
    Action_Type = StringNonNillable(values=['read', 'write'])
    Sequence_Number = Integer(nillable=False)
    Batch_ID = StringNonNillable
    Reference_ID = StringNonNillable
    Msg_Locale = StringNonNillable
    Msg_Time_Zone = StringNonNillable
    Internal_Date_Time_Stamp = StringNonNillable(min_occurs=1)


class TXml(ComplexModelOrdered):
    __namespace__ = NAMESPACE

    Header = Header.customize(min_occurs=1)
    Message = Message.customize(min_occurs=1)


class ReceiveItemBarCode(ComplexModelOrdered):
    __namespace__ = NAMESPACE

    tXml = TXml.customize(min_occurs=1)


class ReceiveItemMaster(ComplexModelOrdered):
    __namespace__ = NAMESPACE

    tXml = TXml.customize(min_occurs=1)


class ResponseHeader(ComplexModelOrdered):
    __namespace__ = NAMESPACE

    ReturnType = StringNonNillable(min_occurs=1)
    ReturnCode = StringNonNillable(min_occurs=1)
    ReturnMessage = StringNonNillable(min_occurs=1)


class ReceiveItemBarCodeOutput(ComplexModelOrdered):
    __namespace__ = NAMESPACE

    receiveItemBarCodeResult = Boolean(min_occurs=1, nillable=False)
    responseHeader = ResponseHeader


class ReceiveItemMasterOutput(ComplexModelOrdered):
    __namespace__ = NAMESPACE

    receiveItemMasterResult = Boolean(min_occurs=1, nillable=False)
    responseHeader = ResponseHeader
