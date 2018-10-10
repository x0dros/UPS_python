/*
 **
 ** Filename: Axis2FreightShipClient.java
 ** Authors: United Parcel Service of America
 **
 ** The use, disclosure, reproduction, modification, transfer, or transmittal
 ** of this work for any purpose in any form or by any means without the
 ** written permission of United Parcel Service is strictly prohibited.
 **
 ** Confidential, Unpublished Property of United Parcel Service.
 ** Use and Distribution Limited Solely to Authorized Personnel.
 **
 ** Copyright 2009 United Parcel Service of America, Inc.  All Rights Reserved.
 **
 */
package com.ups.xolt.codesamples;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Calendar;
import java.util.Properties;

import com.ups.www.wsdl.xoltws.freightship.v1_0.FreightShipServiceStub;
import com.ups.www.wsdl.xoltws.freightship.v1_0.ShipErrorMessage;
import com.ups.www.wsdl.xoltws.freightship.v1_0.FreightShipServiceStub.CommodityType;
import com.ups.www.wsdl.xoltws.freightship.v1_0.FreightShipServiceStub.CommodityValueType;
import com.ups.www.wsdl.xoltws.freightship.v1_0.FreightShipServiceStub.FreightShipAddressType;
import com.ups.www.wsdl.xoltws.freightship.v1_0.FreightShipServiceStub.FreightShipPhoneType;
import com.ups.www.wsdl.xoltws.freightship.v1_0.FreightShipServiceStub.FreightShipRequest;
import com.ups.www.wsdl.xoltws.freightship.v1_0.FreightShipServiceStub.FreightShipResponse;
import com.ups.www.wsdl.xoltws.freightship.v1_0.FreightShipServiceStub.FreightShipUnitOfMeasurementType;
import com.ups.www.wsdl.xoltws.freightship.v1_0.FreightShipServiceStub.HandlingUnitType;
import com.ups.www.wsdl.xoltws.freightship.v1_0.FreightShipServiceStub.NMFCCommodityType;
import com.ups.www.wsdl.xoltws.freightship.v1_0.FreightShipServiceStub.PayerType;
import com.ups.www.wsdl.xoltws.freightship.v1_0.FreightShipServiceStub.PaymentInformationType;
import com.ups.www.wsdl.xoltws.freightship.v1_0.FreightShipServiceStub.RequestType;
import com.ups.www.wsdl.xoltws.freightship.v1_0.FreightShipServiceStub.ServiceAccessToken_type0;
import com.ups.www.wsdl.xoltws.freightship.v1_0.FreightShipServiceStub.ShipCodeDescriptionType;
import com.ups.www.wsdl.xoltws.freightship.v1_0.FreightShipServiceStub.ShipFromType;
import com.ups.www.wsdl.xoltws.freightship.v1_0.FreightShipServiceStub.ShipToType;
import com.ups.www.wsdl.xoltws.freightship.v1_0.FreightShipServiceStub.ShipmentType;
import com.ups.www.wsdl.xoltws.freightship.v1_0.FreightShipServiceStub.UPSSecurity;
import com.ups.www.wsdl.xoltws.freightship.v1_0.FreightShipServiceStub.UsernameToken_type0;
import com.ups.www.wsdl.xoltws.freightship.v1_0.FreightShipServiceStub.WeightType;

public class Axis2GroundFreightShipClient {
	private static String url;
	private static String accessKey;
	private static String userName;
	private static String password;
	private static String buildPropertiesPath="./build.properties";
	private static String out_file_location="out_file_location";
	private static String tool_or_webservice_name="tool_or_webservice_name";
    private static String statusCode = null;
	private static String description = null;

	private static void loadProperties(){
		Properties properties = new Properties();
		try {
			properties.load(new FileInputStream(buildPropertiesPath));

		} catch (IOException e) {
			statusCode = e.getMessage();
			description = e.toString();
			updateResultsToFile(statusCode, description);
			e.printStackTrace();
		}
		url=properties.getProperty("url");
		accessKey=properties.getProperty("accesskey");
		userName=properties.getProperty("username");
		password=properties.getProperty("password");
		out_file_location=properties.getProperty("out_file_location");
		tool_or_webservice_name=properties.getProperty("tool_or_webservice_name");
	}

