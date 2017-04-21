from spyne import Application
from spyne.protocol.soap import Soap11

from soapser import rpc

app = Application([
                      rpc.receiveItemBarCodeService,
                      rpc.receiveItemMasterService
                  ],
                  tns='Flow/Services/Custom',
                  in_protocol=Soap11(validator='lxml'),
                  out_protocol=Soap11(validator='lxml'))
