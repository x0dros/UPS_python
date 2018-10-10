﻿//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//     Runtime Version:4.0.30319.17929
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

// 
// This source code was auto-generated by Microsoft.VSDesigner, Version 4.0.30319.17929.
// 
#pragma warning disable 1591

namespace LabelRecoveryExample.LabelRecoveryWebReference {
    using System;
    using System.Web.Services;
    using System.Diagnostics;
    using System.Web.Services.Protocols;
    using System.Xml.Serialization;
    using System.ComponentModel;
    
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Web.Services", "4.0.30319.17929")]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Web.Services.WebServiceBindingAttribute(Name="LabelRecoveryBinding", Namespace="http://www.ups.com/WSDL/XOLTWS/LBRecovery/v1.0")]
    public partial class LBRecovery : System.Web.Services.Protocols.SoapHttpClientProtocol {
        
        private UPSSecurity uPSSecurityValueField;
        
        private System.Threading.SendOrPostCallback ProcessLabelRecoveryOperationCompleted;
        
        private bool useDefaultCredentialsSetExplicitly;
        
        /// <remarks/>
        public LBRecovery() {
            this.Url = global::LabelRecoveryExample.Properties.Settings.Default.lbdotnet_LabelRecoveryWebReference_LBRecovery;
            if ((this.IsLocalFileSystemWebService(this.Url) == true)) {
                this.UseDefaultCredentials = true;
                this.useDefaultCredentialsSetExplicitly = false;
            }
            else {
                this.useDefaultCredentialsSetExplicitly = true;
            }
        }
        
        public UPSSecurity UPSSecurityValue {
            get {
                return this.uPSSecurityValueField;
            }
            set {
                this.uPSSecurityValueField = value;
            }
        }
        
        public new string Url {
            get {
                return base.Url;
            }
            set {
                if ((((this.IsLocalFileSystemWebService(base.Url) == true) 
                            && (this.useDefaultCredentialsSetExplicitly == false)) 
                            && (this.IsLocalFileSystemWebService(value) == false))) {
                    base.UseDefaultCredentials = false;
                }
                base.Url = value;
            }
        }
        
        public new bool UseDefaultCredentials {
            get {
                return base.UseDefaultCredentials;
            }
            set {
                base.UseDefaultCredentials = value;
                this.useDefaultCredentialsSetExplicitly = true;
            }
        }
        
        /// <remarks/>
        public event ProcessLabelRecoveryCompletedEventHandler ProcessLabelRecoveryCompleted;
        
        /// <remarks/>
        [System.Web.Services.Protocols.SoapHeaderAttribute("UPSSecurityValue")]
        [System.Web.Services.Protocols.SoapDocumentMethodAttribute("http://onlinetools.ups.com/webservices/ShipBinding/v1.1", Use=System.Web.Services.Description.SoapBindingUse.Literal, ParameterStyle=System.Web.Services.Protocols.SoapParameterStyle.Bare)]
        [return: System.Xml.Serialization.XmlElementAttribute("LabelRecoveryResponse", Namespace="http://www.ups.com/XMLSchema/XOLTWS/LBRecovery/v1.0")]
        public LabelRecoveryResponse ProcessLabelRecovery([System.Xml.Serialization.XmlElementAttribute(Namespace="http://www.ups.com/XMLSchema/XOLTWS/LBRecovery/v1.0")] LabelRecoveryRequest LabelRecoveryRequest) {
            object[] results = this.Invoke("ProcessLabelRecovery", new object[] {
                        LabelRecoveryRequest});
            return ((LabelRecoveryResponse)(results[0]));
        }
        
        /// <remarks/>
        public void ProcessLabelRecoveryAsync(LabelRecoveryRequest LabelRecoveryRequest) {
            this.ProcessLabelRecoveryAsync(LabelRecoveryRequest, null);
        }
        
