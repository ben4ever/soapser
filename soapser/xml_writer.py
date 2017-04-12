from lxml import etree

from soapser import OUTPUT_FILE
import soapser.model as mod


def _write_message(root, message):
    pass

def _write_headers(root, headers):
    for header in headers:
        el_header = etree.SubElement(root, 'Header')
        for k, v in header.as_dict().items():
            etree.SubElement(el_header, k).text = v

def write_xml(receiveItemBarCode):
    root = etree.Element('ReceiveItemBarCode')
    for t_xml in receiveItemBarCode.tXml:
        el_t_xml = etree.SubElement(root, 'tXml')
        _write_headers(el_t_xml, t_xml.Header)
        _write_message(el_t_xml, t_xml.Message[0])
    etree.ElementTree(root).write(OUTPUT_FILE, pretty_print=True,
                                  xml_declaration=True)