	public static void main(String[] arguments) throws Exception {
		try {
			loadProperties();
			FreightShipServiceStub freightShipServiceStub = new FreightShipServiceStub(url);
			FreightShipResponse freightShipResponse = freightShipServiceStub.ProcessShipment(populateGroundFreightRateRequest(), populateUPSSecurity());
			System.out.println("The transaction was a "
					+ freightShipResponse.getResponse().getResponseStatus()
							.getDescription());
			System.out.println("The BOLID of the shipment is "
					+ freightShipResponse.getShipmentResults().getBOLID());

			System.out.println("The Shipment number of the shipment is "
					+ freightShipResponse.getShipmentResults().getShipmentNumber());

			statusCode = freightShipResponse.getResponse().getResponseStatus().getCode();
            description = freightShipResponse.getResponse().getResponseStatus().getDescription();
			updateResultsToFile(statusCode, description);
		} catch (Exception e) {
			description=e.getMessage();
			statusCode=e.toString();

			if(e instanceof ShipErrorMessage){
				ShipErrorMessage shpErr = (ShipErrorMessage)e;
				System.out.println(shpErr.getFaultMessage().getErrorDetail()[0].getPrimaryErrorCode().getCode());
				System.out.println(shpErr.getFaultMessage().getErrorDetail()[0].getPrimaryErrorCode().getDescription());
				description=shpErr.getFaultMessage().getErrorDetail()[0].getPrimaryErrorCode().getDescription();
				statusCode=shpErr.getFaultMessage().getErrorDetail()[0].getPrimaryErrorCode().getCode();
			}

			updateResultsToFile(statusCode, description);
		//	e.printStackTrace();
		}
	}

	private static FreightShipRequest populateGroundFreightRateRequest(){
		FreightShipRequest freightShipRequest = new FreightShipRequest();
		RequestType request = new RequestType();
		String[] requestOption = { "1" };
		request.setRequestOption(requestOption);
		freightShipRequest.setRequest(request);
		ShipmentType shipment = new ShipmentType();

		/** ****************ShipFrom******************************* */
		ShipFromType shipFrom = new ShipFromType();
		FreightShipAddressType shipFromAddress = new FreightShipAddressType();
		String[] shipFromAddressLines = { "AddressLine1" };
		shipFromAddress.setAddressLine(shipFromAddressLines);
		shipFromAddress.setCity("Roswell");
		shipFromAddress.setStateProvinceCode("GA");
		shipFromAddress.setPostalCode("30076");
		shipFromAddress.setCountryCode("US");
		shipFrom.setAddress(shipFromAddress);
		shipFrom.setAttentionName("Mr. ABC");
		shipFrom.setName("ABC Associates");
		FreightShipPhoneType shipFromPhone = new FreightShipPhoneType();
		shipFromPhone.setNumber("123456789");
		shipFromPhone.setExtension("34567");
		shipFrom.setPhone(shipFromPhone);
		shipFrom.setEMailAddress("wbb6tdf@ups.com");
		shipment.setShipFrom(shipFrom);
		/** ****************ShipFrom******************************* */

		shipment.setShipperNumber("222006");

		/** ****************ShipTo*************************************** */
		ShipToType shipTo = new ShipToType();
		FreightShipAddressType shipToAddress = new FreightShipAddressType();
		String[] shipToAddressLines = { "123 main st", "Address Line2",
				"Address Line3" };
		shipToAddress.setAddressLine(shipToAddressLines);
		shipToAddress.setCity("Roswell");
		shipToAddress.setStateProvinceCode("GA");
		shipToAddress.setPostalCode("30076");
		shipToAddress.setCountryCode("US");
		shipTo.setAddress(shipFromAddress);
		shipTo.setAttentionName("DEF Associates");
		shipTo.setName("DEF");
		FreightShipPhoneType shipToPhone = new FreightShipPhoneType();
		shipToPhone.setNumber("123456789");
		shipToPhone.setExtension("34567");
		shipTo.setPhone(shipToPhone);
		shipTo.setEMailAddress("wbb6tdf@ups.com");
		shipment.setShipTo(shipTo);
		/** ****************ShipTo*************************************** */

		/** ***************PaymentInformationType************************* */
		PaymentInformationType paymentInfo = new PaymentInformationType();
		PayerType payer = new PayerType();
		payer.setAttentionName("Mr. ABC");
		payer.setName("ABC Associates");
		FreightShipPhoneType payerPhone = new FreightShipPhoneType();
		payerPhone.setNumber("123456789");
		payerPhone.setExtension("3456");
		payer.setPhone(payerPhone);
		payer.setShipperNumber("Your Shipper Number");
		payer.setEMailAddress("xxx2yyy@ups.com");
		FreightShipAddressType payerAddress = new FreightShipAddressType();
		String[] payerAddressLines = { "123 main st", "Address Line2",
				"Address Line3" };
		payerAddress.setAddressLine(payerAddressLines);
		payerAddress.setCity("Roswell");
		payerAddress.setStateProvinceCode("GA");
		payerAddress.setPostalCode("30075");
		payerAddress.setCountryCode("US");
		payer.setAddress(payerAddress);
		paymentInfo.setPayer(payer);
		ShipCodeDescriptionType shipBillOption = new ShipCodeDescriptionType();
		shipBillOption.setCode("10");
		shipBillOption.setDescription("PREPAID");
		paymentInfo.setShipmentBillingOption(shipBillOption);
		shipment.setPaymentInformation(paymentInfo);
		/** ***************PaymentInformationType************************* */

		/** ***************Service************************************** */
		ShipCodeDescriptionType service = new ShipCodeDescriptionType();
		service.setCode("309");
		service.setDescription("UPS Ground Freight");
		shipment.setService(service);
		/** ***************Service************************************** */

		/** **************Commodity************************************* */
		CommodityType commodity = new CommodityType();
		commodity.setNumberOfPieces("20");
		NMFCCommodityType nmfcCommodity = new NMFCCommodityType();
		nmfcCommodity.setPrimeCode("132680");
		nmfcCommodity.setSubCode("02");
		commodity.setNMFCCommodity(nmfcCommodity);
		commodity.setFreightClass("77.5");
		ShipCodeDescriptionType packagingType = new ShipCodeDescriptionType();
		packagingType.setCode("BAG");
		packagingType.setDescription("BAG");
		commodity.setPackagingType(packagingType);
		WeightType weight = new WeightType();
		weight.setValue("200");
		FreightShipUnitOfMeasurementType unitOfMeasurement = new FreightShipUnitOfMeasurementType();
		unitOfMeasurement.setCode("lbs");
		unitOfMeasurement.setDescription("pounds");
		weight.setUnitOfMeasurement(unitOfMeasurement);
		commodity.setWeight(weight);
		CommodityValueType commodityValue = new CommodityValueType();
		commodityValue.setCurrencyCode("USD");
		commodityValue.setMonetaryValue("100");
		commodity.setCommodityValue(commodityValue);
		commodity.setDescription("LCD TVS");
		CommodityType[] commodityArray = { commodity };
		shipment.setCommodity(commodityArray);
		/** **************Commodity************************************* */

		/** **************HandlingUnitOne************************** */
		HandlingUnitType handlingUnit = new HandlingUnitType();
		handlingUnit.setQuantity("1");
		ShipCodeDescriptionType handlingUnitType = new ShipCodeDescriptionType();
		handlingUnitType.setCode("SKD");
		handlingUnitType.setDescription("SKID");
		handlingUnit.setType(handlingUnitType);
		shipment.setHandlingUnitOne(handlingUnit);
		/** **************HandlingUnitOne************************** */
		freightShipRequest.setShipment(shipment);
		return freightShipRequest;
	}