        /// <remarks/>
        public void ProcessLabelRecoveryAsync(LabelRecoveryRequest LabelRecoveryRequest, object userState) {
            if ((this.ProcessLabelRecoveryOperationCompleted == null)) {
                this.ProcessLabelRecoveryOperationCompleted = new System.Threading.SendOrPostCallback(this.OnProcessLabelRecoveryOperationCompleted);
            }
            this.InvokeAsync("ProcessLabelRecovery", new object[] {
                        LabelRecoveryRequest}, this.ProcessLabelRecoveryOperationCompleted, userState);
        }
        
        private void OnProcessLabelRecoveryOperationCompleted(object arg) {
            if ((this.ProcessLabelRecoveryCompleted != null)) {
                System.Web.Services.Protocols.InvokeCompletedEventArgs invokeArgs = ((System.Web.Services.Protocols.InvokeCompletedEventArgs)(arg));
                this.ProcessLabelRecoveryCompleted(this, new ProcessLabelRecoveryCompletedEventArgs(invokeArgs.Results, invokeArgs.Error, invokeArgs.Cancelled, invokeArgs.UserState));
            }
        }
        
        /// <remarks/>
        public new void CancelAsync(object userState) {
            base.CancelAsync(userState);
        }
        
        private bool IsLocalFileSystemWebService(string url) {
            if (((url == null) 
                        || (url == string.Empty))) {
                return false;
            }
            System.Uri wsUri = new System.Uri(url);
            if (((wsUri.Port >= 1024) 
                        && (string.Compare(wsUri.Host, "localHost", System.StringComparison.OrdinalIgnoreCase) == 0))) {
                return true;
            }
            return false;
        }
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Xml", "4.0.30319.17929")]
    [System.SerializableAttribute()]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(AnonymousType=true, Namespace="http://www.ups.com/XMLSchema/XOLTWS/UPSS/v1.0")]
    [System.Xml.Serialization.XmlRootAttribute(Namespace="http://www.ups.com/XMLSchema/XOLTWS/UPSS/v1.0", IsNullable=false)]
    public partial class UPSSecurity : System.Web.Services.Protocols.SoapHeader {
        
        private UPSSecurityUsernameToken usernameTokenField;
        
        private UPSSecurityServiceAccessToken serviceAccessTokenField;
        
        /// <remarks/>
        public UPSSecurityUsernameToken UsernameToken {
            get {
                return this.usernameTokenField;
            }
            set {
                this.usernameTokenField = value;
            }
        }
        
        /// <remarks/>
        public UPSSecurityServiceAccessToken ServiceAccessToken {
            get {
                return this.serviceAccessTokenField;
            }
            set {
                this.serviceAccessTokenField = value;
            }
        }
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Xml", "4.0.30319.17929")]
    [System.SerializableAttribute()]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(AnonymousType=true, Namespace="http://www.ups.com/XMLSchema/XOLTWS/UPSS/v1.0")]
    public partial class UPSSecurityUsernameToken {
        
        private string usernameField;
        
        private string passwordField;
        
        private string authenticationTokenField;
        
        /// <remarks/>
        public string Username {
            get {
                return this.usernameField;
            }
            set {
                this.usernameField = value;
            }
        }
        
        /// <remarks/>
        public string Password {
            get {
                return this.passwordField;
            }
            set {
                this.passwordField = value;
            }
        }
        
        /// <remarks/>
        public string AuthenticationToken {
            get {
                return this.authenticationTokenField;
            }
            set {
                this.authenticationTokenField = value;
            }
        }
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Xml", "4.0.30319.17929")]
    [System.SerializableAttribute()]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(Namespace="http://www.ups.com/XMLSchema/XOLTWS/LBRecovery/v1.0")]
    public partial class PickupDateRangeType {
        
        private string beginDateField;
        
        private string endDateField;
        
        /// <remarks/>
        public string BeginDate {
            get {
                return this.beginDateField;
            }
            set {
                this.beginDateField = value;
            }
        }
        
        /// <remarks/>
        public string EndDate {
            get {
                return this.endDateField;
            }
            set {
                this.endDateField = value;
            }
        }
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Xml", "4.0.30319.17929")]
    [System.SerializableAttribute()]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(Namespace="http://www.ups.com/XMLSchema/XOLTWS/LBRecovery/v1.0")]
    public partial class TrackingCandidateType {
        
