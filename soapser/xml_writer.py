from lxml import etree

from soapser import OUTPUT_FILE
import soapser.model as mod


def _write_header(root, headers):
    for header in headers:
        el_header = etree.SubElement(root, 'Header',
                                     Message_Type=header.Message_Type,
                                     Company_ID=header.Company_ID)

def write_xml(receiveItemBarCode):
    root = etree.Element('ReceiveItemBarCode')
    for t_xml in receiveItemBarCode.tXml:
        el_t_xml = etree.SubElement(root, 'tXml')
        _write_header(el_t_xml, t_xml.Header)
    etree.ElementTree(root).write(OUTPUT_FILE, pretty_print=True,
                                  xml_declaration=True)
