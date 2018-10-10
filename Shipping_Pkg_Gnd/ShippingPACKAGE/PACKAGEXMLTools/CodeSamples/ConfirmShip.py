#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 15:15:37 2018

@author: x0dros
"""
from lxml import etree
#from io import StringIO, BytesIO
import xmlschema
from xmlschema.components import (
    XsdElement,
    XsdAnyElement,
    XsdComplexType,
    XsdAtomicBuiltin,
    XsdSimpleType,
    XsdList,
    XsdUnion
)

class GenXML:
    def __init__(self, xsd, elem, enable_choice):
        self.xsd = xmlschema.XMLSchema(xsd)
        self.elem = elem
        self.enable_choice = enable_choice
        self.root = True
        self.vals = {}
    
    # shorten the namespace  
    def short_ns(self, ns):
        for k, v in self.xsd.namespaces.iteritems():
            if k == '':
                continue
            if v == ns:
                return k
        return ''
    # if name is using long namespace,
    # lets replace it with the short one
    def use_short_ns(self, name):
        if name[0] == '{':
            x = name.find('}')
            ns = name[1:x]
            return self.short_ns(ns) + ":" + name[x + 1:]
        return name
    
    # remove the namespace in name
    def remove_ns(self, name):
        if name[0] == '{':
            x = name.find('}')
            return name[x + 1:]
        return name
    
    def print_header(self):
        print("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>")
        
    # put all defined namespaces as a string
    def ns_map_str(self):
        ns_all = ''
        for k, v in self.xsd.namespaces.iteritems():
            if k == '':
                continue
            else:
                ns_all += 'xmlns:' + k + '=\"' + v + '\"' + ' '
        return ns_all
    
    # start a tag with name
    def start_tag(self, name):
        x = '<' + name
        if self.root:
            self.root = False
            x += ' ' + self.ns_map_str()
        x += '>'
        return x
    
    # end a tag with name
    def end_tag(self, name):
        return '</' + name + '>'
    
    # make a sample data for primitive types
    def genval(self, name):
        name = self.remove_ns(name)
        if name in self 
        
    


#Configuration
access = '2D4DAB13C33EF228'
userid = 'x0dros'
passwd = 'Nostos8410'

#Schema files and response file
xsd_path = '/Users/x0dros/Downloads/Shipping_Pkg_Gnd/ShippingPACKAGE/PACKAGEXMLTools/Schemas'
endpointurl= xsd_path + 'https://wwwcie.ups.com/ups.app/xml/ShipConfirm'
accessSchemaFile= xsd_path + '/AccessRequest.xsd'
requestSchemaFile= xsd_path + '/ShipConfirmRequest.xsd'
responseSchemaFile= xsd_path + '/ShipConfirmResponse.xsd'
ifSchemaFile = xsd_path + '/IF.xsd'
outputFileName = 'XOLTResult.xml'

schema = xmlschema.XMLSchema(accessSchemaFile)

"""
@XML = (); # Array to hold request

my $schema = XML::Compile::Schema->new("$accessSchemaFile");
#print $schema->template('PERL' => 'AccessRequest');
my $doc = XML::LibXML::Document->new('1.0', 'UTF-8');
my $writer = $schema->compile(WRITER => 'AccessRequest');
my $accessrequest =
{
   AccessLicenseNumber => "$access" ,
   UserId => "$userid",
   Password => "$passwd"
};

my $xml = $writer->($doc , $accessrequest);
$doc->setDocumentElement($xml);
push(@XML , $doc->toString());
"""
