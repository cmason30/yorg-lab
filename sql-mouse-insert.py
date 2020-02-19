import psycopg2
import os

def mouse_files_dump(drug, file_name):
    try:
       connection = psycopg2.connect(user="xx",
                                      password="xx",
                                      host="xx",
                                      port="xx",
                                      database="xx")
       cursor = connection.cursor()

       postgres_insert_query = """ INSERT INTO mouses (category, filename) VALUES (%s,%s)"""
       record_to_insert = (drug, file_name)
       cursor.execute(postgres_insert_query, record_to_insert)

       connection.commit()
       count = cursor.rowcount
       print (count, "Record inserted successfully into table")

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into mobile table", error)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


# mouse_files_dump()

x = os.listdir(r"/Users/cmason/Desktop/yorglab/test_loop")


for mice in x:
    if mice == ".DS_Store":
        pass
    else:
        mouse_files_dump(drug="Cocaine", file_name=mice)
