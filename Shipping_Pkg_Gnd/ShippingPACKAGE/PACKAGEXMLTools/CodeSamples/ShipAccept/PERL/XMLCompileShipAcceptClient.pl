no warnings; # turn off warnings

use XML::Compile::Schema;
use XML::LibXML;
use XML::LibXML::Simple;
use LWP::UserAgent;
use HTTP::Request;
use Data::Dumper;
use Cwd;

#Configuration
$access = "2D4DAB13C33EF228";
$userid = "x0dros";
$passwd = "Nostos84100";

#NB:
my $path = "/Users/x0dros/Downloads/Shipping_Pkg_Gnd/ShippingPACKAGE/PACKAGEXMLTools/Schemas";
my $shipConf_re = "/Users/x0dros/Downloads/Shipping_Pkg_Gnd/ShippingPACKAGE/PACKAGEXMLTools/CodeSamples/ShipConfirm/PERL/XOLTResult.xml";

$endpointurl= "https://wwwcie.ups.com/ups.app/xml/ShipAccept";
$accessSchemaFile= "$path/AccessRequest.xsd";
$requestSchemaFile= "$path/ShipAcceptRequest.xsd";
$responseSchemaFile= "$path/ShipAcceptResponse.xsd";

$outputFileName = "XOLTResult.xml";

$acceptFileName = "ShipAcceptRequest.xml";

#********
@XML = (); # Array to hold request

my $schema = XML::Compile::Schema->new("$accessSchemaFile");	# new schema
#print $schema->template('PERL' => 'AccessRequest');
my $doc = XML::LibXML::Document->new('1.0', 'UTF-8');		# new doc with version and encoding
my $writer = $schema->compile(WRITER => 'AccessRequest');	# a var that is a method call on schema: compile according to the AccessRequest XSD
#******** Define the access request complex var
my $accessrequest = 
{
   AccessLicenseNumber => "$access",
   UserId => "$userid",
   Password => "$passwd"
};
#*********
my $xml = $writer->($doc , $accessrequest);			# new var xml that is what $writer returns: write complex var accessrequest in the $doc or according to $doc?    
$doc->setDocumentElement($xml);					# setDocumentElement? 
push(@XML , $doc->toString());					# push(perl method): Guess puts the doc, which has been turned into string in the XML array 

$schema = XML::Compile::Schema->new("$requestSchemaFile");
#print $schema->template('PERL' => 'ShipmentAcceptRequest');
$doc = XML::LibXML::Document->new('1.0', 'UTF-8');
$writer = $schema->compile(WRITER => 'ShipmentAcceptRequest');

#NB: extract ShipmentDigest from the XML received in ShipConfirm 
$parser_schipConf = XML::LibXML::Simple->new();
my $xmlSC= $parser_schipConf->XMLin($shipConf_re);
my $shipmentDigest_str = $xmlSC->{ShipmentDigest};
#print "the digest: ".$shipmentDigest_str . "\n";

#my $sc_r = XML::LibXML->load_xml(location => $shipConf_re);
##my $shimpentDigest_node = $sc_r ->findnodes('/ShipmentConfirmResponse/ShipmentDigest');
##my $shipmentDigest_str = $shimpentDigest_node ->to_literal();

my $shipacceptrequest =  
{
	Request =>
	{
		RequestAction => '01',
		#RequestOption => '01'
	},
	ShipmentDigest => $shipmentDigest_str
};

$xml = $writer->($doc , $shipacceptrequest);
$doc->setDocumentElement($xml);
push(@XML , $doc->toString());

open(fw,">$acceptFileName");
print fw $doc->toString();
close(fw);

#Send HTTP Request
my $browser = LWP::UserAgent->new();   
my $req = HTTP::Request->new(POST => $endpointurl); 	# new HTTP request 
#print "Request: \n@XML";				
$req->content("@XML");					# XML sent as the content of the HTTP req.
    
#Get HTTP Response Status
my $resp = $browser->request($req);			# get response
print "Response: ";
print $resp->status_line() . "\n";
print $resp->content() . "\n";

#Get Response Status
$parser = XML::LibXML::Simple->new();
my $xmlResp= $parser->XMLin($resp->content());
#print Dumper($xmlResp);
if($xmlResp->{Response}->{ResponseStatusDescription} =~ /success/i)
{
	print $xmlResp->{Response}->{ResponseStatusDescription};
}
else
{
	print Dumper($xmlResp);
}

#Save Response To File
open(fw,">$outputFileName");
print fw $resp->content();
close(fw);

#NB: Extract the base64 code from accept response: 
my $graphicImage_b64 = $xmlResp->{ShipmentResults}->{PackageResults}->{LabelImage}->{GraphicImage};

# Save base64 code in a text file:
my $fname = "UPS_label.txt";
open(my $fh, '>', $fname) or die $!;
print $fh $graphicImage_b64;
close($fh);

#convert base64 to GIF:
my $decoded= MIME::Base64::decode_base64($graphicImage_b64);
open my $fh, '>', 'UPS_label.gif' or die $!;
binmode $fh;
print $fh $decoded;
close $fh;


