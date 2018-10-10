#!/usr/local/Cellar/perl/5.28.0/bin/perl
no warnings; # turn off warnings

use XML::Compile::Schema;
use XML::LibXML;
use XML::LibXML::Simple;
use LWP::UserAgent;
use HTTP::Request;
use Data::Dumper;

#Configuration
$access = "2D4DAB13C33EF228";
$userid = "x0dros";
$passwd = "Nostos84100";

my $path = "/Users/x0dros/Downloads/Shipping_Pkg_Gnd/ShippingPACKAGE/PACKAGEXMLTools/Schemas";
$endpointurl= "https://wwwcie.ups.com/ups.app/xml/ShipConfirm";
$accessSchemaFile= "$path/AccessRequest.xsd";
$requestSchemaFile= "$path/ShipConfirmRequest.xsd";
$responseSchemaFile= "$path/ShipConfirmResponse.xsd";
$ifSchemaFile = "$path/IF.xsd";

$outputFileName = "XOLTResult.xml";			# response XML
$accReqFileName = "AccessRequest.xml";			# Access Request XML file
$confReqFileName = "ShipConfirmRequest.xml";		# Confirm Request XML file
# Note: if these file don't existmake the python script run this script to create them!

@XML = (); # Array to hold request

my $schema = XML::Compile::Schema->new("$accessSchemaFile");
#print $schema->template('PERL' => 'AccessRequest');
my $doc = XML::LibXML::Document->new('1.0', 'UTF-8');
#print $doc;
my $writer = $schema->compile(WRITER => 'AccessRequest');
my $accessrequest = 
{
   AccessLicenseNumber => "$access" ,
   UserId => "$userid",
   Password => "$passwd"
};

my $xml = $writer->($doc , $accessrequest);
print $doc;
$doc->setDocumentElement($xml);
push(@XML , $doc->toString());

#Save accReq to File
open(fw,">$accReqFileName");
print fw $doc->toString();
close(fw);

$schema = XML::Compile::Schema->new("$requestSchemaFile");
$schema->importDefinitions($ifSchemaFile);
#print $schema->template('PERL' => 'ShipmentConfirmRequest');
$doc = XML::LibXML::Document->new('1.0', 'UTF-8');
$writer = $schema->compile(WRITER => 'ShipmentConfirmRequest');

