import os
from csi import *

os.makedirs('data/csv/', exist_ok=True)

save_dir = 'data/csv/'

for pcap_fname in os.listdir('data/pcap'):
    df = pcap_to_df(os.path.join('data/pcap', pcap_fname))
    csv_fname = pcap_fname.split('.')[0] + '.csv'
    df.to_csv(os.path.join(save_dir, csv_fname), index=False)
    print(f'Save {csv_fname}')
