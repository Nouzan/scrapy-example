import pandas as pd
from sys import argv

def handle(filename):
    name = filename.split('.')[0]

    df = pd.read_csv(filename)

    def cv_time(mytime):
        mytime = str(mytime).split('.')[0]
        return mytime

    df['timestamp'] = df['timestamp'].apply(cv_time)
    df['timestamp'] = pd.to_datetime(df['timestamp'], format="%Y-%m-%dD%H:%M:%S")
    ts = df.set_index('timestamp')
    ts_minute = ts.to_period('Min')
    ts_price = ts_minute.loc[:, ['price']]
    ts_h = ts_price.groupby('timestamp').max()
    ts_l = ts_price.groupby('timestamp').min()
    ts_o = ts_price.groupby('timestamp').first()
    ts_c = ts_price.groupby('timestamp').last()
    ts_price_done = ts_h
    ts_price_done.rename(columns={'price':'high'}, inplace=True)
    ts_price_done['low'] = ts_l['price']
    ts_price_done['open'] = ts_o['price']
    ts_price_done['close'] = ts_c['price']
    ts_price_done.to_csv(name + '_price.csv')

if __name__ == '__main__':
    filenames = argv[1:]

    for filename in filenames:
        print('handling', filename)
        handle(filename)