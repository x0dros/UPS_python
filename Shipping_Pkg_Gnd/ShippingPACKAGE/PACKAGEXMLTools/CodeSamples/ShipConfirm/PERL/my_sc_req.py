#!/usr/bin/env python

#
# Generated Wed Sep 26 18:57:19 2018 by generateDS.py version 2.29.24.
# Python 3.6.6 |Anaconda custom (64-bit)| (default, Jun 28 2018, 11:07:29)  [GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)]
#
# Command line options:
#   ('-o', 'ShipConfirmRequest.py')
#   ('-s', 'my_sc_req.py')
#   ('--super', 'ShipConfirmRequest')
#
# Command line arguments:
#   /Users/x0dros/Downloads/Shipping_Pkg_Gnd/ShippingPACKAGE/PACKAGEXMLTools/Schemas/ShipConfirmRequest.xsd
#
# Command line:
#   /Users/x0dros/anaconda3/bin/generateDS -o "ShipConfirmRequest.py" -s "my_sc_req.py" --super="ShipConfirmRequest" /Users/x0dros/Downloads/Shipping_Pkg_Gnd/ShippingPACKAGE/PACKAGEXMLTools/Schemas/ShipConfirmRequest.xsd
#
# Current working directory (os.getcwd()):
#   PERL
#

import sys
from lxml import etree as etree_

import ShipConfirmRequest as supermod

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


class ShipmentConfirmRequestSub(supermod.ShipmentConfirmRequest):
    def __init__(self, Request=None, Shipment=None, LabelSpecification=None, ReceiptSpecification=None):
        super(ShipmentConfirmRequestSub, self).__init__(Request, Shipment, LabelSpecification, ReceiptSpecification, )
supermod.ShipmentConfirmRequest.subclass = ShipmentConfirmRequestSub
# end class ShipmentConfirmRequestSub


class RequestTypeSub(supermod.RequestType):
    def __init__(self, RequestAction=None, RequestOption=None, SubVersion=None, TransactionReference=None):
        super(RequestTypeSub, self).__init__(RequestAction, RequestOption, SubVersion, TransactionReference, )
supermod.RequestType.subclass = RequestTypeSub
# end class RequestTypeSub


class TransactionReferenceTypeSub(supermod.TransactionReferenceType):
    def __init__(self, CustomerContext=None):
        super(TransactionReferenceTypeSub, self).__init__(CustomerContext, )
supermod.TransactionReferenceType.subclass = TransactionReferenceTypeSub
# end class TransactionReferenceTypeSub


class ShipmentTypeSub(supermod.ShipmentType):
    def __init__(self, Description=None, ReturnService=None, DocumentsOnly=None, Shipper=None, ShipTo=None, AlternateDeliveryAddress=None, ShipFrom=None, SoldTo=None, PaymentInformation=None, ItemizedPaymentInformation=None, GoodsNotInFreeCirculationIndicator=None, RateInformation=None, MovementReferenceNumber=None, ReferenceNumber=None, Service=None, InvoiceLineTotal=None, NumOfPiecesInShipment=None, USPSEndorsement=None, MILabelCN22Indicator=None, SubClassification=None, CostCenter=None, CostCenterBarcodeIndicator=None, PackageID=None, PackageIDBarcodeIndicator=None, IrregularIndicator=None, ShipmentServiceOptions=None, Package=None, MIDualReturnShipmentKey=None, MIDualReturnShipmentIndicator=None, RatingMethodRequestedIndicator=None, TaxInformationIndicator=None, ShipmentIndicationType=None, PromotionalDiscountInformation=None, DGSignatoryInfo=None):
        super(ShipmentTypeSub, self).__init__(Description, ReturnService, DocumentsOnly, Shipper, ShipTo, AlternateDeliveryAddress, ShipFrom, SoldTo, PaymentInformation, ItemizedPaymentInformation, GoodsNotInFreeCirculationIndicator, RateInformation, MovementReferenceNumber, ReferenceNumber, Service, InvoiceLineTotal, NumOfPiecesInShipment, USPSEndorsement, MILabelCN22Indicator, SubClassification, CostCenter, CostCenterBarcodeIndicator, PackageID, PackageIDBarcodeIndicator, IrregularIndicator, ShipmentServiceOptions, Package, MIDualReturnShipmentKey, MIDualReturnShipmentIndicator, RatingMethodRequestedIndicator, TaxInformationIndicator, ShipmentIndicationType, PromotionalDiscountInformation, DGSignatoryInfo, )
supermod.ShipmentType.subclass = ShipmentTypeSub
# end class ShipmentTypeSub


class PromotionalDiscountInformationTypeSub(supermod.PromotionalDiscountInformationType):
    def __init__(self, PromoCode=None, PromoAliasCode=None):
        super(PromotionalDiscountInformationTypeSub, self).__init__(PromoCode, PromoAliasCode, )
supermod.PromotionalDiscountInformationType.subclass = PromotionalDiscountInformationTypeSub
# end class PromotionalDiscountInformationTypeSub


class ReturnServiceTypeSub(supermod.ReturnServiceType):
    def __init__(self, Code=None):
        super(ReturnServiceTypeSub, self).__init__(Code, )
supermod.ReturnServiceType.subclass = ReturnServiceTypeSub
# end class ReturnServiceTypeSub


class ShipperTypeSub(supermod.ShipperType):
    def __init__(self, Name=None, AttentionName=None, CompanyDisplayableName=None, ShipperNumber=None, TaxIdentificationNumber=None, PhoneNumber=None, FaxNumber=None, EMailAddress=None, Address=None):
        super(ShipperTypeSub, self).__init__(Name, AttentionName, CompanyDisplayableName, ShipperNumber, TaxIdentificationNumber, PhoneNumber, FaxNumber, EMailAddress, Address, )
supermod.ShipperType.subclass = ShipperTypeSub
# end class ShipperTypeSub


class ShipperAddressTypeSub(supermod.ShipperAddressType):
    def __init__(self, AddressLine1=None, AddressLine2=None, AddressLine3=None, City=None, StateProvinceCode=None, PostalCode=None, CountryCode=None):
        super(ShipperAddressTypeSub, self).__init__(AddressLine1, AddressLine2, AddressLine3, City, StateProvinceCode, PostalCode, CountryCode, )
supermod.ShipperAddressType.subclass = ShipperAddressTypeSub
# end class ShipperAddressTypeSub


class ShipToTypeSub(supermod.ShipToType):
    def __init__(self, CompanyName=None, AttentionName=None, TaxIdentificationNumber=None, PhoneNumber=None, FaxNumber=None, EMailAddress=None, Address=None, LocationID=None):
        super(ShipToTypeSub, self).__init__(CompanyName, AttentionName, TaxIdentificationNumber, PhoneNumber, FaxNumber, EMailAddress, Address, LocationID, )
supermod.ShipToType.subclass = ShipToTypeSub
# end class ShipToTypeSub


class ShipToAddressTypeSub(supermod.ShipToAddressType):
    def __init__(self, AddressLine1=None, AddressLine2=None, AddressLine3=None, City=None, StateProvinceCode=None, PostalCode=None, CountryCode=None, ResidentialAddress=None):
        super(ShipToAddressTypeSub, self).__init__(AddressLine1, AddressLine2, AddressLine3, City, StateProvinceCode, PostalCode, CountryCode, ResidentialAddress, )
supermod.ShipToAddressType.subclass = ShipToAddressTypeSub
# end class ShipToAddressTypeSub


