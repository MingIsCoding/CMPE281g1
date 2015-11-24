package com.entities;

import java.util.Date;

/**
 * Created by YuexingYin on 11/23/15.
 */
public class Payments {
    private String paymentid;
    private String cardtype;
    private String cardnumber;
    private String holdername;
    private Date validdate;
    private String csc;
    private String billingaddress;
    private String city;
    private String state;
    private String zipcode;
    private String userid;

    public Payments(String paymentid, String cardtype, String cardnumber, String holdername, Date validdate, String csc,
                    String billingaddress, String city, String state, String zipcode, String userid) {
        this.paymentid = paymentid;
        this.cardtype = cardtype;
        this.cardnumber = cardnumber;
        this.holdername = holdername;
        this.validdate = validdate;
        this.csc = csc;
        this.billingaddress = billingaddress;
        this.city = city;
        this.state = state;
        this.zipcode = zipcode;
        this.userid = userid;
    }

    public String getPaymentid() {
        return paymentid;
    }

    public String getCardtype() {
        return cardtype;
    }

    public String getCardnumber() {
        return cardnumber;
    }

    public String getHoldername() {
        return holdername;
    }

    public Date getValiddate() {
        return validdate;
    }

    public String getCsc() {
        return csc;
    }

    public String getBillingaddress() {
        return billingaddress;
    }

    public String getCity() {
        return city;
    }

    public String getState() {
        return state;
    }

    public String getZipcode() {
        return zipcode;
    }

    public String getUserid() {
        return userid;
    }
}

