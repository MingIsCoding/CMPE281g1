package com.entities;

/**
 * Created by YuexingYin on 11/23/15.
 */
public class Users {
    private String userid;
    private String username;
    private String email;
    private String firstname;
    private String lastname;
    private String password;
    private String roleid;
    private String projectid;
    private String paymentid;
    private String credit;
    private String money;

    public Users(String userid, String username, String email, String firstname, String lastname, String password, String roleid,
                 String projectid, String paymentid, String credit, String money) {
        this.userid = userid;
        this.username = username;
        this.email = email;
        this.firstname = firstname;
        this.lastname = lastname;
        this.password = password;
        this.roleid = roleid;
        this.projectid = projectid;
        this.paymentid = paymentid;
        this.credit = credit;
        this.money = money;
    }

    public Users(String email, String password) {
        this.email = email;
        this.password = password;
    }

    public String getUserid() {
        return userid;
    }

    public String getUsername() {
        return username;
    }

    public String getEmail() {
        return email;
    }

    public String getFirstname() {
        return firstname;
    }

    public String getLastname() {
        return lastname;
    }

    public String getPassword() {
        return password;
    }

    public String getRoleid() {
        return roleid;
    }

    public String getProjectid() {
        return projectid;
    }

    public String getPaymentid() {
        return paymentid;
    }

    public String getCredit() {
        return credit;
    }

    public String getMoney() {
        return money;
    }
}