class ShipFromTypeSub(supermod.ShipFromType):
    def __init__(self, CompanyName=None, AttentionName=None, TaxIdentificationNumber=None, TaxIDType=None, PhoneNumber=None, FaxNumber=None, Address=None):
        super(ShipFromTypeSub, self).__init__(CompanyName, AttentionName, TaxIdentificationNumber, TaxIDType, PhoneNumber, FaxNumber, Address, )
supermod.ShipFromType.subclass = ShipFromTypeSub
# end class ShipFromTypeSub


class ShipFromAddressTypeSub(supermod.ShipFromAddressType):
    def __init__(self, AddressLine1=None, AddressLine2=None, AddressLine3=None, City=None, StateProvinceCode=None, PostalCode=None, CountryCode=None):
        super(ShipFromAddressTypeSub, self).__init__(AddressLine1, AddressLine2, AddressLine3, City, StateProvinceCode, PostalCode, CountryCode, )
supermod.ShipFromAddressType.subclass = ShipFromAddressTypeSub
# end class ShipFromAddressTypeSub


class SoldToTypeSub(supermod.SoldToType):
    def __init__(self, Option=None, CompanyName=None, AttentionName=None, TaxIdentificationNumber=None, PhoneNumber=None, Address=None):
        super(SoldToTypeSub, self).__init__(Option, CompanyName, AttentionName, TaxIdentificationNumber, PhoneNumber, Address, )
supermod.SoldToType.subclass = SoldToTypeSub
# end class SoldToTypeSub


class SoldToAddressTypeSub(supermod.SoldToAddressType):
    def __init__(self, AddressLine1=None, AddressLine2=None, AddressLine3=None, City=None, StateProvinceCode=None, PostalCode=None, CountryCode=None):
        super(SoldToAddressTypeSub, self).__init__(AddressLine1, AddressLine2, AddressLine3, City, StateProvinceCode, PostalCode, CountryCode, )
supermod.SoldToAddressType.subclass = SoldToAddressTypeSub
# end class SoldToAddressTypeSub


class PaymentInformationTypeSub(supermod.PaymentInformationType):
    def __init__(self, Prepaid=None, BillThirdParty=None, FreightCollect=None, ConsigneeBilled=None):
        super(PaymentInformationTypeSub, self).__init__(Prepaid, BillThirdParty, FreightCollect, ConsigneeBilled, )
supermod.PaymentInformationType.subclass = PaymentInformationTypeSub
# end class PaymentInformationTypeSub


class PrepaidTypeSub(supermod.PrepaidType):
    def __init__(self, BillShipper=None):
        super(PrepaidTypeSub, self).__init__(BillShipper, )
supermod.PrepaidType.subclass = PrepaidTypeSub
# end class PrepaidTypeSub


class BillShipperTypeSub(supermod.BillShipperType):
    def __init__(self, AccountNumber=None, CreditCard=None, AlternatePaymentMethod=None):
        super(BillShipperTypeSub, self).__init__(AccountNumber, CreditCard, AlternatePaymentMethod, )
supermod.BillShipperType.subclass = BillShipperTypeSub
# end class BillShipperTypeSub


class CreditCardTypeSub(supermod.CreditCardType):
    def __init__(self, Type=None, Number=None, ExpirationDate=None, SecurityCode=None, Address=None):
        super(CreditCardTypeSub, self).__init__(Type, Number, ExpirationDate, SecurityCode, Address, )
supermod.CreditCardType.subclass = CreditCardTypeSub
# end class CreditCardTypeSub


class CreditCardAddressTypeSub(supermod.CreditCardAddressType):
    def __init__(self, AddressLine1=None, AddressLine2=None, AddressLine3=None, City=None, StateProvinceCode=None, PostalCode=None, CountryCode=None):
        super(CreditCardAddressTypeSub, self).__init__(AddressLine1, AddressLine2, AddressLine3, City, StateProvinceCode, PostalCode, CountryCode, )
supermod.CreditCardAddressType.subclass = CreditCardAddressTypeSub
# end class CreditCardAddressTypeSub


class BillThirdPartyTypeSub(supermod.BillThirdPartyType):
    def __init__(self, BillThirdPartyShipper=None):
        super(BillThirdPartyTypeSub, self).__init__(BillThirdPartyShipper, )
supermod.BillThirdPartyType.subclass = BillThirdPartyTypeSub
# end class BillThirdPartyTypeSub


class BillThirdPartyShipperTypeSub(supermod.BillThirdPartyShipperType):
    def __init__(self, AccountNumber=None, ThirdParty=None):
        super(BillThirdPartyShipperTypeSub, self).__init__(AccountNumber, ThirdParty, )
supermod.BillThirdPartyShipperType.subclass = BillThirdPartyShipperTypeSub
# end class BillThirdPartyShipperTypeSub


class ThirdPartyTypeSub(supermod.ThirdPartyType):
    def __init__(self, Address=None):
        super(ThirdPartyTypeSub, self).__init__(Address, )
supermod.ThirdPartyType.subclass = ThirdPartyTypeSub
# end class ThirdPartyTypeSub


class ThirdPartyAddressTypeSub(supermod.ThirdPartyAddressType):
    def __init__(self, PostalCode=None, CountryCode=None):
        super(ThirdPartyAddressTypeSub, self).__init__(PostalCode, CountryCode, )
supermod.ThirdPartyAddressType.subclass = ThirdPartyAddressTypeSub
# end class ThirdPartyAddressTypeSub


class FreightCollectTypeSub(supermod.FreightCollectType):
    def __init__(self, BillReceiver=None):
        super(FreightCollectTypeSub, self).__init__(BillReceiver, )
supermod.FreightCollectType.subclass = FreightCollectTypeSub
# end class FreightCollectTypeSub


class BillReceiverTypeSub(supermod.BillReceiverType):
    def __init__(self, AccountNumber=None, Address=None):
        super(BillReceiverTypeSub, self).__init__(AccountNumber, Address, )
supermod.BillReceiverType.subclass = BillReceiverTypeSub
# end class BillReceiverTypeSub


class BillReceiverAddressTypeSub(supermod.BillReceiverAddressType):
    def __init__(self, PostalCode=None):
        super(BillReceiverAddressTypeSub, self).__init__(PostalCode, )
supermod.BillReceiverAddressType.subclass = BillReceiverAddressTypeSub
# end class BillReceiverAddressTypeSub


class ItemizedPaymentInformationTypeSub(supermod.ItemizedPaymentInformationType):
    def __init__(self, ShipmentCharge=None, SplitDutyVATIndicator=None):
        super(ItemizedPaymentInformationTypeSub, self).__init__(ShipmentCharge, SplitDutyVATIndicator, )
supermod.ItemizedPaymentInformationType.subclass = ItemizedPaymentInformationTypeSub
# end class ItemizedPaymentInformationTypeSub


class ShipmentChargeTypeSub(supermod.ShipmentChargeType):
    def __init__(self, Type=None, BillShipper=None, BillReceiver=None, BillThirdParty=None, ConsigneeBilled=None):
        super(ShipmentChargeTypeSub, self).__init__(Type, BillShipper, BillReceiver, BillThirdParty, ConsigneeBilled, )
supermod.ShipmentChargeType.subclass = ShipmentChargeTypeSub
# end class ShipmentChargeTypeSub


class ItemizedBillThirdPartyTypeSub(supermod.ItemizedBillThirdPartyType):
    def __init__(self, BillThirdPartyShipper=None, BillThirdPartyConsignee=None):
        super(ItemizedBillThirdPartyTypeSub, self).__init__(BillThirdPartyShipper, BillThirdPartyConsignee, )
