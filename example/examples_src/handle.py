import pandas as pd
from sys import argv

filename = argv[1]
name = filename.splite('.')[0]

df = pd.read_csv(filename, header=None)

def cv_time(mytime):
    mytime = str(mytime).splite('.')[0]
    return mytime

df[0] = df[0].apply(cv_time)
df[0] = pd.to_datetime(df[0], format="%Y-%m-%dD%H:%M:%S")
ts = df.set_index(0)
ts_minute = ts.to_period('Min')
ts_price = ts_minute.loc[:, [4]]
ts_h = ts_price.groupby(0).max()
ts_l = ts_price.groupby(0).min()
ts_o = ts_price.groupby(0).first()
ts_c = ts_price.groupby(0).last()
ts_price_done = ts_h
ts_price_done.rename(columns={4:'high'}, inplace=True)
ts_price_done['low'] = ts_l[4]
ts_price_done['open'] = ts_o[4]
ts_price_done['close'] = ts_c[4]
ts_price_done.to_csv(name + '_price.csv')