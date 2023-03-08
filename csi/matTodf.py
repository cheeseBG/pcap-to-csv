from scipy import io
import pandas as pd
import numpy as np


def mat_to_df(f_path):

    colums = ['_' + str(i) for i in range(0, 242)]

    mat_file = io.loadmat(f_path)
    csi_df = pd.DataFrame(mat_file['cfm_data'], columns=colums)  # Get I/Q complex num dataframe
    d_len = np.arange(0, len(csi_df), 1)
    csi_df.insert(0, 'time', d_len)
    csi_df.insert(0, 'mac', d_len)

    return csi_df


if __name__ == "__main__":
    filename = "../data/mat/test_A2/empty/pca_mat_0.mat"
    df = mat_to_df(filename)

    print(df.iloc[:242])
    print(np.array(df).shape)