supermod.ItemizedBillThirdPartyType.subclass = ItemizedBillThirdPartyTypeSub
# end class ItemizedBillThirdPartyTypeSub


class BillThirdPartyConsigneeTypeSub(supermod.BillThirdPartyConsigneeType):
    def __init__(self, AccountNumber=None, ThirdParty=None):
        super(BillThirdPartyConsigneeTypeSub, self).__init__(AccountNumber, ThirdParty, )
supermod.BillThirdPartyConsigneeType.subclass = BillThirdPartyConsigneeTypeSub
# end class BillThirdPartyConsigneeTypeSub


class RateInformationTypeSub(supermod.RateInformationType):
    def __init__(self, NegotiatedRatesIndicator=None, RateChartIndicator=None, TPFCNegotiatedRatesIndicator=None, UserLevelDiscountIndicator=None):
        super(RateInformationTypeSub, self).__init__(NegotiatedRatesIndicator, RateChartIndicator, TPFCNegotiatedRatesIndicator, UserLevelDiscountIndicator, )
supermod.RateInformationType.subclass = RateInformationTypeSub
# end class RateInformationTypeSub


class ReferenceNumberTypeSub(supermod.ReferenceNumberType):
    def __init__(self, BarCodeIndicator=None, Code=None, Value=None):
        super(ReferenceNumberTypeSub, self).__init__(BarCodeIndicator, Code, Value, )
supermod.ReferenceNumberType.subclass = ReferenceNumberTypeSub
# end class ReferenceNumberTypeSub


class ServiceTypeSub(supermod.ServiceType):
    def __init__(self, Code=None, Description=None):
        super(ServiceTypeSub, self).__init__(Code, Description, )
supermod.ServiceType.subclass = ServiceTypeSub
# end class ServiceTypeSub


class InvoiceLineTotalTypeSub(supermod.InvoiceLineTotalType):
    def __init__(self, CurrencyCode=None, MonetaryValue=None):
        super(InvoiceLineTotalTypeSub, self).__init__(CurrencyCode, MonetaryValue, )
supermod.InvoiceLineTotalType.subclass = InvoiceLineTotalTypeSub
# end class InvoiceLineTotalTypeSub


class ShipmentServiceOptionsTypeSub(supermod.ShipmentServiceOptionsType):
    def __init__(self, SaturdayDelivery=None, SaturdayPickupIndicator=None, COD=None, AccessPointCOD=None, DeliverToAddresseeOnlyIndicator=None, DirectDeliveryOnlyIndicator=None, Notification=None, LabelDelivery=None, InternationalForms=None, ReturnOfDocumentIndicator=None, DeliveryConfirmation=None, ImportControlIndicator=None, LabelMethod=None, CommercialInvoiceRemovalIndicator=None, UPScarbonneutralIndicator=None, PreAlertNotification=None, ExchangeForwardIndicator=None, HoldForPickupIndicator=None, DropoffAtUPSFacilityIndicator=None, LiftGateForPickUpIndicator=None, LiftGateForDeliveryIndicator=None, SDLShipmentIndicator=None, EPRAReleaseCode=None, RestrictedArticles=None):
        super(ShipmentServiceOptionsTypeSub, self).__init__(SaturdayDelivery, SaturdayPickupIndicator, COD, AccessPointCOD, DeliverToAddresseeOnlyIndicator, DirectDeliveryOnlyIndicator, Notification, LabelDelivery, InternationalForms, ReturnOfDocumentIndicator, DeliveryConfirmation, ImportControlIndicator, LabelMethod, CommercialInvoiceRemovalIndicator, UPScarbonneutralIndicator, PreAlertNotification, ExchangeForwardIndicator, HoldForPickupIndicator, DropoffAtUPSFacilityIndicator, LiftGateForPickUpIndicator, LiftGateForDeliveryIndicator, SDLShipmentIndicator, EPRAReleaseCode, RestrictedArticles, )
supermod.ShipmentServiceOptionsType.subclass = ShipmentServiceOptionsTypeSub
# end class ShipmentServiceOptionsTypeSub


class RestrictedArticlesTypeSub(supermod.RestrictedArticlesType):
    def __init__(self, DiagnosticSpecimensIndicator=None, AlcoholicBeveragesIndicator=None, PerishablesIndicator=None, PlantsIndicator=None, SeedsIndicator=None, SpecialExceptionsIndicator=None, TobaccoIndicator=None):
        super(RestrictedArticlesTypeSub, self).__init__(DiagnosticSpecimensIndicator, AlcoholicBeveragesIndicator, PerishablesIndicator, PlantsIndicator, SeedsIndicator, SpecialExceptionsIndicator, TobaccoIndicator, )
supermod.RestrictedArticlesType.subclass = RestrictedArticlesTypeSub
# end class RestrictedArticlesTypeSub


class PreAlertNotificationTypeSub(supermod.PreAlertNotificationType):
    def __init__(self, EMailMessage=None, VoiceMessage=None, TextMessage=None, Locale=None):
        super(PreAlertNotificationTypeSub, self).__init__(EMailMessage, VoiceMessage, TextMessage, Locale, )
supermod.PreAlertNotificationType.subclass = PreAlertNotificationTypeSub
# end class PreAlertNotificationTypeSub


class PreAlertEMailMessageTypeSub(supermod.PreAlertEMailMessageType):
    def __init__(self, EMailAddress=None, UndeliverableEMailAddress=None):
        super(PreAlertEMailMessageTypeSub, self).__init__(EMailAddress, UndeliverableEMailAddress, )
supermod.PreAlertEMailMessageType.subclass = PreAlertEMailMessageTypeSub
# end class PreAlertEMailMessageTypeSub


class LocaleTypeSub(supermod.LocaleType):
    def __init__(self, Language=None, Dialect=None):
        super(LocaleTypeSub, self).__init__(Language, Dialect, )
supermod.LocaleType.subclass = LocaleTypeSub
# end class LocaleTypeSub


class PreAlertVoiceMessageTypeSub(supermod.PreAlertVoiceMessageType):
    def __init__(self, PhoneNumber=None):
        super(PreAlertVoiceMessageTypeSub, self).__init__(PhoneNumber, )
supermod.PreAlertVoiceMessageType.subclass = PreAlertVoiceMessageTypeSub
# end class PreAlertVoiceMessageTypeSub


class PreAlertTextMessageTypeSub(supermod.PreAlertTextMessageType):
    def __init__(self, PhoneNumber=None):
        super(PreAlertTextMessageTypeSub, self).__init__(PhoneNumber, )
supermod.PreAlertTextMessageType.subclass = PreAlertTextMessageTypeSub
# end class PreAlertTextMessageTypeSub


class ShipmentServiceOptionsCODTypeSub(supermod.ShipmentServiceOptionsCODType):
    def __init__(self, CODCode=None, CODFundsCode=None, CODAmount=None):
        super(ShipmentServiceOptionsCODTypeSub, self).__init__(CODCode, CODFundsCode, CODAmount, )
supermod.ShipmentServiceOptionsCODType.subclass = ShipmentServiceOptionsCODTypeSub
# end class ShipmentServiceOptionsCODTypeSub


class ShipmentServiceOptionsCODAmountTypeSub(supermod.ShipmentServiceOptionsCODAmountType):
    def __init__(self, CurrencyCode=None, MonetaryValue=None):
        super(ShipmentServiceOptionsCODAmountTypeSub, self).__init__(CurrencyCode, MonetaryValue, )
