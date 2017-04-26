from io import BytesIO

from spyne.server.wsgi import WsgiApplication
from lxml import etree

from soapser.soap import app
from soapser import WSDL_URL

wsdl = WsgiApplication(app).doc.wsdl11
wsdl.build_interface_document(WSDL_URL)
b = BytesIO(wsdl.get_interface_document())
parser = etree.XMLParser(remove_blank_text=True)
tree = etree.parse(b, parser=parser)
tree.write('/tmp/soapser.wsdl', pretty_print=True,
           xml_declaration=True)
