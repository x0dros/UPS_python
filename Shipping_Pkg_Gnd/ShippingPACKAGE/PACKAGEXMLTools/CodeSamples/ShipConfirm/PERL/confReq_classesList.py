#
# Data representation classes
#

__all__ = [
    "ADLAddressType",                   
    "AddressType",                                          #???
    "AlternateDeliveryAddressType",
    "BillReceiverAddressType",
    "BillReceiverType",
    "BillShipperType",                                      #LEVEL4
    "BillThirdPartyConsigneeType",
    "BillThirdPartyShipperType",
    "BillThirdPartyType",
    "BlanketPeriodType",
    "CN22ContentType",
    "CN22FormType",
    "CodeType",
    "ContactsType",
    "CreditCardAddressType",
    "CreditCardType",
    "DDTCInformationType",
    "DGSignatoryInfoType",
    "DimensionsType",
    "DiscountType",                                         #LEVEL4
    "DryIceType",
    "DryIceWeightType",
    "EEIFilingOptionType",
    "EEIInformationType",
    "EEILicenseType",
    "ExcludeFromFormType",
    "ForwardAgentType",
    "FreightChargesType",                                   #LEVEL4
    "FreightCollectType",
    "HazMatPackageInformationType",
    "HazMatType",
    "ImageFormatCodeDescriptionType",
    "IndicationType",
    "InstructionCodeDescriptionType",
    "InsuranceChargesType",                                 #LEVEL4
    "InsuredValueCodeDescriptionType",
    "InsuredValueType",
    "IntermediateConsigneeType",
    "InternationalFormsType",                               #LEVEL3
    "InvoiceLineTotalType",
    "ItemizedBillThirdPartyType",
    "ItemizedPaymentInformationType",
    "LabelDeliveryEMailMessageType",
    "LabelDeliveryType",
    "LabelImageFormatCodeDescriptionType",                  #LEVEL2
    "LabelMethodType",
    "LabelPrintMethodCodeDescriptionType",                  #LEVEL2
    "LabelSpecificationType",                               #LEVEL1
    "LabelStockSizeType",
    "LanguageForUPSPremiumCareType",
    "LicenseType",
    "LocaleType",
    "NetCostDateRangeType",
    "OtherChargesType",                                     #LEVEL4
    "POAType",
    "PackageAssociatedType",
    "PackageServiceOptionsAccessPointCODType",
    "PackageServiceOptionsCODAmountType",
    "PackageServiceOptionsCODType",
    "PackageServiceOptionsDeliveryConfirmationType",
    "PackageServiceOptionsNotificationEMailMessageType",
    "PackageServiceOptionsNotificationType",
    "PackageServiceOptionsType",
    "PackageType",                                          #LEVEL2
    "PackageWeightType",                                    #LEVEL3
    "PackagingTypeType",                                    #LEVEL3
    "PackingListInfoType",
    "PaymentInformationType",                               #LEVEL2
    "PhoneType",
    "PreAlertEMailMessageType",
    "PreAlertNotificationType",
    "PreAlertTextMessageType",
    "PreAlertVoiceMessageType",
    "PrepaidType",                                          #LEVEL3
    "ProducerType",                                         
    "ProductType",                                          #LEVEL4
    "ProductWeightType",                                    #LEVEL5
    "PromotionalDiscountInformationType",
    "RateInformationType",                                  #LEVEL2
    "ReceiptSpecificationType",
    "ReferenceNumberType",
    "RequestType",                                          #LEVEL1
    "RestrictedArticlesType",
    "ReturnServiceType",
    "ScheduleBType",
    "ServiceType",                                          #LEVEL2
    "ShipFromAddressType",                                  #LEVEL3
    "ShipFromType",                                         #LEVEL2
    "ShipToAddressType",                                    #LEVEL3
    "ShipToType",                                           #LEVEL2
    "ShipmentChargeType",
    "ShipmentConfirmRequest",                               #LEVEL0
    "ShipmentServiceOptionsAccessPointCODType",             
    "ShipmentServiceOptionsCODAmountType",
    "ShipmentServiceOptionsCODType",
    "ShipmentServiceOptionsDeliveryConfirmationType",
    "ShipmentServiceOptionsNotificationEMailMessageType",
    "ShipmentServiceOptionsNotificationTextMessageType",
    "ShipmentServiceOptionsNotificationType",
    "ShipmentServiceOptionsNotificationVoiceMessageType",
    "ShipmentServiceOptionsType",                           #LEVEL2
    "ShipmentType",                                         #LEVEL1
    "ShipperAddressType",                                   #LEVEL3
    "ShipperFiledType",                                     #???
    "ShipperType",                                          #LEVEL2
    "SoldToAddressType",                                    #LEVEL3
    "SoldToType",                                           #LEVEL2
    "TaxIDCodeDescType",                                    #LEVEL3
    "ThirdPartyAddressType",
    "ThirdPartyType",
    "TransactionReferenceType",
    "UPSFiledType",
    "UPSPremiumCareFormType",
    "UltimateConsigneeType",
    "UltimateConsigneeTypeType",
    "UnitOfMeasurementType",                                #LEVEL4
    "UnitType",                                             #LEVEL5
    "UserCreatedFormType",
    "VerbalConfirmationContactInfoType",
    "VerbalConfirmationType"
]



