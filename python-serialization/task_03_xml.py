#!/usr/bin/python3
"""not empty"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """not empty"""
    root = ET.Element('data')

    def add_elements(parent, dict_data):
        """not empty"""
        for key, value in dict_data.items():
            child = ET.Element(key)
            if isinstance(value, dict):
                add_elements(child, value)
            else:
                child.text = str(value)
            parent.append(child)
    add_elements(root, dictionary)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """not empty"""
    tree = ET.parse(filename)
    root = tree.getroot()

    def parse_element(element):
        """not empty"""
        parsed_data = {}
        for child in element:
            if len(child) > 0:
                parsed_data[child.tag] = parse_element(child)
            else:
                parsed_data[child.tag] = child.text
        return parsed_data
    return parse_element(root)
