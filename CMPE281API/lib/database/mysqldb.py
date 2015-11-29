#!/usr/bin/python

from flaskext.mysql import MySQL
import mysql.connector

class DatabaseDriver(object):

    def __enter__(self):
        try:
            #self._conn = psycopg2.connect("dbname='secure7' user='secure7' host='localhost'")
            self._conn = mysql.connector.connect(user='leonsaber', password='8eightwing',
                              host='cmpe272.cmtinfrzsxtp.us-west-2.rds.amazonaws.com',
                              database='CMPE281')

            return self._conn
        except mysql.DatabaseError, e:
            raise e

    def __exit__(self, type, value, traceback):
        self._conn.close()