        private string trackingNumberField;
        
        private string destinationPostalCodeField;
        
        private string destinationCountryCodeField;
        
        private PickupDateRangeType pickupDateRangeField;
        
        /// <remarks/>
        public string TrackingNumber {
            get {
                return this.trackingNumberField;
            }
            set {
                this.trackingNumberField = value;
            }
        }
        
        /// <remarks/>
        public string DestinationPostalCode {
            get {
                return this.destinationPostalCodeField;
            }
            set {
                this.destinationPostalCodeField = value;
            }
        }
        
        /// <remarks/>
        public string DestinationCountryCode {
            get {
                return this.destinationCountryCodeField;
            }
            set {
                this.destinationCountryCodeField = value;
            }
        }
        
        /// <remarks/>
        public PickupDateRangeType PickupDateRange {
            get {
                return this.pickupDateRangeField;
            }
            set {
                this.pickupDateRangeField = value;
            }
        }
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Xml", "4.0.30319.17929")]
    [System.SerializableAttribute()]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(Namespace="http://www.ups.com/XMLSchema/XOLTWS/LBRecovery/v1.0")]
    public partial class ImageType {
        
        private LabelImageFormatType imageFormatField;
        
        private string graphicImageField;
        
        /// <remarks/>
        public LabelImageFormatType ImageFormat {
            get {
                return this.imageFormatField;
            }
            set {
                this.imageFormatField = value;
            }
        }
        
        /// <remarks/>
        public string GraphicImage {
            get {
                return this.graphicImageField;
            }
            set {
                this.graphicImageField = value;
            }
        }
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Xml", "4.0.30319.17929")]
    [System.SerializableAttribute()]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(Namespace="http://www.ups.com/XMLSchema/XOLTWS/LBRecovery/v1.0")]
    public partial class LabelImageFormatType {
        
        private string codeField;
        
        /// <remarks/>
        public string Code {
            get {
                return this.codeField;
            }
            set {
                this.codeField = value;
            }
        }
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Xml", "4.0.30319.17929")]
    [System.SerializableAttribute()]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(Namespace="http://www.ups.com/XMLSchema/XOLTWS/LBRecovery/v1.0")]
    public partial class ReceiptType {
        
        private string hTMLImageField;
        
        private ImageType imageField;
        
        /// <remarks/>
        public string HTMLImage {
            get {
                return this.hTMLImageField;
            }
            set {
                this.hTMLImageField = value;
            }
        }
        
        /// <remarks/>
        public ImageType Image {
            get {
                return this.imageField;
            }
            set {
                this.imageField = value;
            }
        }
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Xml", "4.0.30319.17929")]
    [System.SerializableAttribute()]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(Namespace="http://www.ups.com/XMLSchema/XOLTWS/LBRecovery/v1.0")]
    public partial class LabelImageType {
        
        private LabelImageFormatType labelImageFormatField;
        
        private string graphicImageField;
        
        private string hTMLImageField;
        
        private string pDF417Field;
        
        private string internationalSignatureGraphicImageField;
        
        private string uRLField;
        
        /// <remarks/>
        public LabelImageFormatType LabelImageFormat {
            get {
                return this.labelImageFormatField;
            }
            set {
                this.labelImageFormatField = value;
            }
        }
        
        /// <remarks/>
        public string GraphicImage {
            get {
                return this.graphicImageField;
            }
            set {
                this.graphicImageField = value;
            }
        }
        
        /// <remarks/>
        public string HTMLImage {
            get {
                return this.hTMLImageField;
            }
            set {
                this.hTMLImageField = value;
            }
        }
        
        /// <remarks/>
        public string PDF417 {
            get {
                return this.pDF417Field;
            }
            set {
                this.pDF417Field = value;
            }
        }
        
        /// <remarks/>
        public string InternationalSignatureGraphicImage {
            get {
                return this.internationalSignatureGraphicImageField;
            }
            set {
                this.internationalSignatureGraphicImageField = value;
            }
        }
        
