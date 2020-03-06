import os
from sqlalchemy import create_engine
import pandas as pd
import psycopg2
from psycopg2.extensions import register_adapter
from cocaine_funcs.brn_file_reader import read_brn_JYorg
from cocaine_funcs import insert_functions
import numpy as np

psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)


# Makes a dictionary of files and associated pkeys
def listed_paths(which_table="mouses"):
    list_files = []
    engine1 = create_engine("postgresql://postgres:stefflab@localhost:5432/mouse_practice")
    df = pd.read_sql_table(which_table, engine1)
    filenames = list(df["filename"])
    p_keys = df["mouse_id"].values.astype(int)
    p_keys_file_dict = dict(zip(filenames, p_keys))
    # print(p_keys_file_dict)
    for keys, values in p_keys_file_dict.items():
        file_string = "/Users/cmason/Desktop/yorglab/ext_cocaine/ext_cocaine/{}".format(keys)

        list_files.append(file_string)
        engine1.dispose()
    return dict(zip(list_files, p_keys))


# Does all BRN extractions for one file
def brn_file_iterations(trun_tbl=False):
    new_list_files = listed_paths()
    engine = create_engine("postgresql://postgres:stefflab@localhost:5432/mouse_practice")
    list_keys_exp_dict = []
    list_vals_int_dict = []

    if trun_tbl:
        insert_functions.trun_restart_identity()
    print(new_list_files)
    for paths, p_keys_mouse in new_list_files.items():
        listed_brns = sorted(os.listdir(paths))
        print(listed_brns)
        for brn_it in listed_brns:

            if brn_it.find(".brn") == -1:
                pass
            elif brn_it.find(".brn") > -1:
                read_file = read_brn_JYorg(paths+"/"+brn_it)
                df_exp = read_file[0]
                list_values = df_exp.loc[1].values.tolist()
                primary_key_exp = insert_functions.experiment_data_insert(list_values)

                df_exp2 = pd.read_sql_table("experiments", engine)
                p_k_val = df_exp2["exp_id"].iloc[-1]
                insert_functions.add_fks(mouse_id_val=p_keys_mouse, exp_val=p_k_val)

                df_ints = read_file[1]
                ms_list = df_ints["Time (s)"].tolist()
                curr_list = df_ints["Current (nA)"].tolist()
                tupled_list = list(zip(ms_list, curr_list))
                primary_key_int = insert_functions.intervals_data_insert(tupled_list)

                insert_functions.add_fks_ints(primary_key_exp, primary_key_int)

    engine.dispose()


brn_file_iterations(True)
