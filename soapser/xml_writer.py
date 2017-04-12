from lxml import etree

from soapser import OUTPUT_FILE
import soapser.model as mod


def _write_message(root, message):
    el_msg = etree.SubElement(root, 'Message')
    el_ibc_list = etree.SubElement(el_msg, 'ItemBarCodeList')
    for ibc in message.ItemBarCodeList:
        el_ibc = etree.SubElement(el_ibc_list, 'ItemBarCode')
        for ibc_tag, ibc_content in ibc.as_dict().items():
            if isinstance(ibc_content, list):
                for ext in ibc_content:
                    el_ext = etree.SubElement(el_ibc, 'Extensions')
                    for ext_tag, ext_content in ext.as_dict().items():
                        etree.SubElement(el_ext, ext_tag).text = ext_content
            else:
                etree.SubElement(el_ibc, ibc_tag).text = ibc_content

def _write_header(root, header):
    el_header = etree.SubElement(root, 'Header')
    for k, v in header.as_dict().items():
        etree.SubElement(el_header, k).text = v

def write_xml(receiveItemBarCode):
    root = etree.Element('ReceiveItemBarCode')
    for t_xml in receiveItemBarCode.tXml:
        el_t_xml = etree.SubElement(root, 'tXml')
        _write_header(el_t_xml, t_xml.Header[0])
        _write_message(el_t_xml, t_xml.Message[0])
    etree.ElementTree(root).write(OUTPUT_FILE, encoding='UTF-8',
                                  pretty_print=True, xml_declaration=True)