	private static UPSSecurity populateUPSSecurity() {
		UPSSecurity upss = new UPSSecurity();
		ServiceAccessToken_type0 upsSvcToken = new ServiceAccessToken_type0();
		upsSvcToken.setAccessLicenseNumber(accessKey);
		upss.setServiceAccessToken(upsSvcToken);
		UsernameToken_type0 upsSecUsrnameToken = new UsernameToken_type0();
		upsSecUsrnameToken.setUsername(userName);
		upsSecUsrnameToken.setPassword(password);
		upss.setUsernameToken(upsSecUsrnameToken);

		return upss;
	}


	/**
     * This method updates the XOLTResult.xml file with the received status and description
     * @param statusCode
     * @param description
     */
	   private static void updateResultsToFile(String statusCode, String description){
	    	BufferedWriter bw = null;
	    	try{

	    		File outFile = new File(out_file_location);
	    		System.out.println("Output file deletion status: " + outFile.delete());
	    		outFile.createNewFile();
	    		System.out.println("Output file location: " + outFile.getCanonicalPath());
	    		bw = new BufferedWriter(new FileWriter(outFile));
	    		StringBuffer strBuf = new StringBuffer();
	    		strBuf.append("<ExecutionAt>");
	    		strBuf.append(Calendar.getInstance().getTime());
	    		strBuf.append("</ExecutionAt>\n");
	    		strBuf.append("<ToolOrWebServiceName>");
	    		strBuf.append(tool_or_webservice_name);
	    		strBuf.append("</ToolOrWebServiceName>\n");
	    		strBuf.append("\n");
	    		strBuf.append("<ResponseStatus>\n");
	    		strBuf.append("\t<Code>");
	    		strBuf.append(statusCode);
	    		strBuf.append("</Code>\n");
	    		strBuf.append("\t<Description>");
	    		strBuf.append(description);
	    		strBuf.append("</Description>\n");
	    		strBuf.append("</ResponseStatus>");
	    		bw.write(strBuf.toString());
	    		bw.close();
	    	}catch (Exception e) {
				e.printStackTrace();
			}finally{
				try{
					if (bw != null){
						bw.close();
						bw = null;
					}
				}catch (Exception e) {
					e.printStackTrace();
				}
			}
	    }
}
