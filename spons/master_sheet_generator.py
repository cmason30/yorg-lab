import pandas as pd
import numpy as np


# df_path = df_path.columns[0]
df = pd.read_excel(r'/Users/colinmason/Desktop/yorglab/spon_excel/CoreCocEticSpons.xlsx')
#print(df.columns[0])


def find_drug_applied(row):
    if row['experiment'].find('00') > -1:
        return 'control'
    elif row['experiment'].find('01') > -1:
        return '30uM4AP'
    elif row['experiment'].find('02') > -1:
        return '3uMCoc'
    elif row['experiment'].find('03') > -1:
        return '1uMEtic'
    else:
        return 'NaN'


def find_sex(row):
    if row['sheetname'].find('Male') > -1:
        return 'male'
    elif row['sheetname'].find('Female') > -1:
        return 'female'
    else:
        return 'NaN'


def fem_brain_region(row):
    if row['sheetname'].find('DS') > -1 or row['sheetname'].find('ds') > -1:
        return 'DS'
    elif row['sheetname'].find('shell') > -1:
        return 'Shell'
    elif row['sheetname'].find('core') > -1:
        return 'Core'
    else:
        return 'NaN'


def master_sheet_maker(brain_region, excel_file, region_file, fem=False):
    master_sheet = []
    xls = pd.ExcelFile(excel_file)
    sheets = xls.sheet_names
    for sheet in sheets:
        if sheet.find('Avg') > -1:
            continue
        elif sheet.find('11.') > -1:
            continue
        else:
            df_path = pd.read_excel(excel_file, sheet_name=sheet).columns[0]
            df_sheet = pd.read_excel(excel_file, sheet_name=sheet, header=1).iloc[:, 0:9]
            print(df_sheet.columns)
            true_col = ['experiment', 'File #', 'Time', 'tau', 'R2', 'Amplitude',
                        'Time in Exp. (Sec)', 'Frequency', 'Time (min)']
            if true_col != list(df_sheet):
                print(sheet, region_file)
            df_sheet['drug_applied'] = df_sheet.apply(find_drug_applied, axis=1)
            df_sheet.insert(8, 'sheetname', sheet)
            df_sheet.insert(8, 'file_path', df_path)
            df_sheet.insert(8, 'region_file', region_file)
            if not fem:
                df_sheet.insert(8, 'region_name', brain_region)
            elif fem:
                df_sheet['region_name'] = df_sheet.apply(fem_brain_region, axis=1)

            df_sheet['sex'] = df_sheet.apply(find_sex, axis=1)
            master_sheet.append(df_sheet)

    master_sheet_comb = pd.concat(master_sheet)
    return master_sheet_comb


df2 = master_sheet_maker(brain_region='Core',excel_file='/Users/colinmason/Desktop/yorglab/spon_excel/CoreCocEticSpons.xlsx',region_file='CoreCocEticSpons')
df3 = master_sheet_maker(brain_region='DS', excel_file=r'/Users/colinmason/Desktop/yorglab/spon_excel/DSCocEticSpons kyle.xlsx', region_file='DSCocEticSpons')
df4 = master_sheet_maker(brain_region='Shell', excel_file=r'/Users/colinmason/Desktop/yorglab/spon_excel/ShellCocEticSpons.xlsx', region_file='ShellCocEticSpons')
df5 = master_sheet_maker(brain_region='NaN', excel_file=r'/Users/colinmason/Desktop/yorglab/spon_excel/female4AP_WIP.xlsx', region_file='Female4AP', fem=True)

master_sheet = [df2, df3, df4, df5]

df_final = pd.concat(master_sheet)

df_final.to_csv(r'/Users/colinmason/Desktop/yorglab/testwork/mastersheet9.csv')



df1 = ['g', 'f', 'c']
df2 = ['g', 'b', 'c']
print(df2 != df1)

# output of the function is a master sheet of Core





