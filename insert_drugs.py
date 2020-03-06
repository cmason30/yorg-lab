import psycopg2
import pandas.io.sql as sqlio



def insert_drug_sql(mouse_folder):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="",
                                      host="localhost",
                                      port="",
                                      database="mouse_practice")
        cursor = connection.cursor()
        sql_sel_query = "SELECT * FROM experiments WHERE mouse_id = {}".format(mouse_folder)
        dat_table = sqlio.read_sql_query(sql_sel_query, connection)
        cursor.close()
        connection.close()
        return dat_table

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL function1", error)


def add_drug_conc(file_number):

    flatten = lambda l: [item for sublist in l for item in sublist]
    df = insert_drug_sql(file_number)

    print(df['experiment_file_name'])

    n = int(input('How many drugs are there, including control? '))

    name_lst = df['experiment_file_name']

    final_lst_names = []
    final_lst_conc = []
    for i in range(n):
        code = input('What is the code? ')
        name = input('What is the name? ')
        conc = input('What is the concentration? ')

        names_lst = []
        conc_lst = []
        for file in name_lst:

            if file.find(code) > -1:
                names_lst.append(name)
                conc_lst.append(conc)

        final_lst_names.append(names_lst)
        final_lst_conc.append(conc_lst)

    final_lst_names = flatten(final_lst_names)
    final_lst_conc = flatten(final_lst_conc)

    df['drug_applied'] = final_lst_names
    df['drug_concentration'] = final_lst_conc

    print(df)
    return df


def insert_drugs(file_number):
    df1 = add_drug_conc(file_number)
    duple_applied = df1["drug_applied"].values.tolist()
    duple_conc = df1["drug_concentration"].values.tolist()
    duple_exp = df1["exp_id"].values.tolist()
    zipped_vals = list(zip(duple_applied, duple_conc, duple_exp))
    try:
        connection1 = psycopg2.connect(user="postgres",
                                      password="stefflab",
                                      host="localhost",
                                      port="5432",
                                      database="mouse_practice")
        cursor1 = connection1.cursor()
        for vals in zipped_vals:
            sql_ins_query = """ UPDATE experiments SET drug_applied= %s, drug_concentration = %s WHERE exp_id = %s"""
            cursor1.execute(sql_ins_query, vals)
        connection1.commit()
        cursor1.close()
        connection1.close()

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL function 2", error)