class ShipmentConfirmRequestSub(supermod.ShipmentConfirmRequest):
# end class ShipmentConfirmRequestSub LEVEL0

class RequestTypeSub(supermod.RequestType):
# end class RequestTypeSub LEVEL1

class TransactionReferenceTypeSub(supermod.TransactionReferenceType):
# end class TransactionReferenceTypeSub

class ShipmentTypeSub(supermod.ShipmentType):
# end class ShipmentTypeSub L1
(Description=None, ReturnService=None, DocumentsOnly=None, Shipper=None, ShipTo=None,
 AlternateDeliveryAddress=None, ShipFrom=None, SoldTo=None, PaymentInformation=None,
 ItemizedPaymentInformation=None, GoodsNotInFreeCirculationIndicator=None, RateInformation=None, 
 MovementReferenceNumber=None, ReferenceNumber=None, Service=None, InvoiceLineTotal=None,
 NumOfPiecesInShipment=None, USPSEndorsement=None, MILabelCN22Indicator=None, SubClassification=None, 
 CostCenter=None, CostCenterBarcodeIndicator=None, PackageID=None, PackageIDBarcodeIndicator=None, 
 IrregularIndicator=None, ShipmentServiceOptions=None, Package=None, MIDualReturnShipmentKey=None, 
 MIDualReturnShipmentIndicator=None, RatingMethodRequestedIndicator=None, TaxInformationIndicator=None, 
 ShipmentIndicationType=None, PromotionalDiscountInformation=None, DGSignatoryInfo=None):
        
    
    
    
class PromotionalDiscountInformationTypeSub(supermod.PromotionalDiscountInformationType):
# end class PromotionalDiscountInformationTypeSub

class ReturnServiceTypeSub(supermod.ReturnServiceType):
# end class ReturnServiceTypeSub

class ShipperTypeSub(supermod.ShipperType):
# end class ShipperTypeSub

class ShipperAddressTypeSub(supermod.ShipperAddressType):
# end class ShipperAddressTypeSub

class ShipToTypeSub(supermod.ShipToType):
# end class ShipToTypeSub

class ShipToAddressTypeSub(supermod.ShipToAddressType):
# end class ShipToAddressTypeSub

class ShipFromTypeSub(supermod.ShipFromType):
# end class ShipFromTypeSub

class ShipFromAddressTypeSub(supermod.ShipFromAddressType):
# end class ShipFromAddressTypeSub

class SoldToTypeSub(supermod.SoldToType):
# end class SoldToTypeSub

class SoldToAddressTypeSub(supermod.SoldToAddressType):
# end class SoldToAddressTypeSub

class PaymentInformationTypeSub(supermod.PaymentInformationType):
# end class PaymentInformationTypeSub

class PrepaidTypeSub(supermod.PrepaidType):
# end class PrepaidTypeSub

class BillShipperTypeSub(supermod.BillShipperType):
# end class BillShipperTypeSub

class CreditCardTypeSub(supermod.CreditCardType):
# end class CreditCardTypeSub

class CreditCardAddressTypeSub(supermod.CreditCardAddressType):
# end class CreditCardAddressTypeSub

class BillThirdPartyTypeSub(supermod.BillThirdPartyType):
# end class BillThirdPartyTypeSub

