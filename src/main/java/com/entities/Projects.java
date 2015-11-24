package com.entities;

/**
 * Created by YuexingYin on 11/23/15.
 */
public class Projects {
    private String projectid;
    private String projectname;
    private String starttime;
    private String endtime;
    private String userid;
    private String bugid;

    public Projects(String projectid, String projectname, String starttime, String endtime, String userid, String bugid) {
        this.projectid = projectid;
        this.projectname = projectname;
        this.starttime = starttime;
        this.endtime = endtime;
        this.userid = userid;
        this.bugid = bugid;
    }

    public String getProjectid() {
        return projectid;
    }

    public String getProjectname() {
        return projectname;
    }

    public String getStarttime() {
        return starttime;
    }

    public String getEndtime() {
        return endtime;
    }

    public String getUserid() {
        return userid;
    }

    public String getBugid() {
        return bugid;
    }
}

