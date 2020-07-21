import pandas as pd
import numpy as np

df = pd.read_csv(r'/Users/colinmason/Desktop/yorglab/testwork/masters/spons_mastersheet_UPDATE3.csv')

df['log_tau_1'] = np.log(df['tau'] + 3)


df.to_csv(r'/Users/colinmason/Desktop/yorglab/testwork/masters/spons_master_log_UPDATE3.csv')