supermod.ShipmentServiceOptionsCODAmountType.subclass = ShipmentServiceOptionsCODAmountTypeSub
# end class ShipmentServiceOptionsCODAmountTypeSub


class ShipmentServiceOptionsAccessPointCODTypeSub(supermod.ShipmentServiceOptionsAccessPointCODType):
    def __init__(self, CurrencyCode=None, MonetaryValue=None):
        super(ShipmentServiceOptionsAccessPointCODTypeSub, self).__init__(CurrencyCode, MonetaryValue, )
supermod.ShipmentServiceOptionsAccessPointCODType.subclass = ShipmentServiceOptionsAccessPointCODTypeSub
# end class ShipmentServiceOptionsAccessPointCODTypeSub


class ShipmentServiceOptionsNotificationTypeSub(supermod.ShipmentServiceOptionsNotificationType):
    def __init__(self, NotificationCode=None, EMailMessage=None, VoiceMessage=None, TextMessage=None, Locale=None):
        super(ShipmentServiceOptionsNotificationTypeSub, self).__init__(NotificationCode, EMailMessage, VoiceMessage, TextMessage, Locale, )
supermod.ShipmentServiceOptionsNotificationType.subclass = ShipmentServiceOptionsNotificationTypeSub
# end class ShipmentServiceOptionsNotificationTypeSub


class ShipmentServiceOptionsNotificationEMailMessageTypeSub(supermod.ShipmentServiceOptionsNotificationEMailMessageType):
    def __init__(self, EMailAddress=None, UndeliverableEMailAddress=None, FromEMailAddress=None, FromName=None, Memo=None, Subject=None, SubjectCode=None):
        super(ShipmentServiceOptionsNotificationEMailMessageTypeSub, self).__init__(EMailAddress, UndeliverableEMailAddress, FromEMailAddress, FromName, Memo, Subject, SubjectCode, )
supermod.ShipmentServiceOptionsNotificationEMailMessageType.subclass = ShipmentServiceOptionsNotificationEMailMessageTypeSub
# end class ShipmentServiceOptionsNotificationEMailMessageTypeSub


class LabelDeliveryTypeSub(supermod.LabelDeliveryType):
    def __init__(self, EMailMessage=None, LabelLinksIndicator=None):
        super(LabelDeliveryTypeSub, self).__init__(EMailMessage, LabelLinksIndicator, )
supermod.LabelDeliveryType.subclass = LabelDeliveryTypeSub
# end class LabelDeliveryTypeSub


class LabelDeliveryEMailMessageTypeSub(supermod.LabelDeliveryEMailMessageType):
    def __init__(self, EMailAddress=None, UndeliverableEMailAddress=None, FromEMailAddress=None, FromName=None, Memo=None, Subject=None, SubjectCode=None):
        super(LabelDeliveryEMailMessageTypeSub, self).__init__(EMailAddress, UndeliverableEMailAddress, FromEMailAddress, FromName, Memo, Subject, SubjectCode, )
supermod.LabelDeliveryEMailMessageType.subclass = LabelDeliveryEMailMessageTypeSub
# end class LabelDeliveryEMailMessageTypeSub


class ShipmentServiceOptionsDeliveryConfirmationTypeSub(supermod.ShipmentServiceOptionsDeliveryConfirmationType):
    def __init__(self, DCISType=None):
        super(ShipmentServiceOptionsDeliveryConfirmationTypeSub, self).__init__(DCISType, )
supermod.ShipmentServiceOptionsDeliveryConfirmationType.subclass = ShipmentServiceOptionsDeliveryConfirmationTypeSub
# end class ShipmentServiceOptionsDeliveryConfirmationTypeSub


class LabelMethodTypeSub(supermod.LabelMethodType):
    def __init__(self, Code=None, Description=None):
        super(LabelMethodTypeSub, self).__init__(Code, Description, )
supermod.LabelMethodType.subclass = LabelMethodTypeSub
# end class LabelMethodTypeSub


class PackageTypeSub(supermod.PackageType):
    def __init__(self, Description=None, PackagingType=None, Dimensions=None, DimWeight=None, PackageWeight=None, LargePackageIndicator=None, ReferenceNumber=None, AdditionalHandling=None, PackageServiceOptions=None, HazMatPackageInformation=None):
        super(PackageTypeSub, self).__init__(Description, PackagingType, Dimensions, DimWeight, PackageWeight, LargePackageIndicator, ReferenceNumber, AdditionalHandling, PackageServiceOptions, HazMatPackageInformation, )
supermod.PackageType.subclass = PackageTypeSub
# end class PackageTypeSub


class PackagingTypeTypeSub(supermod.PackagingTypeType):
    def __init__(self, Code=None, Description=None):
        super(PackagingTypeTypeSub, self).__init__(Code, Description, )
supermod.PackagingTypeType.subclass = PackagingTypeTypeSub
# end class PackagingTypeTypeSub


class DimensionsTypeSub(supermod.DimensionsType):
    def __init__(self, UnitOfMeasurement=None, Length=None, Width=None, Height=None):
        super(DimensionsTypeSub, self).__init__(UnitOfMeasurement, Length, Width, Height, )
supermod.DimensionsType.subclass = DimensionsTypeSub
# end class DimensionsTypeSub


class UnitOfMeasurementTypeSub(supermod.UnitOfMeasurementType):
    def __init__(self, Code=None, Description=None):
        super(UnitOfMeasurementTypeSub, self).__init__(Code, Description, )
supermod.UnitOfMeasurementType.subclass = UnitOfMeasurementTypeSub
# end class UnitOfMeasurementTypeSub


class PackageWeightTypeSub(supermod.PackageWeightType):
    def __init__(self, UnitOfMeasurement=None, Weight=None):
        super(PackageWeightTypeSub, self).__init__(UnitOfMeasurement, Weight, )
supermod.PackageWeightType.subclass = PackageWeightTypeSub
# end class PackageWeightTypeSub


class PackageServiceOptionsTypeSub(supermod.PackageServiceOptionsType):
    def __init__(self, DeliveryConfirmation=None, InsuredValue=None, COD=None, AccessPointCOD=None, VerbalConfirmation=None, ShipperReleaseIndicator=None, Notification=None, HazMat=None, DryIce=None, UPSPremiumCareIndicator=None, ProactiveIndicator=None, PackageIdentifier=None, ClinicalTrialsID=None, RefrigerationIndicator=None):
        super(PackageServiceOptionsTypeSub, self).__init__(DeliveryConfirmation, InsuredValue, COD, AccessPointCOD, VerbalConfirmation, ShipperReleaseIndicator, Notification, HazMat, DryIce, UPSPremiumCareIndicator, ProactiveIndicator, PackageIdentifier, ClinicalTrialsID, RefrigerationIndicator, )
supermod.PackageServiceOptionsType.subclass = PackageServiceOptionsTypeSub
# end class PackageServiceOptionsTypeSub


class PackageServiceOptionsDeliveryConfirmationTypeSub(supermod.PackageServiceOptionsDeliveryConfirmationType):
    def __init__(self, DCISType=None, DCISNumber=None):
        super(PackageServiceOptionsDeliveryConfirmationTypeSub, self).__init__(DCISType, DCISNumber, )
supermod.PackageServiceOptionsDeliveryConfirmationType.subclass = PackageServiceOptionsDeliveryConfirmationTypeSub
# end class PackageServiceOptionsDeliveryConfirmationTypeSub


