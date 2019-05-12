import pandas as pd
from sys import argv

filename = argv[1]
output_dir = argv[2]
headers = ['timestamp','symbol','side','size','price','tickDirection','trdMatchID','grossValue','homeNotional','foreignNotional']

df = pd.read_csv(filename, header=None)
df.columns = headers
df = df.set_index('timestamp')
df_sym_all = df['symbol']
df_sym_dup = df_sym_all.drop_duplicates()

for sym in df_sym_dup:
    print('handling', sym)
    df_sym = df[df['symbol'] == sym]
    df_sym = pd.DataFrame(df_sym, columns=['price'])
    output_name = output_dir + '/' + sym + '.csv'
    df_sym.to_csv(output_name, mode='a')