class BillThirdPartyShipperTypeSub(supermod.BillThirdPartyShipperType):
# end class BillThirdPartyShipperTypeSub

class ThirdPartyTypeSub(supermod.ThirdPartyType):
# end class ThirdPartyTypeSub

class ThirdPartyAddressTypeSub(supermod.ThirdPartyAddressType):
# end class ThirdPartyAddressTypeSub

class FreightCollectTypeSub(supermod.FreightCollectType):
# end class FreightCollectTypeSub

class BillReceiverTypeSub(supermod.BillReceiverType):
# end class BillReceiverTypeSub

class BillReceiverAddressTypeSub(supermod.BillReceiverAddressType):
# end class BillReceiverAddressTypeSub

class ItemizedPaymentInformationTypeSub(supermod.ItemizedPaymentInformationType):
# end class ItemizedPaymentInformationTypeSub

class ShipmentChargeTypeSub(supermod.ShipmentChargeType):
# end class ShipmentChargeTypeSub

class ItemizedBillThirdPartyTypeSub(supermod.ItemizedBillThirdPartyType):
# end class ItemizedBillThirdPartyTypeSub

class BillThirdPartyConsigneeTypeSub(supermod.BillThirdPartyConsigneeType):
# end class BillThirdPartyConsigneeTypeSub

class RateInformationTypeSub(supermod.RateInformationType):
# end class RateInformationTypeSub

class ReferenceNumberTypeSub(supermod.ReferenceNumberType):
# end class ReferenceNumberTypeSub

class ServiceTypeSub(supermod.ServiceType):
# end class ServiceTypeSub

class InvoiceLineTotalTypeSub(supermod.InvoiceLineTotalType):
# end class InvoiceLineTotalTypeSub

class ShipmentServiceOptionsTypeSub(supermod.ShipmentServiceOptionsType):
# end class ShipmentServiceOptionsTypeSub

class RestrictedArticlesTypeSub(supermod.RestrictedArticlesType):
# end class RestrictedArticlesTypeSub

class PreAlertNotificationTypeSub(supermod.PreAlertNotificationType):
# end class PreAlertNotificationTypeSub

class PreAlertEMailMessageTypeSub(supermod.PreAlertEMailMessageType):
# end class PreAlertEMailMessageTypeSub

class LocaleTypeSub(supermod.LocaleType):
# end class LocaleTypeSub

class PreAlertVoiceMessageTypeSub(supermod.PreAlertVoiceMessageType):
# end class PreAlertVoiceMessageTypeSub

class PreAlertTextMessageTypeSub(supermod.PreAlertTextMessageType):
# end class PreAlertTextMessageTypeSub

class ShipmentServiceOptionsCODTypeSub(supermod.ShipmentServiceOptionsCODType):
# end class ShipmentServiceOptionsCODTypeSub

class ShipmentServiceOptionsCODAmountTypeSub(supermod.ShipmentServiceOptionsCODAmountType):
# end class ShipmentServiceOptionsCODAmountTypeSub

class ShipmentServiceOptionsAccessPointCODTypeSub(supermod.ShipmentServiceOptionsAccessPointCODType):
# end class ShipmentServiceOptionsAccessPointCODTypeSub

class ShipmentServiceOptionsNotificationTypeSub(supermod.ShipmentServiceOptionsNotificationType):
# end class ShipmentServiceOptionsNotificationTypeSub

class ShipmentServiceOptionsNotificationEMailMessageTypeSub(supermod.ShipmentServiceOptionsNotificationEMailMessageType):
# end class ShipmentServiceOptionsNotificationEMailMessageTypeSub

class LabelDeliveryTypeSub(supermod.LabelDeliveryType):
# end class LabelDeliveryTypeSub


class LabelDeliveryEMailMessageTypeSub(supermod.LabelDeliveryEMailMessageType):
# end class LabelDeliveryEMailMessageTypeSub

class ShipmentServiceOptionsDeliveryConfirmationTypeSub(supermod.ShipmentServiceOptionsDeliveryConfirmationType):
# end class ShipmentServiceOptionsDeliveryConfirmationTypeSub

class LabelMethodTypeSub(supermod.LabelMethodType):
# end class LabelMethodTypeSub
    
class PackageTypeSub(supermod.PackageType):
# end class PackageTypeSub

