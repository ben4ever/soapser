from datetime import datetime
from pathlib import PurePath

from lxml import etree
from spyne import ComplexModel

from soapser import OUTPUT_DIR
import soapser.model as mod


def _process_item_bar_code_list(el, message):
    el_ibc_list = etree.SubElement(el, 'ItemBarCodeList')
    for ibc in message.ItemBarCodeList:
        el_ibc = etree.SubElement(el_ibc_list, 'ItemBarCode')
        for ibc_tag, ibc_content in ibc.as_dict().items():
            if ibc_tag == 'Extensions':
                for ext in ibc_content:
                    el_ext = etree.SubElement(el_ibc, 'Extensions')
                    for ext_tag, ext_content in ext.as_dict().items():
                        etree.SubElement(el_ext, ext_tag).text = ext_content
            else:
                etree.SubElement(el_ibc, ibc_tag).text = ibc_content

def _process_item(el, msg):
    for name, cont in msg.as_dict().items():
        if isinstance(cont, str):
            etree.SubElement(el, name).text = cont
        elif isinstance(cont, list):
            if name.endswith('List'):
                if name == 'ItemBarCodeList':
                    child_name = 'ItemBarCode'
                elif name == 'ItemPackageList':
                    child_name = 'ItemPackage'
                else:
                    assert False, 'Unknown element name'
                sub_el = etree.SubElement(el, name)
                for sub_cont in cont:
                    sub2_el = etree.SubElement(sub_el, child_name)
                    _process_item(sub2_el, sub_cont)
            else:
                for sub_cont in cont:
                    sub_el = etree.SubElement(el, name)
                    _process_item(sub_el, sub_cont)
        elif isinstance(cont, ComplexModel):
            sub_el = etree.SubElement(el, name)
            _process_item(sub_el, cont)

def _write_message(root, message):
    el_msg = etree.SubElement(root, 'Message')
    if hasattr(message, 'ItemBarCodeList') and message.ItemBarCodeList:
        _process_item(el_msg, message)
    elif hasattr(message, 'Item') and message.Item:
        _process_item(el_msg, message)

def _write_header(root, header):
    el_header = etree.SubElement(root, 'Header')
    for k, v in header.as_dict().items():
        etree.SubElement(el_header, k).text = v

def _write_common(content, element_name, folder_name):
    root = etree.Element(element_name)
    el_t_xml = etree.SubElement(root, 'tXml')
    t_xml = content.tXml
    _write_header(el_t_xml, t_xml.Header)
    _write_message(el_t_xml, t_xml.Message)
    filename = '{}.txt'.format(datetime.now().strftime('%Y%m%d_%H%M%S_%f'))
    full_path = str(PurePath(OUTPUT_DIR, folder_name, filename))
    etree.ElementTree(root).write(full_path, encoding='UTF-8',
                                  pretty_print=True, xml_declaration=True)

def write_receiveItemBarCode(content):
    _write_common(content, 'ReceiveItemBarCode', 'receive_item_bar_code')


def write_receiveItemMaster(content):
    _write_common(content, 'ReceiveItemMaster', 'receive_item_master')
