import pandas as pd
import numpy as np

df = pd.read_csv(r'/Users/colinmason/Desktop/yorglab/coding work/spons_mastersheet_v2.csv')

df['log_tau'] = np.log(df['tau'])

df.to_csv(r'/Users/colinmason/Desktop/yorglab/testwork/masters/spons_master_log2.csv')