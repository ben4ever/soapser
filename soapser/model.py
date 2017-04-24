from spyne import Boolean, ComplexModel, Integer, String

from soapser import NAMESPACE

StringNonNillable = String(nillable=False)
StringMinOcc1 = String(min_occurs=1)


class Extensions(ComplexModel):
    __namespace__ = NAMESPACE

    _type_info = [
        ('FieldCode', StringNonNillable(min_occurs=1)),
        ('FieldCodeDesc', StringNonNillable),
        ('FieldValue', StringNonNillable(min_occurs=1)),
        ]

class ItemAttributes(ComplexModel):
    __namespace__ = NAMESPACE

    _type_info = [
        ('AttributeTypeId', StringMinOcc1),
        ('AttributeTypeDesc', StringMinOcc1),
        ('AttributeHeaderId', StringMinOcc1),
        ('AttributeHeaderDesc', StringMinOcc1),
        ('AttributeCodeId', StringMinOcc1),
        ('AttributeCode', StringMinOcc1),
        ('AttributeCodeDesc', StringMinOcc1),
        ]

class Slotting(ComplexModel):
    __namespace__ = NAMESPACE

    _type_info = [
        ('LocationCode', StringMinOcc1),
        ('SlottingRequired', StringMinOcc1),
        ]

class ItemPromotion(ComplexModel):
    __namespace__ = NAMESPACE

    _type_info = [
        ('OnPromo', StringMinOcc1),
        ('PromoStartWeek', StringMinOcc1),
        ]

class WarehouseAttributes(ComplexModel):
    __namespace__ = NAMESPACE

    _type_info = [
        ('SecureProduct', StringMinOcc1),
        ('Conveyable', StringMinOcc1),
        ('PutawayType', StringMinOcc1),
        ('CrushCode', StringMinOcc1),
        ('VolatilityCode', StringMinOcc1),
        ]

class PerishableAttribute(ComplexModel):
    __namespace__ = NAMESPACE

    _type_info = [
        ('ShelfDays', StringMinOcc1),
        ('ExpireDateReqd', StringMinOcc1),
        ('MinReceivedToExpireDays', StringMinOcc1),
        ('MaxReceivedToExpireDays', StringMinOcc1),
        ]

class ItemBarCode(ComplexModel):
    __namespace__ = NAMESPACE

    _type_info = [
        ('IsPrimary', StringNonNillable),
        ('ItemCode', StringNonNillable),
        ('Barcode', StringNonNillable),
        ('Quantity', StringNonNillable(min_occurs=1)),
        ('ActionType', StringNonNillable),
        ('BarcodeType', StringNonNillable),
        ('Extensions', Extensions.customize(max_occurs='unbounded')),
        ]

class ProductHeirarchy(ComplexModel):
    __namespace__ = NAMESPACE

    _type_info = [
        ('Variant', StringMinOcc1),
        ('Product', StringMinOcc1),
        ('MerchandiseStyle', StringMinOcc1),
        ('Range', StringMinOcc1),
        ('MajorClass', StringMinOcc1),
        ('ClassGroup', StringMinOcc1),
        ('Department', StringMinOcc1),
        ('BusinessGroup', StringMinOcc1),
        ('Section', StringMinOcc1),
        ('Company', StringMinOcc1),
        ]

class ItemPackage(ComplexModel):
    __namespace__ = NAMESPACE

    _type_info = [
        ('PackageType', StringNonNillable),
        ('Description', StringMinOcc1),
        ('Quantity', StringMinOcc1),
        ('UnitWeight', StringMinOcc1),
        ('UnitWidth', StringMinOcc1),
        ('UnitLength', StringMinOcc1),
        ('UnitHeight', StringMinOcc1),
        ('UnitVolume', StringMinOcc1),
        ('WeigthUOM', StringMinOcc1),
        ('DimensionUOM', StringMinOcc1),
        ('VolumeUOM', StringMinOcc1),
        ('IsPrimary', StringMinOcc1),
        ('BusinessPartnerNumber', StringMinOcc1),
        ('Ti', StringMinOcc1),
        ('Hi', StringMinOcc1),
        ]

class ItemBarCodeList(ComplexModel):
    __namespace__ = NAMESPACE

    _type_info = [
        ('ItemBarCode', ItemBarCode.customize(max_occurs='unbounded')),
        ]

