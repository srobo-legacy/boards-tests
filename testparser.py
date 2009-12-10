import xml.etree.ElementTree as ET

class Test:
    """A class to represent an individual test"""
    text = ""
    name = ""
    passed = False
    
    def __init__(self, xmlnode):
        self.text = xmlnode.text
        self.name = xmlnode.get("name", "")


def parse_file(fname):
    tree = ET.parse(fname)

    root = tree.getroot()
    tests = []

    for e in root:
        if e.tag == "test":
            tests.append( Test(e) )

    return tests

    
