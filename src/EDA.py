# -*- coding: utf-8 -*-
# @Author: Yulin Liu
# @Date:   2018-11-01 20:26:55
# @Last Modified by:   Yulin Liu
# @Last Modified time: 2018-11-01 21:15:47

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import gzip

class ExploreData:
    def __init__(self, 
                 file_in, 
                 n_rows = 200000):
        self.file_in = file_in
        self.n_rows = n_rows

        self.dataset = self._read_traj_nrows()

    def _read_traj_nrows(self):
        dataset = pd.read_csv(self.file_in, nrows = self.n_rows, header = None, names=['driver_id', 'order_id', 'time', 'lon', 'lat'])
        return dataset

    def visual_traj(self, dataset):
        plt.figure(figsize=(16, 12))
        plt.scatter(dataset.lon.values, dataset.lat.values, s = 0.1)
        lon_interest = [108.9375, 108.93645, 108.93645, 108.9375]
        lat_interest = [34.248, 34.248, 34.241, 34.241]
        plt.scatter(lon_interest, lat_interest, s = 5, zorder = 10, c = 'r')
        plt.show()
        return

"""
Example use
exp_data = ExploreData('../data/6a2b11c93bd64aed9a06b3b9875008db.tar.gz')
exp_data.visual_traj(exp_data.dataset)
"""
# exp_data = ExploreData('../data/6a2b11c93bd64aed9a06b3b9875008db.tar.gz', 5000000)
# exp_data.dataset.to_csv('subsamples', index = False)
# exp_data.visual_traj(exp_data.dataset)