class ItemPackageList(ComplexModel):
    __namespace__ = NAMESPACE

    _type_info = [
        ('ItemPackage', ItemPackage.customize(max_occurs='unbounded')),
        ]

class Item(ComplexModel):
    __namespace__ = NAMESPACE

    _type_info = [
        ('ItemCode', StringNonNillable),
        ('IsStyle', StringMinOcc1),
        ('ActionType', StringMinOcc1),
        ('ActivationDate', StringMinOcc1),
        ('TargetExclusive', StringMinOcc1),
        ('OnlineExclusive', StringMinOcc1),
        ('EssentialItem', StringMinOcc1),
        ('LongDescription', StringMinOcc1),
        ('ShortDescription', StringMinOcc1),
        ('PrimaryBarcode', StringMinOcc1),
        ('HazmatCode', StringMinOcc1),
        ('BulkyItem', StringMinOcc1),
        ('ItemWeight', StringMinOcc1),
        ('ItemHeight', StringMinOcc1),
        ('ItemLength', StringMinOcc1),
        ('ItemWidth', StringMinOcc1),
        ('ItemVolume', StringMinOcc1),
        ('WeightUOM', StringMinOcc1),
        ('DimensionUOM', StringMinOcc1),
        ('VolumeUOM', StringMinOcc1),
        ('IsPerishable', StringMinOcc1),
        ('ItemPackageList', ItemPackageList),
        ('ProductHeirarchy', ProductHeirarchy),
        ('ItemBarCodeList', ItemBarCodeList),
        ('PerishableAttribute', PerishableAttribute),
        ('WarehouseAttributes', WarehouseAttributes),
        ('Slotting', Slotting.customize(max_occurs='unbounded')),
        ('ItemPromotion', ItemPromotion),
        ('ItemAttributes', ItemAttributes.customize(max_occurs='unbounded')),
        ('Extensions', Extensions.customize(max_occurs='unbounded')),
        ]

class Message(ComplexModel):
    __namespace__ = NAMESPACE

    _type_info = [
        ('ItemBarCodeList', ItemBarCodeList),
        ('Item', Item.customize(max_occurs='unbounded')),
        ]

class Header(ComplexModel):
    __namespace__ = NAMESPACE

    _type_info = [
        ('Message_Type', StringNonNillable),
        ('Company_ID', StringNonNillable),
        ('Version', StringNonNillable),
        ('Source', StringNonNillable),
        ('Destination', StringNonNillable),
        ('Action_Type', StringNonNillable(values=['read', 'write'])),
        ('Sequence_Number', Integer(nillable=False)),
        ('Batch_ID', StringNonNillable),
        ('Reference_ID', StringNonNillable),
        ('Msg_Locale', StringNonNillable),
        ('Msg_Time_Zone', StringNonNillable),
        ('Internal_Date_Time_Stamp', StringNonNillable(min_occurs=1)),
        ]

class TXml(ComplexModel):
    __namespace__ = NAMESPACE

    _type_info = [
        ('Header', Header.customize(min_occurs=1)),
        ('Message', Message.customize(min_occurs=1)),
        ]

class ReceiveItemBarCode(ComplexModel):
    __namespace__ = NAMESPACE

    _type_info = [
        ('tXml', TXml.customize(min_occurs=1)),
        ]

class ReceiveItemMaster(ComplexModel):
    __namespace__ = NAMESPACE

    _type_info = [
        ('tXml', TXml.customize(min_occurs=1)),
        ]

class ResponseHeader(ComplexModel):
    __namespace__ = NAMESPACE

    _type_info = [
        ('ReturnType', StringNonNillable(min_occurs=1)),
        ('ReturnCode', StringNonNillable(min_occurs=1)),
        ('ReturnMessage', StringNonNillable(min_occurs=1)),
        ]

class ReceiveItemBarCodeOutput(ComplexModel):
    __namespace__ = NAMESPACE

    _type_info = [
        ('receiveItemBarCodeResult', Boolean(min_occurs=1, nillable=False)),
        ('responseHeader', ResponseHeader),
        ]

class ReceiveItemMasterOutput(ComplexModel):
    __namespace__ = NAMESPACE

    _type_info = [
        ('receiveItemMasterResult', Boolean(min_occurs=1, nillable=False)),
        ('responseHeader', ResponseHeader),
    ]
