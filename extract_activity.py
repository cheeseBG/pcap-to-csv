import os
import time
from csi import *
from datetime import datetime

os.makedirs('data/csv/', exist_ok=True)
save_dir = 'data/csv/'

act_time = {
    'empty': ['2023-06-05 23:35:00', '2023-06-06 12:05:00'],
    'sit': ['2023-06-06 12:10:00', '2023-06-06 12:25:00'],
    'walk': ['2023-06-06 12:51:00', '2023-06-06 13:01:00'],
    'stand': ['2023-06-06 12:37:00', '2023-06-06 12:47:00']
}


pcap_fname = os.listdir('data/pcap')[0]

df = pcap_to_df(os.path.join('data/pcap', pcap_fname), amp=False, add_MAC=True, add_time=True)

for item in act_time:
    start_time, end_time = act_time[item]
    start_time = time.mktime(datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S').timetuple())
    end_time = time.mktime(datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S').timetuple())

    act_df = df[(df['time'] >= start_time) & (df['time'] < end_time)]

    csv_fname = item + '_' + pcap_fname.split('.')[0] + '.csv'
    act_df.to_csv(os.path.join(save_dir, csv_fname), index=False)
    print(f'Save {csv_fname}')