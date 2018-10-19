#!/usr/bin/env python

#
# Generated Thu Oct 18 17:44:01 2018 by generateDS.py version 2.29.24.
# Python 3.6.6 |Anaconda custom (64-bit)| (default, Jun 28 2018, 11:07:29)  [GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)]
#
# Command line options:
#   ('-o', 'ShipAcceptRequest.py')
#   ('-s', 'my_sa_req.py')
#   ('--super', 'ShipAcceptRequest')
#
# Command line arguments:
#   /Users/x0dros/Downloads/Shipping_Pkg_Gnd/ShippingPACKAGE/PACKAGEXMLTools/Schemas/ShipAcceptRequest.xsd
#
# Command line:
#   /Users/x0dros/anaconda3/bin/generateDS -o "ShipAcceptRequest.py" -s "my_sa_req.py" --super="ShipAcceptRequest" /Users/x0dros/Downloads/Shipping_Pkg_Gnd/ShippingPACKAGE/PACKAGEXMLTools/Schemas/ShipAcceptRequest.xsd
#
# Current working directory (os.getcwd()):
#   PERL
#

import sys
from lxml import etree as etree_

import ShipAcceptRequest as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = ''

#
# Data representation classes
#


class ShipmentAcceptRequestSub(supermod.ShipmentAcceptRequest):
    def __init__(self, Request=None, ShipmentDigest=None):
        super(ShipmentAcceptRequestSub, self).__init__(Request, ShipmentDigest, )
supermod.ShipmentAcceptRequest.subclass = ShipmentAcceptRequestSub
# end class ShipmentAcceptRequestSub


class RequestTypeSub(supermod.RequestType):
    def __init__(self, RequestAction=None, SubVersion=None, TransactionReference=None):
        super(RequestTypeSub, self).__init__(RequestAction, SubVersion, TransactionReference, )
supermod.RequestType.subclass = RequestTypeSub
# end class RequestTypeSub


class TransactionReferenceTypeSub(supermod.TransactionReferenceType):
    def __init__(self, CustomerContext=None):
        super(TransactionReferenceTypeSub, self).__init__(CustomerContext, )
supermod.TransactionReferenceType.subclass = TransactionReferenceTypeSub
# end class TransactionReferenceTypeSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ShipmentAcceptRequest'
        rootClass = supermod.ShipmentAcceptRequest
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ShipmentAcceptRequest'
        rootClass = supermod.ShipmentAcceptRequest
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    if sys.version_info.major == 2:
        from StringIO import StringIO
    else:
        from io import BytesIO as StringIO
    parser = None
    doc = parsexml_(StringIO(inString), parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ShipmentAcceptRequest'
        rootClass = supermod.ShipmentAcceptRequest
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ShipmentAcceptRequest'
        rootClass = supermod.ShipmentAcceptRequest
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from ShipAcceptRequest import *\n\n')
        sys.stdout.write('import ShipAcceptRequest as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
