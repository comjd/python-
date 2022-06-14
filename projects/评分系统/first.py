#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022 2022/5/25 下午2:06
# @Author : tyler
# @File : first.py
# @Project : projects

import pymysql


class MySQLHelper:
    myVersion = 0.1

    def __init__(self, host, user, password, database, port=3306, charset="utf8"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.port = port

        try:
            self.conn = pymysql.connect(host=self.host, user=self.user, passwd=self.password, database=self.database,
                                        port=self.port, charset=self.charset)
            # self.conn.set_character_set(self.charset)
            self.cursor = self.conn.cursor()
        except pymysql.Error as e:
            print('MySql Error : %d %s' % (e.args[0], e.args[1]))

    # def setDB(self,db):
    # try:
    #       self.conn.select_db(db)
    # except pymysql.Error as e:
    #   print ('MySql Error : %d %s' %(e.args[0],e.args[1]))

    def query(self, sql):
        try:
            rows = self.cursor.execute(sql)
            return rows;
        except pymysql.Error as e:
            print('MySql Error: %s SQL: %s' % (e, sql))

    def queryOnlyRow(self, sql):
        try:
            self.query(sql)
            result = self.cursor.fetchone()
            desc = self.cursor.description
            row = {}
            for i in range(0, len(result)):
                row[desc[i][0]] = result[i]
            return row;
        except pymysql.Error as e:
            print('MySql Error: %s SQL: %s' % (e, sql))

    def queryAll(self, sql):
        try:
            self.query(sql)
            result = self.cursor.fetchall()
            desc = self.cursor.description
            rows = []
            for cloumn in result:
                row = {}
                for i in range(0, len(cloumn)):
                    row[desc[i][0]] = cloumn[i]
                rows.append(row)
            return rows
        except pymysql.Error as e:
            print('MySql Error: %s SQL: %s' % (e, sql))

    def insert(self, tableName, pData):
        try:
            newData = {}
            for key in pData:
                newData[key] = "'" + pData[key] + "'"
            key = ','.join(newData.keys())
            value = ','.join(newData.values())
            sql = "insert into " + tableName + "(" + key + ") values(" + value + ")"
            self.query("set names 'utf8'")
            self.query(sql)
            self.commit()
        except pymysql.Error as e:
            self.conn.rollback()
            print('MySql Error: %s %s' % (e.args[0], e.args[1]))
        finally:
            self.close()

    def update(self, tableName, pData, whereData):
        try:
            newData = []
            keys = pData.keys()
            for i in keys:
                item = "%s=%s" % (i, "'" + pData[i] + "'")
                newData.append(item)
            items = ','.join(newData)
            newData2 = []
            keys = whereData.keys()
            for i in keys:
                item = "%s=%s" % (i, "'" + whereData[i] + "'")
                newData2.append(item)
            whereItems = " AND ".join(newData2)
            sql = "update " + tableName + " set " + items + " where " + whereItems
            self.query("set names 'utf8'")
            self.query(sql)
            self.commit()
        except pymysql.Error as e:
            self.conn.rollback()
            print('MySql Error: %s %s' % (e.args[0], e.args[1]))
        finally:
            self.close()

    def getLastInsertRowId(self):
        return self.cursor.lastrowid

    def getRowCount(self):
        return self.cursor.rowcount

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()


# import pymysql
#
#
# class MySqlHelper:
#     conn = pymysql.connect(host='192.168.1.121', user='root', password='lensyn@Admin.', port=3306, db='remarks',
#                            charset='utf8')


if __name__ == '__main__':

    helper = MySQLHelper("192.168.1.121", "root", "lensyn@Admin.", "remarks")
    # helper.setDB("employee")
    sql = "select * from "
    rows = helper.queryAll(sql)
    for row in rows:
        print(row['id'], row['account'])

    # dataSource={"name":"汤姆克路斯".decode("gbk").encode("utf-8"),"birthday":"1992-03-12"}
    # helper.insert("users", dataSource)
    # print helper.getLastInsertRowId()

    # pData={"birthday":"2005-05-05 18:32:23"}
    # whereData={"name":"Jack Tang"}
    # helper.update("users", pData, whereData)