class InsuredValueTypeSub(supermod.InsuredValueType):
    def __init__(self, Type=None, CurrencyCode=None, MonetaryValue=None):
        super(InsuredValueTypeSub, self).__init__(Type, CurrencyCode, MonetaryValue, )
supermod.InsuredValueType.subclass = InsuredValueTypeSub
# end class InsuredValueTypeSub


class InsuredValueCodeDescriptionTypeSub(supermod.InsuredValueCodeDescriptionType):
    def __init__(self, Code=None, Description=None):
        super(InsuredValueCodeDescriptionTypeSub, self).__init__(Code, Description, )
supermod.InsuredValueCodeDescriptionType.subclass = InsuredValueCodeDescriptionTypeSub
# end class InsuredValueCodeDescriptionTypeSub


class PackageServiceOptionsCODTypeSub(supermod.PackageServiceOptionsCODType):
    def __init__(self, CODCode=None, CODFundsCode=None, CODAmount=None):
        super(PackageServiceOptionsCODTypeSub, self).__init__(CODCode, CODFundsCode, CODAmount, )
supermod.PackageServiceOptionsCODType.subclass = PackageServiceOptionsCODTypeSub
# end class PackageServiceOptionsCODTypeSub


class PackageServiceOptionsCODAmountTypeSub(supermod.PackageServiceOptionsCODAmountType):
    def __init__(self, CurrencyCode=None, MonetaryValue=None):
        super(PackageServiceOptionsCODAmountTypeSub, self).__init__(CurrencyCode, MonetaryValue, )
supermod.PackageServiceOptionsCODAmountType.subclass = PackageServiceOptionsCODAmountTypeSub
# end class PackageServiceOptionsCODAmountTypeSub


class PackageServiceOptionsAccessPointCODTypeSub(supermod.PackageServiceOptionsAccessPointCODType):
    def __init__(self, CurrencyCode=None, MonetaryValue=None):
        super(PackageServiceOptionsAccessPointCODTypeSub, self).__init__(CurrencyCode, MonetaryValue, )
supermod.PackageServiceOptionsAccessPointCODType.subclass = PackageServiceOptionsAccessPointCODTypeSub
# end class PackageServiceOptionsAccessPointCODTypeSub


class VerbalConfirmationTypeSub(supermod.VerbalConfirmationType):
    def __init__(self, ContactInfo=None):
        super(VerbalConfirmationTypeSub, self).__init__(ContactInfo, )
supermod.VerbalConfirmationType.subclass = VerbalConfirmationTypeSub
# end class VerbalConfirmationTypeSub


class VerbalConfirmationContactInfoTypeSub(supermod.VerbalConfirmationContactInfoType):
    def __init__(self, Name=None, PhoneNumber=None):
        super(VerbalConfirmationContactInfoTypeSub, self).__init__(Name, PhoneNumber, )
supermod.VerbalConfirmationContactInfoType.subclass = VerbalConfirmationContactInfoTypeSub
# end class VerbalConfirmationContactInfoTypeSub


class PackageServiceOptionsNotificationTypeSub(supermod.PackageServiceOptionsNotificationType):
    def __init__(self, NotificationCode=None, EMailMessage=None):
        super(PackageServiceOptionsNotificationTypeSub, self).__init__(NotificationCode, EMailMessage, )
supermod.PackageServiceOptionsNotificationType.subclass = PackageServiceOptionsNotificationTypeSub
# end class PackageServiceOptionsNotificationTypeSub


class PackageServiceOptionsNotificationEMailMessageTypeSub(supermod.PackageServiceOptionsNotificationEMailMessageType):
    def __init__(self, EMailAddress=None, UndeliverableEMailAddress=None, FromEMailAddress=None, FromName=None, Memo=None, Subject=None, SubjectCode=None):
        super(PackageServiceOptionsNotificationEMailMessageTypeSub, self).__init__(EMailAddress, UndeliverableEMailAddress, FromEMailAddress, FromName, Memo, Subject, SubjectCode, )
supermod.PackageServiceOptionsNotificationEMailMessageType.subclass = PackageServiceOptionsNotificationEMailMessageTypeSub
# end class PackageServiceOptionsNotificationEMailMessageTypeSub


class LabelSpecificationTypeSub(supermod.LabelSpecificationType):
    def __init__(self, LabelPrintMethod=None, HTTPUserAgent=None, LabelStockSize=None, LabelImageFormat=None, Instruction=None, CharacterSet=None):
        super(LabelSpecificationTypeSub, self).__init__(LabelPrintMethod, HTTPUserAgent, LabelStockSize, LabelImageFormat, Instruction, CharacterSet, )
supermod.LabelSpecificationType.subclass = LabelSpecificationTypeSub
# end class LabelSpecificationTypeSub


class InstructionCodeDescriptionTypeSub(supermod.InstructionCodeDescriptionType):
    def __init__(self, Code=None, Description=None):
        super(InstructionCodeDescriptionTypeSub, self).__init__(Code, Description, )
supermod.InstructionCodeDescriptionType.subclass = InstructionCodeDescriptionTypeSub
# end class InstructionCodeDescriptionTypeSub


class LabelPrintMethodCodeDescriptionTypeSub(supermod.LabelPrintMethodCodeDescriptionType):
    def __init__(self, Code=None, Description=None):
        super(LabelPrintMethodCodeDescriptionTypeSub, self).__init__(Code, Description, )
supermod.LabelPrintMethodCodeDescriptionType.subclass = LabelPrintMethodCodeDescriptionTypeSub
# end class LabelPrintMethodCodeDescriptionTypeSub


class LabelStockSizeTypeSub(supermod.LabelStockSizeType):
    def __init__(self, Height=None, Width=None):
        super(LabelStockSizeTypeSub, self).__init__(Height, Width, )
supermod.LabelStockSizeType.subclass = LabelStockSizeTypeSub
# end class LabelStockSizeTypeSub


class LabelImageFormatCodeDescriptionTypeSub(supermod.LabelImageFormatCodeDescriptionType):
    def __init__(self, Code=None, Description=None):
        super(LabelImageFormatCodeDescriptionTypeSub, self).__init__(Code, Description, )
supermod.LabelImageFormatCodeDescriptionType.subclass = LabelImageFormatCodeDescriptionTypeSub
# end class LabelImageFormatCodeDescriptionTypeSub


class HazMatPackageInformationTypeSub(supermod.HazMatPackageInformationType):
    def __init__(self, AllPackedInOneIndicator=None, OverPackedIndicator=None, QValue=None):
        super(HazMatPackageInformationTypeSub, self).__init__(AllPackedInOneIndicator, OverPackedIndicator, QValue, )
supermod.HazMatPackageInformationType.subclass = HazMatPackageInformationTypeSub
# end class HazMatPackageInformationTypeSub


class HazMatTypeSub(supermod.HazMatType):
    def __init__(self, PackagingTypeQuantity=None, RecordIdentifier1=None, RecordIdentifier2=None, RecordIdentifier3=None, SubRiskClass=None, aDRItemNumber=None, aDRPackingGroupLetter=None, TechnicalName=None, HazardLabelRequired=None, ClassDivisionNumber=None, ReferenceNumber=None, Quantity=None, UOM=None, PackagingType=None, IDNumber=None, ProperShippingName=None, AdditionalDescription=None, PackagingGroupType=None, PackagingInstructionCode=None, EmergencyPhone=None, EmergencyContact=None, ReportableQuantity=None, RegulationSet=None, TransportationMode=None, CommodityRegulatedLevelCode=None, TransportCategory=None, TunnelRestrictionCode=None, ChemicalRecordIdentifier=None, LocalTechnicalName=None, LocalProperShippingName=None):
        super(HazMatTypeSub, self).__init__(PackagingTypeQuantity, RecordIdentifier1, RecordIdentifier2, RecordIdentifier3, SubRiskClass, aDRItemNumber, aDRPackingGroupLetter, TechnicalName, HazardLabelRequired, ClassDivisionNumber, ReferenceNumber, Quantity, UOM, PackagingType, IDNumber, ProperShippingName, AdditionalDescription, PackagingGroupType, PackagingInstructionCode, EmergencyPhone, EmergencyContact, ReportableQuantity, RegulationSet, TransportationMode, CommodityRegulatedLevelCode, TransportCategory, TunnelRestrictionCode, ChemicalRecordIdentifier, LocalTechnicalName, LocalProperShippingName, )
