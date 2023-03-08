import os
import time
from csi import *
from datetime import datetime

save_dir = 'data/csv/'

act_time = {
    'Empty': ['2023-03-07 14:04:00', '2023-03-07 14:11:00'],
    'Sitting': ['2023-03-07 14:12:00', '2023-03-07 14:18:00'],
    'Walking': ['2023-03-07 14:18:30', '2023-03-07 14:24:00'],
    'Lying': ['2023-03-07 14:25:00', '2023-03-07 14:30:00'],
    'Standing': ['2023-03-07 14:31:00', '2023-03-07 14:36:00']
}


pcap_fname = os.listdir('data/pcap')[0]

df = pcap_to_df(os.path.join('data/pcap', pcap_fname))

for item in act_time:
    start_time, end_time = act_time[item]
    start_time = time.mktime(datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S').timetuple())
    end_time = time.mktime(datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S').timetuple())

    act_df = df[(df['time'] >= start_time) & (df['time'] < end_time)]

    csv_fname = item + '_' + pcap_fname.split('.')[0] + '.csv'
    act_df.to_csv(os.path.join(save_dir, csv_fname), index=False)
    print(f'Save {csv_fname}')