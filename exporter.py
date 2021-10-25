import pandas as pd
import argparse as ap
import psycopg2


parser = ap.ArgumentParser()
parser.add_argument("--f", default="param.csv", help="This is the file with parameters. It must be defined. Defalt name: param.csv")
args = parser.parse_args()
f = args.f

df1 = pd.read_csv(f, delimiter = ';') 
i = 0
while i < len(df1):
    conn = psycopg2.connect(dbname=df1.iat[i, 1] , user=df1.iat[i, 2], password=df1.iat[i, 3], host=df1.iat[i, 4])
    dfbd = pd.read_sql(df1.iat[i, 5], conn)
    table_name = df1.iat[i, 0]
    dfbd.to_excel(str(table_name) + '.xlsx' , startcol = -1)
    conn.close()
    i = i+1