supermod.HazMatType.subclass = HazMatTypeSub
# end class HazMatTypeSub


class DryIceTypeSub(supermod.DryIceType):
    def __init__(self, RegulationSet=None, DryIceWeight=None, MedicalUseIndicator=None):
        super(DryIceTypeSub, self).__init__(RegulationSet, DryIceWeight, MedicalUseIndicator, )
supermod.DryIceType.subclass = DryIceTypeSub
# end class DryIceTypeSub


class DryIceWeightTypeSub(supermod.DryIceWeightType):
    def __init__(self, UnitOfMeasurement=None, Weight=None):
        super(DryIceWeightTypeSub, self).__init__(UnitOfMeasurement, Weight, )
supermod.DryIceWeightType.subclass = DryIceWeightTypeSub
# end class DryIceWeightTypeSub


class ReceiptSpecificationTypeSub(supermod.ReceiptSpecificationType):
    def __init__(self, ImageFormat=None):
        super(ReceiptSpecificationTypeSub, self).__init__(ImageFormat, )
supermod.ReceiptSpecificationType.subclass = ReceiptSpecificationTypeSub
# end class ReceiptSpecificationTypeSub


class ImageFormatCodeDescriptionTypeSub(supermod.ImageFormatCodeDescriptionType):
    def __init__(self, Code=None, Description=None):
        super(ImageFormatCodeDescriptionTypeSub, self).__init__(Code, Description, )
supermod.ImageFormatCodeDescriptionType.subclass = ImageFormatCodeDescriptionTypeSub
# end class ImageFormatCodeDescriptionTypeSub


class AlternateDeliveryAddressTypeSub(supermod.AlternateDeliveryAddressType):
    def __init__(self, Name=None, AttentionName=None, UPSAccessPointID=None, Address=None):
        super(AlternateDeliveryAddressTypeSub, self).__init__(Name, AttentionName, UPSAccessPointID, Address, )
supermod.AlternateDeliveryAddressType.subclass = AlternateDeliveryAddressTypeSub
# end class AlternateDeliveryAddressTypeSub


class IndicationTypeSub(supermod.IndicationType):
    def __init__(self, Code=None, Description=None):
        super(IndicationTypeSub, self).__init__(Code, Description, )
supermod.IndicationType.subclass = IndicationTypeSub
# end class IndicationTypeSub


class ShipmentServiceOptionsNotificationVoiceMessageTypeSub(supermod.ShipmentServiceOptionsNotificationVoiceMessageType):
    def __init__(self, PhoneNumber=None):
        super(ShipmentServiceOptionsNotificationVoiceMessageTypeSub, self).__init__(PhoneNumber, )
supermod.ShipmentServiceOptionsNotificationVoiceMessageType.subclass = ShipmentServiceOptionsNotificationVoiceMessageTypeSub
# end class ShipmentServiceOptionsNotificationVoiceMessageTypeSub


class ShipmentServiceOptionsNotificationTextMessageTypeSub(supermod.ShipmentServiceOptionsNotificationTextMessageType):
    def __init__(self, PhoneNumber=None):
        super(ShipmentServiceOptionsNotificationTextMessageTypeSub, self).__init__(PhoneNumber, )
supermod.ShipmentServiceOptionsNotificationTextMessageType.subclass = ShipmentServiceOptionsNotificationTextMessageTypeSub
# end class ShipmentServiceOptionsNotificationTextMessageTypeSub


class ADLAddressTypeSub(supermod.ADLAddressType):
    def __init__(self, AddressLine1=None, AddressLine2=None, AddressLine3=None, City=None, StateProvinceCode=None, PostalCode=None, CountryCode=None):
        super(ADLAddressTypeSub, self).__init__(AddressLine1, AddressLine2, AddressLine3, City, StateProvinceCode, PostalCode, CountryCode, )
supermod.ADLAddressType.subclass = ADLAddressTypeSub
# end class ADLAddressTypeSub


class TaxIDCodeDescTypeSub(supermod.TaxIDCodeDescType):
    def __init__(self, Code=None, Description=None):
        super(TaxIDCodeDescTypeSub, self).__init__(Code, Description, )
supermod.TaxIDCodeDescType.subclass = TaxIDCodeDescTypeSub
# end class TaxIDCodeDescTypeSub


class DGSignatoryInfoTypeSub(supermod.DGSignatoryInfoType):
    def __init__(self, Name=None, Title=None, Place=None, Date=None, ShipperDeclaration=None):
        super(DGSignatoryInfoTypeSub, self).__init__(Name, Title, Place, Date, ShipperDeclaration, )
supermod.DGSignatoryInfoType.subclass = DGSignatoryInfoTypeSub
# end class DGSignatoryInfoTypeSub


class InternationalFormsTypeSub(supermod.InternationalFormsType):
    def __init__(self, FormType=None, UserCreatedForm=None, CN22Form=None, UPSPremiumCareForm=None, AdditionalDocumentIndicator=None, FormGroupIdName=None, SEDFilingOption=None, Contacts=None, Product=None, InvoiceNumber=None, InvoiceDate=None, PurchaseOrderNumber=None, TermsOfShipment=None, ReasonForExport=None, Comments=None, DeclarationStatement=None, Discount=None, FreightCharges=None, InsuranceCharges=None, OtherCharges=None, CurrencyCode=None, BlanketPeriod=None, ExportDate=None, ExportingCarrier=None, CarrierID=None, InBondCode=None, EntryNumber=None, PointOfOrigin=None, ModeOfTransport=None, PortOfExport=None, PortOfUnloading=None, LoadingPier=None, PartiesToTransaction=None, RoutedExportTransactionIndicator=None, ContainerizedIndicator=None, License=None, ECCNNumber=None, ShipperMemo=None, OverridePaperlessIndicator=None, MultiCurrencyInvoiceLineTotal=None, PointOfOriginType=None, EEIFilingOption=None, HazardousMaterialsIndicator=None):
        super(InternationalFormsTypeSub, self).__init__(FormType, UserCreatedForm, CN22Form, UPSPremiumCareForm, AdditionalDocumentIndicator, FormGroupIdName, SEDFilingOption, Contacts, Product, InvoiceNumber, InvoiceDate, PurchaseOrderNumber, TermsOfShipment, ReasonForExport, Comments, DeclarationStatement, Discount, FreightCharges, InsuranceCharges, OtherCharges, CurrencyCode, BlanketPeriod, ExportDate, ExportingCarrier, CarrierID, InBondCode, EntryNumber, PointOfOrigin, ModeOfTransport, PortOfExport, PortOfUnloading, LoadingPier, PartiesToTransaction, RoutedExportTransactionIndicator, ContainerizedIndicator, License, ECCNNumber, ShipperMemo, OverridePaperlessIndicator, MultiCurrencyInvoiceLineTotal, PointOfOriginType, EEIFilingOption, HazardousMaterialsIndicator, )
