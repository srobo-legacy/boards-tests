import xml.etree.ElementTree as ET
import os

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def save_results( board_name, board_number, results ):
    fname = "%s_results.xml" % board_name
    if not os.path.exists(fname):
        tree = ET.ElementTree( ET.fromstring("<results_file></results_file>") )
    else:
        tree = ET.parse( fname )

    root = tree.getroot()
    board = None

    # Find the board
    for e in root:
        if e.attrib.has_key("number") and int(e.attrib["number"]) == board_number:
            board = e
            break

    if board == None:
        "Need to add a new entry into the tree"
        board = ET.Element("board")
        root.append(board)

    board.clear()
    board.set( "number", str(board_number) )

    # Add test results:
    for x in range(0, len(results)):
        result = results[x]

        ent = ET.Element("test")
        ent.set( "number", str(x) )

        if result == None:
            continue
        elif result:
            ent.set( "result", "pass" )
        elif result == False:
            ent.set( "result", "fail" )

        board.append(ent)

    indent(root)
    tree.write( fname )