        /// <remarks/>
        public string URL {
            get {
                return this.uRLField;
            }
            set {
                this.uRLField = value;
            }
        }
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Xml", "4.0.30319.17929")]
    [System.SerializableAttribute()]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(Namespace="http://www.ups.com/XMLSchema/XOLTWS/LBRecovery/v1.0")]
    public partial class LabelResultsType {
        
        private string trackingNumberField;
        
        private LabelImageType labelImageField;
        
        private ReceiptType receiptField;
        
        /// <remarks/>
        public string TrackingNumber {
            get {
                return this.trackingNumberField;
            }
            set {
                this.trackingNumberField = value;
            }
        }
        
        /// <remarks/>
        public LabelImageType LabelImage {
            get {
                return this.labelImageField;
            }
            set {
                this.labelImageField = value;
            }
        }
        
        /// <remarks/>
        public ReceiptType Receipt {
            get {
                return this.receiptField;
            }
            set {
                this.receiptField = value;
            }
        }
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Xml", "4.0.30319.17929")]
    [System.SerializableAttribute()]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(Namespace="http://www.ups.com/XMLSchema/XOLTWS/Common/v1.0")]
    public partial class CodeDescriptionType {
        
        private string codeField;
        
        private string descriptionField;
        
        /// <remarks/>
        public string Code {
            get {
                return this.codeField;
            }
            set {
                this.codeField = value;
            }
        }
        
        /// <remarks/>
        public string Description {
            get {
                return this.descriptionField;
            }
            set {
                this.descriptionField = value;
            }
        }
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Xml", "4.0.30319.17929")]
    [System.SerializableAttribute()]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(Namespace="http://www.ups.com/XMLSchema/XOLTWS/Common/v1.0")]
    public partial class ResponseType {
        
        private CodeDescriptionType responseStatusField;
        
        private CodeDescriptionType[] alertField;
        
        private TransactionReferenceType transactionReferenceField;
        
        /// <remarks/>
        public CodeDescriptionType ResponseStatus {
            get {
                return this.responseStatusField;
            }
            set {
                this.responseStatusField = value;
            }
        }
        
        /// <remarks/>
        [System.Xml.Serialization.XmlElementAttribute("Alert")]
        public CodeDescriptionType[] Alert {
            get {
                return this.alertField;
            }
            set {
                this.alertField = value;
            }
        }
        
        /// <remarks/>
        public TransactionReferenceType TransactionReference {
            get {
                return this.transactionReferenceField;
            }
            set {
                this.transactionReferenceField = value;
            }
        }
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Xml", "4.0.30319.17929")]
    [System.SerializableAttribute()]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(Namespace="http://www.ups.com/XMLSchema/XOLTWS/Common/v1.0")]
    public partial class TransactionReferenceType {
        
        private string customerContextField;
        
        private string transactionIdentifierField;
        
        /// <remarks/>
        public string CustomerContext {
            get {
                return this.customerContextField;
            }
            set {
                this.customerContextField = value;
            }
        }
        
        /// <remarks/>
        public string TransactionIdentifier {
            get {
                return this.transactionIdentifierField;
            }
            set {
                this.transactionIdentifierField = value;
            }
        }
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Xml", "4.0.30319.17929")]
    [System.SerializableAttribute()]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(Namespace="http://www.ups.com/XMLSchema/XOLTWS/LBRecovery/v1.0")]
    public partial class ReferenceNumberType {
        
        private string valueField;
        
        /// <remarks/>
        public string Value {
            get {
                return this.valueField;
            }
            set {
                this.valueField = value;
            }
        }
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Xml", "4.0.30319.17929")]
    [System.SerializableAttribute()]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(Namespace="http://www.ups.com/XMLSchema/XOLTWS/LBRecovery/v1.0")]
    public partial class ReferenceValuesType {
        
        private ReferenceNumberType referenceNumberField;
        
        private string shipperNumberField;
        
        /// <remarks/>
        public ReferenceNumberType ReferenceNumber {
            get {
                return this.referenceNumberField;
            }
            set {
                this.referenceNumberField = value;
            }
        }
        