my $shipconfirmrequest =  
{
	
	Request =>
	{
		RequestAction => 'ShipConfirm',
		RequestOption => 'nonvalidate'
	},
	
	LabelSpecification => 
	{
		LabelPrintMethod =>
		{
			Code => 'GIF',
			Description => 'gif file'
		},
		HTTPUserAgent => 'Mozilla/4.5',
		LabelImageFormat =>
		{
			Code => 'GIF',
			Description => 'gif'
		},
	},
    
    Shipment =>
    {
    	RateInformation =>
    	{
    		NegotiatedRatesIndicator => '',
    		RateChartIndicator => ''
    	},
    	Description => 'BotFactory',
    	Shipper =>
    	{
    		Name => 'Shipper Name',
    		PhoneNumber => '6464602195',
    		ShipperNumber => '45V8V5',
		AttentionName => 'Shipper Name',
		TaxIdentificationNumber => '1234567877',
    		Address =>
    		{
    			AddressLine1 => '315 87th St',
    			City => 'Brooklyn',
    			StateProvinceCode => 'NY',
    			PostalCode => '11209',
    			CountryCode => 'US'
    		},
    	},
    	ShipTo =>
    	{
    		CompanyName => 'Happy Dog Pet Supply',
    		AttentionName => 'Marley Brinson',
    		PhoneNumber => '97225377171',
    		Address =>
    		{
    			AddressLine1 => '78 federal road',
    			City => 'Hamburg',
    			StateProvinceCode => 'CT',
    			PostalCode => '20354',
    			CountryCode => 'DE'
    		},
    	},
    	ShipFrom =>
    	{
    		CompanyName => 'Bullwinkle J. Moose',
    		AttentionName => 'Bull',
    		PhoneNumber => '1234567890',
		TaxIdentificationNumber => '1234567877',
		TaxIDType =>
		{
			Code => '02',
			Description => 'Customer Supplied'
		},
    		Address =>
    		{
    			AddressLine1 => '2311 York Rd',
    			City => 'City',
    			StateProvinceCode => 'MD',
    			PostalCode => '21093',
    			CountryCode => 'US'
    		},
    	},
    	SoldTo =>
	{
		Option => '01',
		AttentionName => 'Sold To Attn Name',
		CompanyName => 'Sold To Name',
		PhoneNumber => '1234567890',
		Address =>
		{
			AddressLine1 => '34 Queen St',
			City => 'Frankfurt',
			PostalCode => '60547',
			CountryCode => 'DE',
		},
	},
    	PaymentInformation =>
    	{
    		Prepaid =>
    		{
    			 BillShipper =>
    			 {
    			 	AccountNumber => '45V8V5'
    			 },
    		},
    	},
    	Service =>
    	{
    		Code => '08',
    		Description => 'UPS Expedited'
    	},
    	ShipmentServiceOptions =>
    	{
    		InternationalForms =>
    		{
    			FormType => '01',
			InvoiceNumber => 'asdf123',
			InvoiceDate => '20151225',
			PurchaseOrderNumber => '999jjj777',
			TermsOfShipment => 'CFR',
			ReasonForExport => 'Sale',
			Comments => 'Your Comments',
			DeclarationStatement => 'Your Declaration Statement',
			CurrencyCode => 'USD',
			Product =>
			{
				Description => 'Product 1',
				CommodityCode => '111222AA',
				OriginCountryCode => 'US',
				Unit =>
				{
					Number => '147',
					Value => '478',
					UnitOfMeasurement =>
					{
						Code => 'BOX',
						Description => 'BOX',
					},
				},
				ProductWeight =>
				{
					Weight => '10',
					UnitOfMeasurement =>
					{
						Code => 'LBS',
						Description => 'LBS',
					},
				},
			},
			Discount =>
			{
				MonetaryValue => '100',
			},
			FreightCharges =>
			{
				MonetaryValue => '50',	
			},
			InsuranceCharges =>
			{
				MonetaryValue => '200',
			},
			OtherCharges =>
			{
				MonetaryValue => '50',
				Description => 'Misc',
			},
    		}
    	},
    	Package =>
    	{
    		PackagingType =>
    		{
    			Code => '02',
    			Description => 'Customer Supplied'
    		},
    		Description => 'Package Description',
    		PackageWeight =>
    		{
    			UnitOfMeasurement => 
    			{
    				Code => ''
    			},
    			Weight => '60.0'
    		},
    	},
    }		
};

$xml = $writer->($doc, $shipconfirmrequest);
$doc->setDocumentElement($xml);
push(@XML , $doc->toString());

#Save confReq to File
open(fw,">$confReqFileName");
print fw $doc->toString();
close(fw);

#Send HTTP Request
my $browser = LWP::UserAgent->new();   
my $req = HTTP::Request->new(POST => $endpointurl);
print "Request: \n@XML";
$req->content("@XML");
#Get HTTP Response Status
print "NB: HTTP resp: "."\n";
my $resp = $browser->request($req);
print "Response: ";
print $resp->status_line() . "\n";
print $resp->content() . "\n";

#Get Response Status
print "NB: XML resp: "."\n";
$parser = XML::LibXML::Simple->new();
my $xmlResp= $parser->XMLin($resp->content());
#print Dumper($xmlResp);
if($xmlResp->{Response}->{ResponseStatusDescription} =~ /success/i)
{
	print "NB: if XML resp success "."\n";
	print $xmlResp->{Response}->{ResponseStatusDescription};
}
else
{
	print "NB: if XML resp failure: "."\n";
	print Dumper($xmlResp);
}
#Save Response To File
open(fw,">$outputFileName");
print fw $resp->content();
close(fw);

$testfilename = "testfile.txt";  
open my $fh, '>', "testfile.txt" or die "Cannot open output.txt: $!";
foreach (@XML)
{
	    print $fh "$_\n"; # Print each entry in our array to the file
}
close $fh;