class PackagingTypeTypeSub(supermod.PackagingTypeType):
# end class PackagingTypeTypeSub

class DimensionsTypeSub(supermod.DimensionsType):
# end class DimensionsTypeSub

class UnitOfMeasurementTypeSub(supermod.UnitOfMeasurementType):
# end class UnitOfMeasurementTypeSub

class PackageWeightTypeSub(supermod.PackageWeightType):
# end class PackageWeightTypeSub

class PackageServiceOptionsTypeSub(supermod.PackageServiceOptionsType):
# end class PackageServiceOptionsTypeSub

class PackageServiceOptionsDeliveryConfirmationTypeSub(supermod.PackageServiceOptionsDeliveryConfirmationType):
# end class PackageServiceOptionsDeliveryConfirmationTypeSub

class InsuredValueTypeSub(supermod.InsuredValueType):
# end class InsuredValueTypeSub

class InsuredValueCodeDescriptionTypeSub(supermod.InsuredValueCodeDescriptionType):
# end class InsuredValueCodeDescriptionTypeSub

class PackageServiceOptionsCODTypeSub(supermod.PackageServiceOptionsCODType):
# end class PackageServiceOptionsCODTypeSub

class PackageServiceOptionsCODAmountTypeSub(supermod.PackageServiceOptionsCODAmountType):
# end class PackageServiceOptionsCODAmountTypeSub

class PackageServiceOptionsAccessPointCODTypeSub(supermod.PackageServiceOptionsAccessPointCODType):
# end class PackageServiceOptionsAccessPointCODTypeSub

class VerbalConfirmationTypeSub(supermod.VerbalConfirmationType):
# end class VerbalConfirmationTypeSub

class VerbalConfirmationContactInfoTypeSub(supermod.VerbalConfirmationContactInfoType):
# end class VerbalConfirmationContactInfoTypeSub

class PackageServiceOptionsNotificationTypeSub(supermod.PackageServiceOptionsNotificationType):
# end class PackageServiceOptionsNotificationTypeSub

class PackageServiceOptionsNotificationEMailMessageTypeSub(supermod.PackageServiceOptionsNotificationEMailMessageType):
# end class PackageServiceOptionsNotificationEMailMessageTypeSub

class LabelSpecificationTypeSub(supermod.LabelSpecificationType):
# end class LabelSpecificationTypeSub LEVEL1

class InstructionCodeDescriptionTypeSub(supermod.InstructionCodeDescriptionType):
# end class InstructionCodeDescriptionTypeSub

class LabelPrintMethodCodeDescriptionTypeSub(supermod.LabelPrintMethodCodeDescriptionType):
# end class LabelPrintMethodCodeDescriptionTypeSub LEVEL2

class LabelStockSizeTypeSub(supermod.LabelStockSizeType):
# end class LabelStockSizeTypeSub

class LabelImageFormatCodeDescriptionTypeSub(supermod.LabelImageFormatCodeDescriptionType):
# end class LabelImageFormatCodeDescriptionTypeSub LEVEL2

class HazMatPackageInformationTypeSub(supermod.HazMatPackageInformationType):
# end class HazMatPackageInformationTypeSub

class HazMatTypeSub(supermod.HazMatType):
# end class HazMatTypeSub

class DryIceTypeSub(supermod.DryIceType):
# end class DryIceTypeSub

class DryIceWeightTypeSub(supermod.DryIceWeightType):
# end class DryIceWeightTypeSub

class ReceiptSpecificationTypeSub(supermod.ReceiptSpecificationType):
# end class ReceiptSpecificationTypeSub

class ImageFormatCodeDescriptionTypeSub(supermod.ImageFormatCodeDescriptionType):
# end class ImageFormatCodeDescriptionTypeSub

class AlternateDeliveryAddressTypeSub(supermod.AlternateDeliveryAddressType):
# end class AlternateDeliveryAddressTypeSub

class IndicationTypeSub(supermod.IndicationType):
# end class IndicationTypeSub

class ShipmentServiceOptionsNotificationVoiceMessageTypeSub(supermod.ShipmentServiceOptionsNotificationVoiceMessageType):
# end class ShipmentServiceOptionsNotificationVoiceMessageTypeSub

class ShipmentServiceOptionsNotificationTextMessageTypeSub(supermod.ShipmentServiceOptionsNotificationTextMessageType):
# end class ShipmentServiceOptionsNotificationTextMessageTypeSub