        /// <remarks/>
        public string ShipperNumber {
            get {
                return this.shipperNumberField;
            }
            set {
                this.shipperNumberField = value;
            }
        }
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Xml", "4.0.30319.17929")]
    [System.SerializableAttribute()]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(Namespace="http://www.ups.com/XMLSchema/XOLTWS/LBRecovery/v1.0")]
    public partial class EMailMessageType {
        
        private string eMailAddressField;
        
        /// <remarks/>
        public string EMailAddress {
            get {
                return this.eMailAddressField;
            }
            set {
                this.eMailAddressField = value;
            }
        }
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Xml", "4.0.30319.17929")]
    [System.SerializableAttribute()]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(Namespace="http://www.ups.com/XMLSchema/XOLTWS/LBRecovery/v1.0")]
    public partial class LabelDeliveryType {
        
        private string labelLinkIndicatorField;
        
        private string resendEMailIndicatorField;
        
        private EMailMessageType eMailMessageField;
        
        /// <remarks/>
        public string LabelLinkIndicator {
            get {
                return this.labelLinkIndicatorField;
            }
            set {
                this.labelLinkIndicatorField = value;
            }
        }
        
        /// <remarks/>
        public string ResendEMailIndicator {
            get {
                return this.resendEMailIndicatorField;
            }
            set {
                this.resendEMailIndicatorField = value;
            }
        }
        
        /// <remarks/>
        public EMailMessageType EMailMessage {
            get {
                return this.eMailMessageField;
            }
            set {
                this.eMailMessageField = value;
            }
        }
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Xml", "4.0.30319.17929")]
    [System.SerializableAttribute()]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(Namespace="http://www.ups.com/XMLSchema/XOLTWS/LBRecovery/v1.0")]
    public partial class TranslateType {
        
        private string languageCodeField;
        
        private string dialectCodeField;
        
        private string codeField;
        
        /// <remarks/>
        public string LanguageCode {
            get {
                return this.languageCodeField;
            }
            set {
                this.languageCodeField = value;
            }
        }
        
        /// <remarks/>
        public string DialectCode {
            get {
                return this.dialectCodeField;
            }
            set {
                this.dialectCodeField = value;
            }
        }
        
        /// <remarks/>
        public string Code {
            get {
                return this.codeField;
            }
            set {
                this.codeField = value;
            }
        }
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Xml", "4.0.30319.17929")]
    [System.SerializableAttribute()]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(Namespace="http://www.ups.com/XMLSchema/XOLTWS/LBRecovery/v1.0")]
    public partial class LabelSpecificationType {
        
        private string hTTPUserAgentField;
        
        private LabelImageFormatType labelImageFormatField;
        
        /// <remarks/>
        public string HTTPUserAgent {
            get {
                return this.hTTPUserAgentField;
            }
            set {
                this.hTTPUserAgentField = value;
            }
        }
        
        /// <remarks/>
        public LabelImageFormatType LabelImageFormat {
            get {
                return this.labelImageFormatField;
            }
            set {
                this.labelImageFormatField = value;
            }
        }
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Xml", "4.0.30319.17929")]
    [System.SerializableAttribute()]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(Namespace="http://www.ups.com/XMLSchema/XOLTWS/Common/v1.0")]
    public partial class RequestType {
        
        private string[] requestOptionField;
        
        private TransactionReferenceType transactionReferenceField;
        
        /// <remarks/>
        [System.Xml.Serialization.XmlElementAttribute("RequestOption")]
        public string[] RequestOption {
            get {
                return this.requestOptionField;
            }
            set {
                this.requestOptionField = value;
            }
        }
        
        /// <remarks/>
        public TransactionReferenceType TransactionReference {
            get {
                return this.transactionReferenceField;
            }
            set {
                this.transactionReferenceField = value;
            }
        }
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Xml", "4.0.30319.17929")]
    [System.SerializableAttribute()]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(AnonymousType=true, Namespace="http://www.ups.com/XMLSchema/XOLTWS/UPSS/v1.0")]
    public partial class UPSSecurityServiceAccessToken {
        
        private string accessLicenseNumberField;
        
