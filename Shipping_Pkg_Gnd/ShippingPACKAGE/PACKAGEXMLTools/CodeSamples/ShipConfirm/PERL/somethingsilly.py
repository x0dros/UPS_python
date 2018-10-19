#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 18:27:14 2018

@author: x0dros
"""
import xml.etree.ElementTree as ET
import xmlschema
import requests
import AccessRequest as arq  
import ShipConfirmRequest as scr
import ShipAcceptRequest as sar
import base64
#import sys
#sys.path.append('/Users/x0dros/anaconda3/lib/python3.6/site-packages')
#import untangle 

accReq_filen = '/Users/x0dros/Downloads/Shipping_Pkg_Gnd/ShippingPACKAGE/PACKAGEXMLTools/CodeSamples/ShipConfirm/PERL/AccessRequest.xml'
shConfReq_filen = '/Users/x0dros/Downloads/Shipping_Pkg_Gnd/ShippingPACKAGE/PACKAGEXMLTools/CodeSamples/ShipConfirm/PERL/ShipConfirmRequest.xml'
xmldeclaration = '<?xml version="1.0" encoding="UTF-8"?>'
shConfReq_sch_n = '/Users/x0dros/Downloads/Shipping_Pkg_Gnd/ShippingPACKAGE/PACKAGEXMLTools/Schemas/ShipConfirmRequest.xsd'
shAcceptReq_sch_n = '/Users/x0dros/Downloads/Shipping_Pkg_Gnd/ShippingPACKAGE/PACKAGEXMLTools/Schemas/ShipAcceptRequest.xsd'
shConReq_schema = xmlschema.XMLSchema(shConfReq_sch_n)
shAcceptReq_schema = xmlschema.XMLSchema(shAcceptReq_sch_n)
ups_shc_url = "https://wwwcie.ups.com/ups.app/xml/ShipConfirm"
ups_sha_url = "https://wwwcie.ups.com/ups.app/xml/ShipAccept"
                        #Access request:
AccessLicenseNumber= '111111'
UserId= 'somebody'
Password= 'something'
my_ar = arq.AccessRequest()
my_ar.set_AccessLicenseNumber(AccessLicenseNumber)
my_ar.set_UserId(UserId)
my_ar.set_Password(Password)

my_ar.get_AccessLicenseNumber()

outfile_a_n = "accreq_1.xml"
outfile_a = open(outfile_a_n, "w")
my_ar.export(outfile_a, 0, pretty_print=False)
outfile_a.close()


                        #Ship Confirm request:
#Level 6:
code_61 = 'BOX' 
desc_61 = 'BOX'
code_62 = 'LBS'
desc_62 = 'LBS'

my_uomt61 = scr.UnitOfMeasurementType() #Assume Shipment->ShipmentServiceOptions->InternationalForms->product->unit->unitofmeasurement
my_uomt61.set_Code(code_61)
my_uomt61.set_Description(desc_61)

my_uomt62 = scr.UnitOfMeasurementType() #Assume Shipment->ShipmentServiceOptions->InternationalForms->product->ProductWeight->unitofmeasurement
my_uomt62.set_Code(code_62)
my_uomt62.set_Description(desc_62)

my_uomt63 = scr.UnitOfMeasurementType() #For Shipment->Package->PackageWeight->unitofmeasurement: Not really level 6 but it has code!
my_uomt63.set_Code('')


#Level 5:
number_5 = '147'
value_5 = '478'
weight_5 = '10'

my_ut5 = scr.UnitType()
my_ut5.set_Number(number_5)
my_ut5.set_Value(value_5)
my_ut5.set_UnitOfMeasurement(my_uomt61)

my_pwt5 = scr.ProductWeightType()
my_pwt5.set_UnitOfMeasurement(my_uomt62)
my_pwt5.set_Weight(weight_5)
#my_uomt5 = scr.UnitOfMeasurementType()


#Level 4:
mon_val_41 = '100'
mon_val_42 = '50'
mon_val_43 = '200'
mon_val_44 = '50'
desc_41 = 'Misc'  
desc_42 = ['Product 1']
comm_code_4 = '111222AA'
or_ctry_code_4 = 'US'
AccountNumber_4 = '45V8V5'

my_dt4 = scr.DiscountType()
my_dt4.set_MonetaryValue(mon_val_41)

my_fct4 = scr.FreightChargesType()
my_fct4.set_MonetaryValue(mon_val_42)

my_ict4 = scr.InsuranceChargesType()
my_ict4.set_MonetaryValue(mon_val_43)

my_oct4 = scr.OtherChargesType()
my_oct4.set_MonetaryValue(mon_val_44)
my_oct4.set_Description(desc_41)

my_bst4 = scr.BillShipperType()
my_bst4.set_AccountNumber(AccountNumber_4)
#my_bst4.set_CreditCard(CreditCard) #needs def of a class one level below(5)
#my_bst4.set_AlternatePaymentMethod(AlternatePaymentMethod)

my_pt4 = scr.ProductType()
my_pt4.set_Description(desc_42)
my_pt4.set_Unit(my_ut5)
my_pt4.set_CommodityCode(comm_code_4)
my_pt4.set_OriginCountryCode(or_ctry_code_4)
my_pt4.set_ProductWeight(my_pwt5)
#my_pt4.add_Description(self, value): self.Description.append(value)
#my_pt4.insert_Description_at(self, index, value): self.Description.insert(index, value)
#my_pt4.replace_Description_at(self, index, value): self.Description[index] = value
#my_pt4.set_PartNumber(PartNumber)
#my_pt4.set_JointProductionIndicator(ointProductionIndicator)
#my_pt4.set_NetCostDateRange(self, NetCostDateRange): self.NetCostDateRange = NetCostDateRange
#my_pt4.set_PreferenceCriteria(self, PreferenceCriteria): self.PreferenceCriteria = PreferenceCriteria
#my_pt4.set_ProducerInfo(self, ProducerInfo): self.ProducerInfo = ProducerInfo
#my_pt4.set_MarksAndNumbers(self, MarksAndNumbers): self.MarksAndNumbers = MarksAndNumbers
#my_pt4.set_NumberOfPackagesPerCommodity(self, NumberOfPackagesPerCommodity): self.NumberOfPackagesPerCommodity = NumberOfPackagesPerCommodity
#my_pt4.set_VehicleID(self, VehicleID): self.VehicleID = VehicleID
#my_pt4.set_ScheduleB(self, ScheduleB): self.ScheduleB = ScheduleB
#my_pt4.set_ExportType(self, ExportType): self.ExportType = ExportType
#my_pt4.set_SEDTotalValue(self, SEDTotalValue): self.SEDTotalValue = SEDTotalValue
#my_pt4.set_ExcludeFromForm(self, ExcludeFromForm): self.ExcludeFromForm = ExcludeFromForm
#my_pt4.set_ProductCurrencyCode(self, ProductCurrencyCode): self.ProductCurrencyCode = ProductCurrencyCode
#my_pt4.set_PackingListInfo(self, PackingListInfo): self.PackingListInfo = PackingListInfo
#my_pt4.set_EEIInformation(self, EEIInformation): self.EEIInformation = EEIInformation



#Level 3:

UnitOfMeasurement_3 = my_uomt63 
Weight_3 = '60.0'

CodeP_3 = '02'
DescriptionP_3 = 'Customer Supplied'

FormType_3 = ['01']
Product_3 = [my_pt4]
InvoiceNumber_3 = 'asdf123'
InvoiceDate_3 = '20151225' #YYYYMMDD
PurchaseOrderNumber_3 = '999jjj777'
TermsOfShipment_3 = 'CFR'
ReasonForExport_3 = 'Sale'
Comments_3 = 'Your Comments'
DeclarationStatement_3 = 'Your Declaration Statement'
Discount_3 = my_dt4
FreightCharges_3 = my_fct4
InsuranceCharges_3 = my_ict4
OtherCharges_3 = my_oct4
CurrencyCode_3 = 'USD'

Code_3 = '02'
Description_3 = 'Customer Supplied'

AddressLine1_sh = '315 87th St'
AddressLine2_sh = ''
AddressLine3_sh = ''
City_sh = 'Brooklyn' 
StateProvinceCode_sh = 'NY'
PostalCode_sh = '11209'
CountryCode_sh = 'US'

AddressLine1_shto = '78 Federal road'
AddressLine2_shto = ''
AddressLine3_shto = ''
City_shto = 'Hamburg' 
StateProvinceCode_shto = 'CT'
PostalCode_shto = '20354'
CountryCode_shto = 'DE'
ResidentialAddress_shto = ''

AddressLine1_shfr = '2311 York Rd'
AddressLine2_shfr = ''
AddressLine3_shfr = ''
City_shfr = 'City' 
StateProvinceCode_shfr = 'MD'
PostalCode_shfr = '21093'
CountryCode_shfr = 'US'

AddressLine1_soto = '34 Queen St'
AddressLine2_soto = ''
AddressLine3_soto = ''
City_soto = 'Frankfurt' 
StateProvinceCode_soto = ''
PostalCode_soto = '60547'
CountryCode_soto = 'DE'

my_pwt3 = scr.PackageWeightType()
my_pwt3.set_UnitOfMeasurement(UnitOfMeasurement_3)
my_pwt3.set_Weight(Weight_3)

my_ptt3 = scr.PackagingTypeType()
my_ptt3.set_Code(CodeP_3)
my_ptt3.set_Description(DescriptionP_3)

my_pt3 = scr.PrepaidType()
my_pt3.set_BillShipper(my_bst4)

my_sat3 = scr.ShipperAddressType()
my_sat3.set_AddressLine1(AddressLine1_sh)
my_sat3.set_AddressLine2(AddressLine2_sh)
my_sat3.set_AddressLine3(AddressLine3_sh)
my_sat3.set_City(City_sh)
my_sat3.set_StateProvinceCode(StateProvinceCode_sh)
my_sat3.set_PostalCode(PostalCode_sh)
my_sat3.set_CountryCode(CountryCode_sh)

my_stat3 = scr.ShipToAddressType()
my_stat3.set_AddressLine1(AddressLine1_shto)
my_stat3.set_AddressLine2(AddressLine2_shto)
my_stat3.set_AddressLine3(AddressLine3_shto)
my_stat3.set_City(City_shto)
my_stat3.set_StateProvinceCode(StateProvinceCode_shto)
my_stat3.set_PostalCode(PostalCode_shto)
my_stat3.set_CountryCode(CountryCode_shto)
my_stat3.set_ResidentialAddress(ResidentialAddress_shto)

my_sfat3 = scr.ShipFromAddressType()
my_sfat3.set_AddressLine1(AddressLine1_shfr)
my_sfat3.set_AddressLine2(AddressLine2_shfr)
my_sfat3.set_AddressLine3(AddressLine3_shfr)
my_sfat3.set_City(City_shfr)
my_sfat3.set_StateProvinceCode(StateProvinceCode_shfr)
my_sfat3.set_PostalCode(PostalCode_shfr)
my_sfat3.set_CountryCode(CountryCode_shfr)

my_stoat3 = scr.SoldToAddressType()
my_stoat3.set_AddressLine1(AddressLine1_soto)
my_stoat3.set_AddressLine2(AddressLine2_soto)
my_stoat3.set_AddressLine3(AddressLine3_soto)
my_stoat3.set_City(City_soto)
my_stoat3.set_StateProvinceCode(StateProvinceCode_soto)
my_stoat3.set_PostalCode(PostalCode_soto)
my_stoat3.set_CountryCode(CountryCode_soto)

my_ticdt3 = scr.TaxIDCodeDescType()
my_ticdt3.set_Code(Code_3)
my_ticdt3.set_Description(Description_3)

#my_ift3 = scr.InternationalFormsType() #Not necessary!
#my_ift3.set_FormType(FormType_3)
#my_ift3.set_Product(Product_3)
#my_ift3.set_InvoiceNumber(InvoiceNumber_3)
#my_ift3.set_InvoiceDate(InvoiceDate_3)
#my_ift3.set_PurchaseOrderNumber(PurchaseOrderNumber_3)
#my_ift3.set_TermsOfShipment(TermsOfShipment_3)
#my_ift3.set_ReasonForExport(ReasonForExport_3)
#my_ift3.set_Comments(Comments_3)
#my_ift3.set_DeclarationStatement(DeclarationStatement_3)
#my_ift3.set_Discount(Discount_3)
#my_ift3.set_FreightCharges(FreightCharges_3)
#my_ift3.set_InsuranceCharges(InsuranceCharges_3)
#my_ift3.set_OtherCharges(OtherCharges_3)
#my_ift3.set_CurrencyCode(CurrencyCode_3)

#    my_ift3.add_FormType(self, value): self.FormType.append(value)
#    my_ift3.insert_FormType_at(self, index, value): self.FormType.insert(index, value)
#    my_ift3.replace_FormType_at(self, index, value): self.FormType[index] = value
#    my_ift3.set_UserCreatedForm(UserCreatedForm)
#    my_ift3.set_CN22Form(CN22Form)
#    my_ift3.set_UPSPremiumCareForm(UPSPremiumCareForm)
#    my_ift3.set_AdditionalDocumentIndicator(AdditionalDocumentIndicator)
#    my_ift3.set_FormGroupIdName(FormGroupIdName)
#    my_ift3.set_SEDFilingOption(SEDFilingOption)
#    my_ift3.set_Contacts(Contacts)

#    my_ift3.add_Product(self, value): self.Product.append(value)
#    my_ift3.insert_Product_at(self, index, value): self.Product.insert(index, value)
#    my_ift3.replace_Product_at(self, index, value): self.Product[index] = value
#    my_ift3.set_BlanketPeriod(BlanketPeriod)
#    my_ift3.set_ExportDate(ExportDate)
#    my_ift3.set_ExportingCarrier(ExportingCarrier)
#    my_ift3.set_CarrierID(CarrierID)
#    my_ift3.set_InBondCode(InBondCode)
#    my_ift3.set_EntryNumber(EntryNumber)
#    my_ift3.set_PointOfOrigin(PointOfOrigin)
#    my_ift3.set_ModeOfTransport(ModeOfTransport)
#    my_ift3.set_PortOfExport(PortOfExport)
#    my_ift3.set_PortOfUnloading(PortOfUnloading)
#    my_ift3.set_LoadingPier(LoadingPier)
#    my_ift3.set_PartiesToTransaction(PartiesToTransaction)
#    my_ift3.set_RoutedExportTransactionIndicator(RoutedExportTransactionIndicator)
#    my_ift3.set_ContainerizedIndicator(ContainerizedIndicator)
#    my_ift3.set_License(License)
#    my_ift3.set_ECCNNumber(ECCNNumber)
#    my_ift3.set_ShipperMemo(ShipperMemo)
#    my_ift3.set_OverridePaperlessIndicator(OverridePaperlessIndicator)
#    my_ift3.set_MultiCurrencyInvoiceLineTotal(MultiCurrencyInvoiceLineTotal)
#    my_ift3.set_PointOfOriginType(PointOfOriginType)
#    my_ift3.set_EEIFilingOption(EEIFilingOption)
#    my_ift3.set_HazardousMaterialsIndicator(HazardousMaterialsIndicator)


#Level 2:
CodeL_2 = 'GIF'
DescriptionL_2 = 'gif'

CodeLP_2 = 'GIF'
DescriptionLP_2 = 'gif file'

DescriptionP_2 = 'Package Description'
PackagingType_2 = my_ptt3
PackageWeight_2 = my_pwt3

Prepaid_2 = my_pt3

CodeS_2 = '08'
DescriptionS_2 = 'UPS Expedited'

CompanyNameSF_2 = 'Bullwinkle J. Moose'
AttentionNameSF_2 = 'Bull'
TaxIdentificationNumberSF_2 = '1234567877'
TaxIDTypeSF_2 = my_ticdt3
PhoneNumberSF_2 = '1234567890'
AddressSF_2 = my_sfat3

CompanyNameST_2 = 'Happy Dog Pet Supply'
AttentionNameST_2 = 'Marley Brinson'
PhoneNumberST_2 = '97225377171'
AddressST_2 = my_stat3

#InternationalForms = my_ift3 #not necessary 

NegotiatedRatesIndicator_2 = ''
RateChartIndicator_2 = ''

OptionSOT_2 = '01'
CompanyNameSOT_2 = 'Sold To Name'
AttentionNameSOT_2 = 'Sold To Attn Name '
PhoneNumberSOT_2 = '1234567890'
AddressSOT_2 = my_stoat3

NameS_2 = 'Shipper Name'
AttentionNameS_2 = 'Shipper Name'
ShipperNumberS_2 = '45V8V5'
TaxIdentificationNumberS_2 = '1234567877'
PhoneNumberS_2 = '6464602195' 
AddressS_2 = my_sat3

my_lifcdt2 = scr.LabelImageFormatCodeDescriptionType()
my_lifcdt2.set_Code(CodeL_2)
my_lifcdt2.set_Description(DescriptionL_2)

my_lpmcdt2 = scr.LabelPrintMethodCodeDescriptionType()
my_lpmcdt2.set_Code(CodeLP_2)
my_lpmcdt2.set_Description(DescriptionLP_2)

my_pt2 = scr.PackageType()
my_pt2.set_Description(DescriptionP_2)
my_pt2.set_PackagingType(PackagingType_2)
my_pt2.set_PackageWeight(PackageWeight_2)
#my_pt2.set_Dimensions(Dimensions)
#my_pt2.set_DimWeight(DimWeight)
#my_pt2.set_LargePackageIndicator(LargePackageIndicator)
#my_pt2.set_ReferenceNumber(ReferenceNumber)
#my_pt2.add_ReferenceNumber(value)
#my_pt2.insert_ReferenceNumber_at(index, value)
#my_pt2.replace_ReferenceNumber_at(index, value)
#my_pt2.set_AdditionalHandling(AdditionalHandling)
#my_pt2.set_PackageServiceOptions(PackageServiceOptions)
#my_pt2.set_HazMatPackageInformation(HazMatPackageInformation)

my_pit2 = scr.PaymentInformationType()
my_pit2.set_Prepaid(Prepaid_2)
#my_pit2.set_BillThirdParty(BillThirdParty)
#my_pit2.set_FreightCollect(FreightCollect)
#my_pit2.set_ConsigneeBilled(ConsigneeBilled)

my_rit2 = scr.RateInformationType()
my_rit2.set_NegotiatedRatesIndicator(NegotiatedRatesIndicator_2)
my_rit2.set_RateChartIndicator(RateChartIndicator_2)
#my_rit2.set_TPFCNegotiatedRatesIndicator(TPFCNegotiatedRatesIndicator)
#my_rit2.set_UserLevelDiscountIndicator(UserLevelDiscountIndicator)

my_st2 = scr.ServiceType()
my_st2.set_Code(CodeS_2)
my_st2.set_Description(DescriptionS_2)

my_sft2 = scr.ShipFromType()
my_sft2.set_CompanyName(CompanyNameSF_2)
my_sft2.set_AttentionName(AttentionNameSF_2)
my_sft2.set_TaxIdentificationNumber(TaxIdentificationNumberSF_2)
my_sft2.set_TaxIDType(TaxIDTypeSF_2)
my_sft2.set_PhoneNumber(PhoneNumberSF_2)
my_sft2.set_Address(AddressSF_2)
#my_sft2set_FaxNumber(FaxNumber)

my_stt2 = scr.ShipToType()
my_stt2.set_CompanyName(CompanyNameST_2)
my_stt2.set_AttentionName(AttentionNameST_2)
my_stt2.set_PhoneNumber(PhoneNumberST_2)
my_stt2.set_Address(AddressST_2)
#my_stt2.set_TaxIdentificationNumber(TaxIdentificationNumber)
#my_stt2.set_FaxNumber(FaxNumber)
#my_stt2.set_EMailAddress(EMailAddress)
#my_stt2.set_LocationID(LocationID)

my_ssot2 = scr.ShipmentServiceOptionsType()
#my_ssot2.set_InternationalForms(InternationalForms) # Not necessary!


my_spt2 = scr.ShipperType()
my_spt2.set_Name(NameS_2)
my_spt2.set_AttentionName(AttentionNameS_2)
my_spt2.set_ShipperNumber(ShipperNumberS_2)
my_spt2.set_TaxIdentificationNumber(TaxIdentificationNumberS_2)
my_spt2.set_PhoneNumber(PhoneNumberS_2)
my_spt2.set_Address(AddressS_2)
#my_spt2.set_CompanyDisplayableName(CompanyDisplayableName)
#my_spt2.set_FaxNumber(self, FaxNumber)
#my_spt2.set_EMailAddress(EMailAddressS_2)

my_stot2 = scr.SoldToType()
my_stot2.set_Option(OptionSOT_2)
my_stot2.set_CompanyName(CompanyNameSOT_2)
my_stot2.set_AttentionName(AttentionNameSOT_2)
my_stot2.set_PhoneNumber(PhoneNumberSOT_2)
my_stot2.set_Address(AddressSOT_2)
#my_stot2.set_TaxIdentificationNumber(TaxIdentificationNumber)

#Level 1: NB: Start here!
LabelPrintMethodL_1 = my_lpmcdt2
HTTPUserAgentL_1 = 'Mozilla/4.5'
LabelImageFormatL_1 = my_lifcdt2

RequestAction_1 = 'ShipConfirm'
RequestOption_1 = 'nonvalidate' 


DescriptionST_1 = 'BotFactory'
ShipperST_1 = my_spt2
ShipToST_1 = my_stt2
ShipFromST_1 = my_sft2
SoldToST_1 = my_stot2
PaymentInformationST_1 =my_pit2
RateInformationST_1 = my_rit2
ServiceST_1 = my_st2
ShipmentServiceOptionsST_1 = my_ssot2
PackageST_1 = [my_pt2]


 
my_lst1 = scr.LabelSpecificationType()
my_lst1.set_LabelPrintMethod(LabelPrintMethodL_1)
my_lst1.set_HTTPUserAgent(HTTPUserAgentL_1)
my_lst1.set_LabelImageFormat(LabelImageFormatL_1)
#my_lst1.set_Instruction(InstructionL_1)
#my_lst1.set_LabelStockSize(LabelStockSizeL_1)
#my_lst1.add_Instruction(value)
#my_lst1.insert_Instruction_at(value)
#my_lst1.replace_Instruction_at(value)
#my_lst1.set_CharacterSet(CharacterSet)

my_rt1 = scr.RequestType()
my_rt1.set_RequestAction(RequestAction_1)
my_rt1.set_RequestOption(RequestOption_1)
#my_rt1.set_SubVersion(SubVersion)
#my_rt1.set_TransactionReference(TransactionReference)

my_st1 = scr.ShipmentType()
my_st1.set_Description(DescriptionST_1)
my_st1.set_Shipper(ShipperST_1)
my_st1.set_ShipTo(ShipToST_1)
my_st1.set_ShipFrom(ShipFromST_1)
my_st1.set_SoldTo(SoldToST_1)
my_st1.set_PaymentInformation(PaymentInformationST_1)
my_st1.set_RateInformation(RateInformationST_1)
my_st1.set_Service(ServiceST_1)
my_st1.set_ShipmentServiceOptions(ShipmentServiceOptionsST_1)
my_st1.set_Package(PackageST_1)
#my_st1.set_ReturnService(ReturnService)
#my_st1.set_DocumentsOnly(DocumentsOnly)
#my_st1.set_AlternateDeliveryAddress(AlternateDeliveryAddress)
#my_st1.set_ItemizedPaymentInformation(ItemizedPaymentInformation)
#my_st1.set_GoodsNotInFreeCirculationIndicator(GoodsNotInFreeCirculationIndicator)
#my_st1.set_InvoiceLineTotal(InvoiceLineTotal)
#my_st1.set_NumOfPiecesInShipment(NumOfPiecesInShipment)
#my_st1.set_USPSEndorsement(USPSEndorsement)
#my_st1.set_MILabelCN22Indicator(MILabelCN22Indicator)
#my_st1.set_SubClassification(SubClassification)
#my_st1.set_CostCenter(CostCenter)
#my_st1.set_CostCenterBarcodeIndicator(CostCenterBarcodeIndicator)
#my_st1.set_PackageID(PackageID)
#my_st1.set_PackageIDBarcodeIndicator(PackageIDBarcodeIndicator)
#my_st1.set_IrregularIndicator(IrregularIndicator)
#my_st1.set_InvoiceLineTotal(InvoiceLineTotal)
#my_st1.set_NumOfPiecesInShipment(NumOfPiecesInShipment)
#my_st1.set_USPSEndorsement(USPSEndorsement)
#my_st1.set_MILabelCN22Indicator(MILabelCN22Indicator)
#my_st1.set_SubClassification(SubClassification)
#my_st1.set_CostCenter(CostCenter)
#my_st1.set_CostCenterBarcodeIndicator(CostCenterBarcodeIndicator)
#my_st1.set_PackageID(PackageID)
#my_st1.set_PackageIDBarcodeIndicator(PackageIDBarcodeIndicator)
#my_st1.set_IrregularIndicator(IrregularIndicator)
#my_st1.add_Package(value)
#my_st1.insert_Package_at(index, value)
#my_st1.replace_Package_at(index, value)
#my_st1.set_MIDualReturnShipmentKey(MIDualReturnShipmentKey)
#my_st1.set_MIDualReturnShipmentIndicator(MIDualReturnShipmentIndicator)
#my_st1.set_RatingMethodRequestedIndicator(RatingMethodRequestedIndicator)
#my_st1.set_TaxInformationIndicator(TaxInformationIndicator)
#my_st1.set_ShipmentIndicationType(ShipmentIndicationType)
#my_st1.add_ShipmentIndicationType(value)
#my_st1.insert_ShipmentIndicationType_at(index, value)
#my_st1.replace_ShipmentIndicationType_at(index, value)
#my_st1.set_PromotionalDiscountInformation(PromotionalDiscountInformation)

#Level 0:
Request_0 = my_rt1
Shipment_0 = my_st1
LabelSpecification_0 = my_lst1

my_sc = scr.ShipmentConfirmRequest()
my_sc.set_Request(Request_0)
my_sc.set_Shipment(Shipment_0)
my_sc.set_LabelSpecification(LabelSpecification_0)
#my_sc.set_ReceiptSpecification(ReceiptSpecification)

outfile_sc_n = "sconf_req_1.xml"
outfile_sc = open(outfile_sc_n, "w")
my_sc.export(outfile_sc, 0, pretty_print=True)
outfile_sc.close()

#check if it follows the schema:
shConReq_schema.is_valid(outfile_sc_n)

# parse the xml files and save them in two stings

with open(outfile_a_n, 'r') as myfile:
    ar_str =myfile.read().replace('\n', '')
    
with open(outfile_sc_n, 'r') as myfile:
    scr_str =myfile.read().replace('\n', '')
    
# append the two strings 
req_str = ar_str + '\n' + scr_str
print(req_str)

sc_resp = requests.post(url = ups_shc_url, data = req_str) 
#parse the response XML as an element tree
sc_xml_root = ET.fromstring(sc_resp.content)
# extract the response text  
pastebin_url = sc_resp.text 
print("The pastebin URL is:%s"%pastebin_url) 

# Check if the response was a success
for rsps in sc_xml_root.findall('Response'):
    sc_stat_desc = rsps.find('ResponseStatusDescription').text
    
if sc_stat_desc == 'Success':
    print(sc_stat_desc)
    #Get Shipment digest and shipment id numbers from the reponse
    shpmnt_dgst = sc_xml_root.find('ShipmentDigest').text
    shpmnt_idn = sc_xml_root.find('ShipmentIdentificationNumber').text
    #print(shpmnt_dgst)
    #print(shpmnt_idn)
    
# Shipment Accept Request:    
    #Level 1:
    RequestAction1 = '01'  # What does it mean? No clue! 
    my_sarRequest = sar.RequestType()
    my_sarRequest.set_RequestAction(RequestAction1)
    
    #Level 0:
    ShipmentDigest0 = shpmnt_dgst   
    my_sa = sar.ShipmentAcceptRequest()
    my_sa.set_Request(my_sarRequest)
    my_sa.set_ShipmentDigest(ShipmentDigest0)
    
    outfile_sa_n = "shaccept_req.xml"
    outfile_sa = open(outfile_sa_n, "w")
    my_sa.export(outfile_sa, 0, pretty_print=True)
    outfile_sa.close()

    #check if it follows the schema:
    shAcceptReq_schema.is_valid(outfile_sa_n)

    # parse the xml file and save it in a string
    
    with open(outfile_sa_n, 'r') as myfile:
        sar_str =myfile.read().replace('\n', '')
    
    # append the two strings 
    acreq_str = ar_str + '\n' + sar_str
    print(acreq_str)

    sa_resp = requests.post(url = ups_sha_url, data = acreq_str)
    
    sa_xml_root = ET.fromstring(sa_resp.content)
    # extract the response text  
    pastebin_url_sa = sa_resp.text 
    print("The pastebin URL is:%s"%pastebin_url_sa) 

    # Check if the response was a success
    for sa_rsps in sa_xml_root.findall('Response'):
        sa_stat_desc = sa_rsps.find('ResponseStatusDescription').text
        
    if sa_stat_desc == 'Success':
        for node_sa in sa_xml_root.iter('GraphicImage'):
            graphicImage_b64_str = node_sa.text;
            print(graphicImage_b64_str)
                
        rxLabel_b64 = base64.b64decode(graphicImage_b64_str)
        rxLabel_b64_fname = 'UPS_label_py.gif'
        with open(rxLabel_b64_fname, 'wb') as labelf:
                labelf.write(rxLabel_b64)
    else:
        print('\n Something went wrong. ShipAcceptRequest Failed! \n')
            
else:
    print('\n ShipConfirmRequest failed!\n')
                
    
    
    
    


# pack access req and shipment confrimr req and send them to UPS
# 1 Append Sh Conf Req to Acc Req              Done
# 2 Send it therough http to UPS               Done
# 3 Get response (save it in an xml file)      Done
# 4 Get the digest from response               next
# 5 Save it in a file so Ship Accept Req reads it and sends it to UPS in the
# second step                                  next













##rootObject = myadd.parse('people.xml') 
#
#def parseXMLfile(xmlfile_n):
#    tree = ET.parse(xmlfile_n)
#    root = tree.getroot()
#    xmldic = {}
#    
#    # parse over entire xml tree and add each element to a dicttionary
#    for child in root.iter('AddressLine1'):
#        #print(child.tag, child.attrib)
#        print(child.text)
#        xmldic[child.text] = child
#        
#    #print(ET.tostring(tree, pretty_print=True))
#    return xmldic
#        
#def main():
#    
#    xmltags = parseXMLfile(shConfReq_filen)
#    print(xmltags)
#    
#    for x in xmltags:
#        print(x)
#    
#if __name__ == "__main__":
#    main()
#                
#        
#                    


