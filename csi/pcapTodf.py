import importlib
import csi.config as config
import pandas as pd
import numpy as np

decoder = importlib.import_module(f'csi.decoders.{config.decoder}') # This is also an import


def pcap_to_df(filename, amp=False, del_null=False, add_MAC=True, add_time=True):
    nulls = {
        20: [x + 32 for x in [
            -32, -31, -30, -29,
            31, 30, 29, 0
        ]],

        40: [x + 64 for x in [
            -64, -63, -62, -61, -60, -59, -1,
            63, 62, 61, 60, 59, 1, 0
        ]],

        80: [x + 128 for x in [
            -128, -127, -126, -125, -124, -123, -1,
            127, 126, 125, 124, 123, 1, 0
        ]],

        160: [x + 256 for x in [
            -256, -255, -254, -253, -252, -251, -129, -128, -127, -5, -4, -3, -2, -1,
            255, 254, 253, 252, 251, 129, 128, 127, 5, 4, 3, 3, 1, 0
        ]]
    }

    # Read pcap file and create dataframe
    try:
        csi_samples = decoder.read_pcap(filename)
    except FileNotFoundError:
        print(f'File {filename} not found.')
        exit(-1)

    bw = csi_samples.bandwidth

    num_20MHz_sc = 64
    num_sc = num_20MHz_sc * bw//20  # number of subcarriers

    # Create csi data frame
    colums = ['_' + str(i) for i in range(0, num_sc)]

    if amp is True:
        csi_df = pd.DataFrame(np.abs(csi_samples.get_all_csi()), columns=colums)  # Get csi amplitude dataframe
    else:
        csi_df = pd.DataFrame(csi_samples.get_all_csi(), columns=colums)  # Get I/Q complex num dataframe

    if del_null is True:
        csi_df = csi_df[csi_df.columns.difference(nulls[bw])]

    if add_time is True:
        pkttimes = csi_samples.get_times()
        csi_df.insert(0, 'time', pkttimes)

    if add_MAC is True:
        mac_list = [csi_samples.get_mac(i).hex() for i in range(0, csi_samples.nsamples)]
        csi_df.insert(0, 'mac', mac_list)

    return csi_df


if __name__ == "__main__":
    filename = "../pcap/Empty_Ex_Home_13.pcap"
    df = pcap_to_df(filename)

    print(df.iloc[:242])
    print(np.array(df).shape)
