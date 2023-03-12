import os
import time
from csi import *
from datetime import datetime

os.makedirs('data/csv/', exist_ok=True)
save_dir = 'data/csv/'

act_time = {
    'Empty': ['2023-03-12 16:58:00', '2023-03-12 17:38:00'],
    'Sitting': ['2023-03-12 17:40:00', '2023-03-12 17:55:00'],
    'Walking': ['2023-03-12 17:56:30', '2023-03-12 18:06:00'],
    'Lying': ['2023-03-12 18:07:00', '2023-03-12 18:17:00'],
    'Standing': ['2023-03-12 18:18:00', '2023-03-12 18:28:00']
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