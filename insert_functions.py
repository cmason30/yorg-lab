import psycopg2
import os



def experiment_data_insert(tuple_unpack):
                # (Original_File_Path, Experiment_File_Name, r2, K, Tau, Half_Life, Selected_Area, T20, T80, Half_Width, Peak_Height_nA, DAc, Rise_Time, Rising_Slope):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="stefflab",
                                      host="localhost",
                                      port="5432",
                                      database="mouse_practice")
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO experiments (original_file, experiment_file_name, r2, k_vals, tau_vals, half_life_vals, selected_area, t20, t80, half_width, peak_height, dac_vals, rise_time, rising_slope) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING exp_id;"""
        record_to_insert = tuple_unpack
        cursor.execute(postgres_insert_query, record_to_insert)
        return_id = cursor.fetchall()[0]

        connection.commit()
        cursor.close()
        connection.close()
        return return_id[0]

    except (Exception, psycopg2.Error) as error:
        if connection:
            print("Failed to insert record into table", error)


def mouse_files_dump(drug, file_name):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="stefflab",
                                      host="localhost",
                                      port="5432",
                                      database="mouse_practice")
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO mouses (category, filename) VALUES (%s,%s)"""
        record_to_insert = (drug, file_name)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        cursor.close()
        connection.close()
    except (Exception, psycopg2.Error) as error :
        print(error)


def intervals_data_insert(data):
    try:
        connection = psycopg2.connect(user="postgres",
                                       password="stefflab",
                                       host="localhost",
                                       port="5432",
                                       database="mouse_practice")
        cursor = connection.cursor()
        listed_keys = []
        for d in data:

            postgres_insert_query = """ INSERT INTO intervals (time_vals, current_na_vals) VALUES (%s,%s) RETURNING int_id"""
            record_to_insert = d
            cursor.execute(postgres_insert_query, record_to_insert)
            prim_key = cursor.fetchall()[0]

            listed_keys.append(prim_key[0])

        connection.commit()

        cursor.close()
        connection.close()
        return(listed_keys)
       # print (count, "Record inserted successfully into table")

    except (Exception, psycopg2.Error) as error:
        if(connection):
            print("ERROR", error)


def select_mouses():
    try:
        connection = psycopg2.connect(user="postgres",
                                          password="stefflab",
                                          host="localhost",
                                          port="5432",
                                          database="mouse_practice")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select filename from mouses"

        cursor.execute(postgreSQL_select_Query)
        print("Selecting rows from mobile table using cursor.fetchall")
        mobile_records = cursor.fetchall()

        print(mobile_records)


    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            # print("PostgreSQL connection is closed")


def add_fks(mouse_id_val, exp_val):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="stefflab",
                                      host="localhost",
                                      port="5432",
                                      database="mouse_practice")
        cursor = connection.cursor()
        sql_update_query = """Update experiments set mouse_id = %s where exp_id = %s"""
        cursor.execute(sql_update_query, (mouse_id_val, exp_val))
        connection.commit()
        cursor.close()
        connection.close()
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)


def add_fks_ints(exp_id_val, pkeys):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="stefflab",
                                      host="localhost",
                                      port="5432",
                                      database="mouse_practice")
        cursor = connection.cursor()
        for int_val in pkeys:
            sql_update_query = """Update intervals set exp_id = %s where int_id = %s"""
            cursor.execute(sql_update_query, (exp_id_val, int_val))
        connection.commit()
        cursor.close()
        connection.close()
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)


def trun_restart_identity():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="stefflab",
                                      host="localhost",
                                      port="5432",
                                      database="mouse_practice")
        cursor = connection.cursor()

        postgres_insert_query = """ TRUNCATE table experiments, intervals RESTART IDENTITY"""
        cursor.execute(postgres_insert_query)
        connection.commit()
        cursor.close()
        connection.close()
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
