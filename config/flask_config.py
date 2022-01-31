import os
from dotenv import load_dotenv
import psycopg2

load_dotenv(verbose=True)


class Databases():
    def __init__(self):
        self.db = psycopg2.connect(host=os.getenv('HOST'),
                                   dbname=os.getenv('DBNAME'),
                                   user=os.getenv('USER'),
                                   password=os.getenv('PWD'),
                                   port=os.getenv('PORT'))
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()
        self.cursor.close()

    def execute(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.cursor.commit()


class CRUD(Databases):
    def insertDB(self, schema, table, colum, data):
        sql = " INSERT INTO {schema}.{table}({colum}) VALUES ('{data}') ;".format(schema=schema, table=table,
                                                                                  colum=colum, data=data)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(" insert DB err ", e)

    def readDB(self, schema, table, colum):
        sql = " SELECT {colum} from {schema}.{table}".format(colum=colum, schema=schema, table=table)
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except Exception as e:
            result = (" read DB err", e)

        return result

    def updateDB(self, schema, table, colum, value, condition):
        sql = " UPDATE {schema}.{table} SET {colum}='{value}' WHERE {colum}='{condition}' ".format(schema=schema,
                                                                                                   table=table,
                                                                                                   colum=colum,
                                                                                                   value=value,
                                                                                                   condition=condition)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(" update DB err", e)

    def deleteDB(self, schema, table, condition):
        sql = " delete from {schema}.{table} where {condition} ; ".format(schema=schema, table=table,
                                                                          condition=condition)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print("delete DB err", e)