class ADLAddressTypeSub(supermod.ADLAddressType):
# end class ADLAddressTypeSub

class TaxIDCodeDescTypeSub(supermod.TaxIDCodeDescType):
# end class TaxIDCodeDescTypeSub

class DGSignatoryInfoTypeSub(supermod.DGSignatoryInfoType):
# end class DGSignatoryInfoTypeSub

class InternationalFormsTypeSub(supermod.InternationalFormsType):
# end class InternationalFormsTypeSub

class UPSPremiumCareFormTypeSub(supermod.UPSPremiumCareFormType):
# end class UPSPremiumCareFormTypeSub

class LanguageForUPSPremiumCareTypeSub(supermod.LanguageForUPSPremiumCareType):
# end class LanguageForUPSPremiumCareTypeSub

class UserCreatedFormTypeSub(supermod.UserCreatedFormType):
# end class UserCreatedFormTypeSub

class CN22FormTypeSub(supermod.CN22FormType):
# end class CN22FormTypeSub

class CN22ContentTypeSub(supermod.CN22ContentType):
# end class CN22ContentTypeSub

class AddressTypeSub(supermod.AddressType):
# end class AddressTypeSub
    
class BlanketPeriodTypeSub(supermod.BlanketPeriodType):
# end class BlanketPeriodTypeSub

class ContactsTypeSub(supermod.ContactsType):
# end class ContactsTypeSub

class CodeTypeSub(supermod.CodeType):
# end class CodeTypeSub

class DiscountTypeSub(supermod.DiscountType):
# end class DiscountTypeSub

class ForwardAgentTypeSub(supermod.ForwardAgentType):
# end class ForwardAgentTypeSub

class FreightChargesTypeSub(supermod.FreightChargesType):
# end class FreightChargesTypeSub

class InsuranceChargesTypeSub(supermod.InsuranceChargesType):
# end class InsuranceChargesTypeSub

class IntermediateConsigneeTypeSub(supermod.IntermediateConsigneeType):
# end class IntermediateConsigneeTypeSub

class LicenseTypeSub(supermod.LicenseType):
# end class LicenseTypeSub

class NetCostDateRangeTypeSub(supermod.NetCostDateRangeType):
# end class NetCostDateRangeTypeSub

class OtherChargesTypeSub(supermod.OtherChargesType):
# end class OtherChargesTypeSub


class PhoneTypeSub(supermod.PhoneType):
# end class PhoneTypeSub

class ProductTypeSub(supermod.ProductType):
# end class ProductTypeSub

class ExcludeFromFormTypeSub(supermod.ExcludeFromFormType):
# end class ExcludeFromFormTypeSub

class ProducerTypeSub(supermod.ProducerType):
# end class ProducerTypeSub

class ProductWeightTypeSub(supermod.ProductWeightType):
# end class ProductWeightTypeSub

class ScheduleBTypeSub(supermod.ScheduleBType):
# end class ScheduleBTypeSub

class UltimateConsigneeTypeSub(supermod.UltimateConsigneeType):
# end class UltimateConsigneeTypeSub

class UnitTypeSub(supermod.UnitType):
# end class UnitTypeSub


class PackingListInfoTypeSub(supermod.PackingListInfoType):
# end class PackingListInfoTypeSub

class PackageAssociatedTypeSub(supermod.PackageAssociatedType):
# end class PackageAssociatedTypeSub

class EEILicenseTypeSub(supermod.EEILicenseType):
# end class EEILicenseTypeSub

class EEIFilingOptionTypeSub(supermod.EEIFilingOptionType):
# end class EEIFilingOptionTypeSub

class UPSFiledTypeSub(supermod.UPSFiledType):
# end class UPSFiledTypeSub

class ShipperFiledTypeSub(supermod.ShipperFiledType):
# end class ShipperFiledTypeSub

class EEIInformationTypeSub(supermod.EEIInformationType):
# end class EEIInformationTypeSub

class POATypeSub(supermod.POAType):
# end class POATypeSub

class UltimateConsigneeTypeTypeSub(supermod.UltimateConsigneeTypeType):
# end class UltimateConsigneeTypeTypeSub

class DDTCInformationTypeSub(supermod.DDTCInformationType):
# end class DDTCInformationTypeSub


