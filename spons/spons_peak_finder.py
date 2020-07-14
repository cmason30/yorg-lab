from full_processing import get_dataframe
import pandas as pd
from master_sheet_generator2 import master_sheet_maker
import os


def absoluteFilePaths(region_int):
   directory = r'/Users/colinmason/Desktop/yorglab/spon_excel/demon files/RegionalCocEticSpons/{region}'.format(region=region_int)
   for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           yield os.path.abspath(os.path.join(dirpath, f))


def preds_generator():
    df_list = []
    df2 = master_sheet_maker(brain_region='Core',excel_file='/Users/colinmason/Desktop/yorglab/spon_excel/CoreCocEticSpons2.xlsx',region_file='CoreCocEticSpons')
    listed_paths = df2.file_path.unique().tolist()
    # df_initial = pd.DataFrame(
    #                          columns= ['Filename',
    #                          "Start Time",
    #                          'Rise Time',
    #                          'Decay Time',
    #                          'Oxidation Index',
    #                          'R Squared Voltammogram',
    #                          'Signal to Noise Ratio',
    #                          'Peak Height',
    #                          'Area Under the Curve'])
    for path in listed_paths:
        try:
            print('NICE', path)
            preds_df = get_dataframe(path)
            preds_df['tdms_path'] = path
            df_list.append(preds_df)
        except KeyError:
            print('NOOO', path)
            continue

    preds_final = pd.concat(df_list)

    return preds_final
