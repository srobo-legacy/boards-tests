import xml.etree.ElementTree as ET

def parse_file(fname):
    tree = ET.parse(fname)

    root = tree.getroot()
    tests = []

    for e in root:
        if e.tag == "test":
            tests.append( e.text )

    return tests

    