supermod.InternationalFormsType.subclass = InternationalFormsTypeSub
# end class InternationalFormsTypeSub


class UPSPremiumCareFormTypeSub(supermod.UPSPremiumCareFormType):
    def __init__(self, ShipmentDate=None, PageSize=None, PrintType=None, NumOfCopies=None, LanguageForUPSPremiumCare=None):
        super(UPSPremiumCareFormTypeSub, self).__init__(ShipmentDate, PageSize, PrintType, NumOfCopies, LanguageForUPSPremiumCare, )
supermod.UPSPremiumCareFormType.subclass = UPSPremiumCareFormTypeSub
# end class UPSPremiumCareFormTypeSub


class LanguageForUPSPremiumCareTypeSub(supermod.LanguageForUPSPremiumCareType):
    def __init__(self, Language=None):
        super(LanguageForUPSPremiumCareTypeSub, self).__init__(Language, )
supermod.LanguageForUPSPremiumCareType.subclass = LanguageForUPSPremiumCareTypeSub
# end class LanguageForUPSPremiumCareTypeSub


class UserCreatedFormTypeSub(supermod.UserCreatedFormType):
    def __init__(self, DocumentID=None):
        super(UserCreatedFormTypeSub, self).__init__(DocumentID, )
supermod.UserCreatedFormType.subclass = UserCreatedFormTypeSub
# end class UserCreatedFormTypeSub


class CN22FormTypeSub(supermod.CN22FormType):
    def __init__(self, LabelSize=None, PrintsPerPage=None, LabelPrintType=None, CN22Type=None, CN22OtherDescription=None, FoldHereText=None, CN22Content=None):
        super(CN22FormTypeSub, self).__init__(LabelSize, PrintsPerPage, LabelPrintType, CN22Type, CN22OtherDescription, FoldHereText, CN22Content, )
supermod.CN22FormType.subclass = CN22FormTypeSub
# end class CN22FormTypeSub


class CN22ContentTypeSub(supermod.CN22ContentType):
    def __init__(self, CN22ContentQuantity=None, CN22ContentDescription=None, CN22ContentWeight=None, CN22ContentTotalValue=None, CN22ContentCurrencyCode=None, CN22ContentCountryOfOrigin=None, CN22ContentTariffNumber=None):
        super(CN22ContentTypeSub, self).__init__(CN22ContentQuantity, CN22ContentDescription, CN22ContentWeight, CN22ContentTotalValue, CN22ContentCurrencyCode, CN22ContentCountryOfOrigin, CN22ContentTariffNumber, )
supermod.CN22ContentType.subclass = CN22ContentTypeSub
# end class CN22ContentTypeSub


class AddressTypeSub(supermod.AddressType):
    def __init__(self, AddressLine1=None, AddressLine2=None, AddressLine3=None, City=None, StateProvinceCode=None, PostalCode=None, CountryCode=None):
        super(AddressTypeSub, self).__init__(AddressLine1, AddressLine2, AddressLine3, City, StateProvinceCode, PostalCode, CountryCode, )
supermod.AddressType.subclass = AddressTypeSub
# end class AddressTypeSub


class BlanketPeriodTypeSub(supermod.BlanketPeriodType):
    def __init__(self, BeginDate=None, EndDate=None):
        super(BlanketPeriodTypeSub, self).__init__(BeginDate, EndDate, )
supermod.BlanketPeriodType.subclass = BlanketPeriodTypeSub
# end class BlanketPeriodTypeSub


class ContactsTypeSub(supermod.ContactsType):
    def __init__(self, ForwardAgent=None, UltimateConsignee=None, IntermediateConsignee=None, Producer=None):
        super(ContactsTypeSub, self).__init__(ForwardAgent, UltimateConsignee, IntermediateConsignee, Producer, )
supermod.ContactsType.subclass = ContactsTypeSub
# end class ContactsTypeSub


class CodeTypeSub(supermod.CodeType):
    def __init__(self, Code=None, Description=None):
        super(CodeTypeSub, self).__init__(Code, Description, )
supermod.CodeType.subclass = CodeTypeSub
# end class CodeTypeSub


class DiscountTypeSub(supermod.DiscountType):
    def __init__(self, MonetaryValue=None):
        super(DiscountTypeSub, self).__init__(MonetaryValue, )
supermod.DiscountType.subclass = DiscountTypeSub
# end class DiscountTypeSub


class ForwardAgentTypeSub(supermod.ForwardAgentType):
    def __init__(self, CompanyName=None, TaxIdentificationNumber=None, Address=None):
        super(ForwardAgentTypeSub, self).__init__(CompanyName, TaxIdentificationNumber, Address, )
supermod.ForwardAgentType.subclass = ForwardAgentTypeSub
# end class ForwardAgentTypeSub


class FreightChargesTypeSub(supermod.FreightChargesType):
    def __init__(self, MonetaryValue=None):
        super(FreightChargesTypeSub, self).__init__(MonetaryValue, )
supermod.FreightChargesType.subclass = FreightChargesTypeSub
# end class FreightChargesTypeSub


class InsuranceChargesTypeSub(supermod.InsuranceChargesType):
    def __init__(self, MonetaryValue=None):
        super(InsuranceChargesTypeSub, self).__init__(MonetaryValue, )
supermod.InsuranceChargesType.subclass = InsuranceChargesTypeSub
# end class InsuranceChargesTypeSub


class IntermediateConsigneeTypeSub(supermod.IntermediateConsigneeType):
    def __init__(self, CompanyName=None, Address=None):
        super(IntermediateConsigneeTypeSub, self).__init__(CompanyName, Address, )
supermod.IntermediateConsigneeType.subclass = IntermediateConsigneeTypeSub
# end class IntermediateConsigneeTypeSub


class LicenseTypeSub(supermod.LicenseType):
    def __init__(self, Number=None, Date=None, ExceptionCode=None):
        super(LicenseTypeSub, self).__init__(Number, Date, ExceptionCode, )
supermod.LicenseType.subclass = LicenseTypeSub
# end class LicenseTypeSub


class NetCostDateRangeTypeSub(supermod.NetCostDateRangeType):
    def __init__(self, BeginDate=None, EndDate=None):
        super(NetCostDateRangeTypeSub, self).__init__(BeginDate, EndDate, )
supermod.NetCostDateRangeType.subclass = NetCostDateRangeTypeSub
# end class NetCostDateRangeTypeSub


class OtherChargesTypeSub(supermod.OtherChargesType):
    def __init__(self, MonetaryValue=None, Description=None):
        super(OtherChargesTypeSub, self).__init__(MonetaryValue, Description, )
supermod.OtherChargesType.subclass = OtherChargesTypeSub
# end class OtherChargesTypeSub


class PhoneTypeSub(supermod.PhoneType):
    def __init__(self, Number=None, Extension=None):
        super(PhoneTypeSub, self).__init__(Number, Extension, )
supermod.PhoneType.subclass = PhoneTypeSub
# end class PhoneTypeSub


