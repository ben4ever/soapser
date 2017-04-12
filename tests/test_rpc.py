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
    server.service.Flow_Services_Custom_receiveItemBarCode(obj)
