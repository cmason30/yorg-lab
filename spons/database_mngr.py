import pandas as pd
import sqlalchemy as sql
import psycopg2 as pg

df = pd.read_csv(r'/Users/colinmason/Desktop/yorglab/testwork/masters/spons_master_log_UPDATE3.csv')

engine = sql.create_engine('postgresql://postgres:Spillermcvp15@localhost:5432/postgres')

df.to_sql('spons_actuals', engine)