class ProductTypeSub(supermod.ProductType):
    def __init__(self, Description=None, Unit=None, CommodityCode=None, PartNumber=None, OriginCountryCode=None, JointProductionIndicator=None, NetCostCode=None, NetCostDateRange=None, PreferenceCriteria=None, ProducerInfo=None, MarksAndNumbers=None, NumberOfPackagesPerCommodity=None, ProductWeight=None, VehicleID=None, ScheduleB=None, ExportType=None, SEDTotalValue=None, ExcludeFromForm=None, ProductCurrencyCode=None, PackingListInfo=None, EEIInformation=None):
        super(ProductTypeSub, self).__init__(Description, Unit, CommodityCode, PartNumber, OriginCountryCode, JointProductionIndicator, NetCostCode, NetCostDateRange, PreferenceCriteria, ProducerInfo, MarksAndNumbers, NumberOfPackagesPerCommodity, ProductWeight, VehicleID, ScheduleB, ExportType, SEDTotalValue, ExcludeFromForm, ProductCurrencyCode, PackingListInfo, EEIInformation, )
supermod.ProductType.subclass = ProductTypeSub
# end class ProductTypeSub


class ExcludeFromFormTypeSub(supermod.ExcludeFromFormType):
    def __init__(self, FormType=None):
        super(ExcludeFromFormTypeSub, self).__init__(FormType, )
supermod.ExcludeFromFormType.subclass = ExcludeFromFormTypeSub
# end class ExcludeFromFormTypeSub


class ProducerTypeSub(supermod.ProducerType):
    def __init__(self, Option=None, CompanyName=None, TaxIdentificationNumber=None, Address=None, AttentionName=None, Phone=None, EMailAddress=None):
        super(ProducerTypeSub, self).__init__(Option, CompanyName, TaxIdentificationNumber, Address, AttentionName, Phone, EMailAddress, )
supermod.ProducerType.subclass = ProducerTypeSub
# end class ProducerTypeSub


class ProductWeightTypeSub(supermod.ProductWeightType):
    def __init__(self, UnitOfMeasurement=None, Weight=None):
        super(ProductWeightTypeSub, self).__init__(UnitOfMeasurement, Weight, )
supermod.ProductWeightType.subclass = ProductWeightTypeSub
# end class ProductWeightTypeSub


class ScheduleBTypeSub(supermod.ScheduleBType):
    def __init__(self, Number=None, Quantity=None, UnitOfMeasurement=None):
        super(ScheduleBTypeSub, self).__init__(Number, Quantity, UnitOfMeasurement, )
supermod.ScheduleBType.subclass = ScheduleBTypeSub
# end class ScheduleBTypeSub


class UltimateConsigneeTypeSub(supermod.UltimateConsigneeType):
    def __init__(self, CompanyName=None, Address=None, UltimateConsigneeType_member=None):
        super(UltimateConsigneeTypeSub, self).__init__(CompanyName, Address, UltimateConsigneeType_member, )
supermod.UltimateConsigneeType.subclass = UltimateConsigneeTypeSub
# end class UltimateConsigneeTypeSub


class UnitTypeSub(supermod.UnitType):
    def __init__(self, Number=None, Value=None, UnitOfMeasurement=None):
        super(UnitTypeSub, self).__init__(Number, Value, UnitOfMeasurement, )
supermod.UnitType.subclass = UnitTypeSub
# end class UnitTypeSub


class PackingListInfoTypeSub(supermod.PackingListInfoType):
    def __init__(self, PackageAssociated=None):
        super(PackingListInfoTypeSub, self).__init__(PackageAssociated, )
supermod.PackingListInfoType.subclass = PackingListInfoTypeSub
# end class PackingListInfoTypeSub


class PackageAssociatedTypeSub(supermod.PackageAssociatedType):
    def __init__(self, PackageNumber=None, ProductAmount=None):
        super(PackageAssociatedTypeSub, self).__init__(PackageNumber, ProductAmount, )
supermod.PackageAssociatedType.subclass = PackageAssociatedTypeSub
# end class PackageAssociatedTypeSub


class EEILicenseTypeSub(supermod.EEILicenseType):
    def __init__(self, Number=None, Code=None, LicenseLineValue=None, ECCNNumber=None):
        super(EEILicenseTypeSub, self).__init__(Number, Code, LicenseLineValue, ECCNNumber, )
supermod.EEILicenseType.subclass = EEILicenseTypeSub
# end class EEILicenseTypeSub


class EEIFilingOptionTypeSub(supermod.EEIFilingOptionType):
    def __init__(self, Code=None, EMailAddress=None, Description=None, UPSFiled=None, ShipperFiled=None):
        super(EEIFilingOptionTypeSub, self).__init__(Code, EMailAddress, Description, UPSFiled, ShipperFiled, )
supermod.EEIFilingOptionType.subclass = EEIFilingOptionTypeSub
# end class EEIFilingOptionTypeSub


class UPSFiledTypeSub(supermod.UPSFiledType):
    def __init__(self, POA=None):
        super(UPSFiledTypeSub, self).__init__(POA, )
supermod.UPSFiledType.subclass = UPSFiledTypeSub
# end class UPSFiledTypeSub


class ShipperFiledTypeSub(supermod.ShipperFiledType):
    def __init__(self, Code=None, Description=None, PreDepartureITNNumber=None, ExemptionLegend=None, EEIShipmentReferenceNumber=None):
        super(ShipperFiledTypeSub, self).__init__(Code, Description, PreDepartureITNNumber, ExemptionLegend, EEIShipmentReferenceNumber, )
supermod.ShipperFiledType.subclass = ShipperFiledTypeSub
# end class ShipperFiledTypeSub


class EEIInformationTypeSub(supermod.EEIInformationType):
    def __init__(self, ExportInformation=None, License=None, DDTCInformation=None):
        super(EEIInformationTypeSub, self).__init__(ExportInformation, License, DDTCInformation, )
supermod.EEIInformationType.subclass = EEIInformationTypeSub
# end class EEIInformationTypeSub


class POATypeSub(supermod.POAType):
    def __init__(self, Code=None, Description=None):
        super(POATypeSub, self).__init__(Code, Description, )
supermod.POAType.subclass = POATypeSub
# end class POATypeSub


class UltimateConsigneeTypeTypeSub(supermod.UltimateConsigneeTypeType):
    def __init__(self, Code=None, Description=None):
        super(UltimateConsigneeTypeTypeSub, self).__init__(Code, Description, )
supermod.UltimateConsigneeTypeType.subclass = UltimateConsigneeTypeTypeSub
# end class UltimateConsigneeTypeTypeSub


class DDTCInformationTypeSub(supermod.DDTCInformationType):
    def __init__(self, ITARExemptionNumber=None, USMLCategoryCode=None, EligiblePartyIndicator=None, RegistrationNumber=None, Quantity=None, UnitOfMeasurement=None, SignificantMilitaryEquipmentIndicator=None, ACMNumber=None):
        super(DDTCInformationTypeSub, self).__init__(ITARExemptionNumber, USMLCategoryCode, EligiblePartyIndicator, RegistrationNumber, Quantity, UnitOfMeasurement, SignificantMilitaryEquipmentIndicator, ACMNumber, )
supermod.DDTCInformationType.subclass = DDTCInformationTypeSub
# end class DDTCInformationTypeSub


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
        rootTag = 'ShipmentConfirmRequest'
        rootClass = supermod.ShipmentConfirmRequest
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
        rootTag = 'ShipmentConfirmRequest'
        rootClass = supermod.ShipmentConfirmRequest
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
        rootTag = 'ShipmentConfirmRequest'
        rootClass = supermod.ShipmentConfirmRequest
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
        rootTag = 'ShipmentConfirmRequest'
        rootClass = supermod.ShipmentConfirmRequest
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from ShipConfirmRequest import *\n\n')
        sys.stdout.write('import ShipConfirmRequest as model_\n\n')
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
