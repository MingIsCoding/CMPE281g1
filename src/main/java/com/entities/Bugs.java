package com.entities;

/**
 * Created by YuexingYin on 11/23/15.
 */
public class Bugs {
    private String bugid;
    private String bugname;
    private String buglevel;
    private Boolean bugstatus;
    private String projectid;
    private String userid;

    public Bugs(String bugid, String bugname, String buglevel, Boolean bugstatus, String projectid, String userid) {
        this.bugid = bugid;
        this.bugname = bugname;
        this.buglevel = buglevel;
        this.bugstatus = bugstatus;
        this.projectid = projectid;
        this.userid = userid;
    }

    public String getBugid() {
        return bugid;
    }

    public String getBugname() {
        return bugname;
    }

    public String getBuglevel() {
        return buglevel;
    }

    public Boolean getBugstatus() {
        return bugstatus;
    }

    public String getProjectid() {
        return projectid;
    }

    public String getUserid() {
        return userid;
    }
}
