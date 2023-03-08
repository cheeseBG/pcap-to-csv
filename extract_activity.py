import os
import date.datetime
from csi import *

act_time = {
    'Empty': ['23.03.07 14:04:00', '23.03.07 14:10:59'],
    'Sitting': ['23.03.07 14:12:00', '23.03.07 14:17:59'],
    'Walking': ['23.03.07 14:18:30', '23.03.07 14:23:59'],
    'Lying': ['23.03.07 14:25:00', '23.03.07 14:30:00'],
    'Standing': ['23.03.07 14:31:00', '23.03.07 14:36:00']
}


for pcap_fname in os.listdir('data/pcap'):
    df = pcap_to_df(os.path.join('data/pcap', pcap_fname))
    csv_fname = pcap_fname.split('.')[0] + '.csv'
    df.to_csv(os.path.join(save_dir, csv_fname), index=False)
    print(f'Save {csv_fname}')