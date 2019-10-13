# class get the data from database

# import library
import records
import pandas as pd

# database information
db = records.Database('mysql://root:ECC12345$@mydatabase.cn2pbhimebqz.ap-southeast-2.rds.amazonaws.com/food_recall')


# get recall information
def recall_table():
    row = db.query("SELECT * FROM recall ORDER BY id DESC LIMIT 10;")
    data = row.as_dict()

    return data


# get food information
def food_table():
    row = db.query("SELECT * FROM  food;")
    advanced = db.query("select * from advanced;")

    return (row,advanced)