        /// <remarks/>
        public string AccessLicenseNumber {
            get {
                return this.accessLicenseNumberField;
            }
            set {
                this.accessLicenseNumberField = value;
            }
        }
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Xml", "4.0.30319.17929")]
    [System.SerializableAttribute()]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(AnonymousType=true, Namespace="http://www.ups.com/XMLSchema/XOLTWS/LBRecovery/v1.0")]
    public partial class LabelRecoveryRequest {
        
        private RequestType requestField;
        
        private LabelSpecificationType labelSpecificationField;
        
        private TranslateType translateField;
        
        private LabelDeliveryType labelDeliveryField;
        
        private string trackingNumberField;
        
        private ReferenceValuesType referenceValuesField;
        
        /// <remarks/>
        [System.Xml.Serialization.XmlElementAttribute(Namespace="http://www.ups.com/XMLSchema/XOLTWS/Common/v1.0")]
        public RequestType Request {
            get {
                return this.requestField;
            }
            set {
                this.requestField = value;
            }
        }
        
        /// <remarks/>
        public LabelSpecificationType LabelSpecification {
            get {
                return this.labelSpecificationField;
            }
            set {
                this.labelSpecificationField = value;
            }
        }
        
        /// <remarks/>
        public TranslateType Translate {
            get {
                return this.translateField;
            }
            set {
                this.translateField = value;
            }
        }
        
        /// <remarks/>
        public LabelDeliveryType LabelDelivery {
            get {
                return this.labelDeliveryField;
            }
            set {
                this.labelDeliveryField = value;
            }
        }
        
        /// <remarks/>
        public string TrackingNumber {
            get {
                return this.trackingNumberField;
            }
            set {
                this.trackingNumberField = value;
            }
        }
        
        /// <remarks/>
        public ReferenceValuesType ReferenceValues {
            get {
                return this.referenceValuesField;
            }
            set {
                this.referenceValuesField = value;
            }
        }
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Xml", "4.0.30319.17929")]
    [System.SerializableAttribute()]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(AnonymousType=true, Namespace="http://www.ups.com/XMLSchema/XOLTWS/LBRecovery/v1.0")]
    public partial class LabelRecoveryResponse {
        
        private ResponseType responseField;
        
        private string shipmentIdentificationNumberField;
        
        private object[] itemsField;
        
        /// <remarks/>
        [System.Xml.Serialization.XmlElementAttribute(Namespace="http://www.ups.com/XMLSchema/XOLTWS/Common/v1.0")]
        public ResponseType Response {
            get {
                return this.responseField;
            }
            set {
                this.responseField = value;
            }
        }
        
        /// <remarks/>
        public string ShipmentIdentificationNumber {
            get {
                return this.shipmentIdentificationNumberField;
            }
            set {
                this.shipmentIdentificationNumberField = value;
            }
        }
        
        /// <remarks/>
        [System.Xml.Serialization.XmlElementAttribute("LabelResults", typeof(LabelResultsType))]
        [System.Xml.Serialization.XmlElementAttribute("TrackingCandidate", typeof(TrackingCandidateType))]
        public object[] Items {
            get {
                return this.itemsField;
            }
            set {
                this.itemsField = value;
            }
        }
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Web.Services", "4.0.30319.17929")]
    public delegate void ProcessLabelRecoveryCompletedEventHandler(object sender, ProcessLabelRecoveryCompletedEventArgs e);
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Web.Services", "4.0.30319.17929")]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    public partial class ProcessLabelRecoveryCompletedEventArgs : System.ComponentModel.AsyncCompletedEventArgs {
        
        private object[] results;
        
        internal ProcessLabelRecoveryCompletedEventArgs(object[] results, System.Exception exception, bool cancelled, object userState) : 
                base(exception, cancelled, userState) {
            this.results = results;
        }
        
        /// <remarks/>
        public LabelRecoveryResponse Result {
            get {
                this.RaiseExceptionIfNecessary();
                return ((LabelRecoveryResponse)(this.results[0]));
            }
        }
    }
}

#pragma warning restore 1591