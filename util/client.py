from zeep import Client


c = Client('http://localhost:8000?wsdl')

header = c.get_type('ns0:Header')(
            Message_Type='mt',
            Company_ID='ci',
            Version='v',
            Source='s',
            Destination='d',
            Action_Type='read',
            Sequence_Number='1',
            Batch_ID='bi',
            Reference_ID='ri',
            Msg_Locale='ml',
            Msg_Time_Zone='mtz',
            Internal_Date_Time_Stamp='idts')

extensions = c.get_type('ns0:Extensions')(
    FieldCode='fc',
    FieldCodeDesc='fcd',
    FieldValue='fv')

item_bar_code = c.get_type('ns0:ItemBarCode')(
    IsPrimary='ip',
    ItemCode='ic',
    Barcode='b',
    Quantity='q',
    ActionType='at',
    BarcodeType='bt')
item_bar_code.Extensions.append(extensions)
item_bar_code.Extensions.append(extensions)

item_bar_code_list = c.get_type('ns0:ItemBarCodeList')()
item_bar_code_list.ItemBarCode.append(item_bar_code)
item_bar_code_list.ItemBarCode.append(item_bar_code)

message = c.get_type('ns0:Message')(
    ItemBarCodeList=item_bar_code_list)

tXml = c.get_type('ns0:TXml')(Header=header, Message=message)

c.service.receiveItemBarCode(tXml=tXml)
