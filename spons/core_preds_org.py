import pandas as pd
import numpy as np

df_actuals = pd.read_csv(r'/Users/colinmason/Desktop/yorglab/testwork/relationals/core_files2.csv')
df_preds = pd.read_csv(r'/Users/colinmason/Desktop/yorglab/testwork/relationals/preds_core2.csv')


def dict_maker(df):
    sub_set = df[['time_val', 'pk_id']].query("time_val != 'nan'")
    my_dict = dict(zip(sub_set.time_val, sub_set.pk_id))
    return my_dict


def time_unpacker(row):
    numb = row['start_end'].replace('(', '').replace(',','').replace(')','')
    digits = [float(words) for words in numb.split() if words.isdigit()]
    digits = [round(i/10, 1) for i in digits]
    return digits




# pred_sorter: key is time value of actual
# we need to subset the preds_df bassed on pk_id (value) and apply whichever times that are in the range of tuples presented
def pred_sorter(actual, prediction_df):
    pred = prediction_df
    dictionary_time_vals = dict_maker(actual)
    pred.insert(8,'marked', 0)
    pred['start_end'] = pred.apply(time_unpacker, axis=1)
    pred['start'] = pred.start_end.apply(lambda x: x[0])
    pred['end'] = pred.start_end.apply(lambda x: x[1])
    for key, value in dictionary_time_vals.items():
        subset_df = pred[['start','end','oxidation_index','marked','pk_id']].query("pk_id == {id}".format(id=value))
        subset_df = subset_df[(subset_df['start'] <= key) & (key <= subset_df['end'])]
        print(key)
        print(subset_df)

    return pred










# df_preds['start_end'] = df_preds.apply(time_unpacker, axis=1)
# df_preds['start'] = df_preds.start_end.apply(lambda x: x[0])
# df_preds['end'] = df_preds.start_end.apply(lambda x: x[1])
# print(df_preds['start'], df_preds['end'])

# f = pred_sorter()
#

z = pred_sorter(df_actuals, df_preds)











