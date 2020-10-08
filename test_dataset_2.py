#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import h5py
import matplotlib.pyplot as plt

with h5py.File('test_dataset_2.hdf5', 'r') as hf:
    ls = list(hf.items())
    print ('List of datasets in this file: \n', ls)
    data = hf.get('internal')
    data_items = list(data.items())
    print ('items of internal: \n', data_items)
    time = np.array(data.get('time'))
    print (time.shape)
    glucose = np.array(data.get('glucose'))
    print (glucose.shape)
    measurement = np.array(data.get('measurement'))
    print (measurement.shape)
    reference = np.array(data.get('reference'))

    (fig, axs) = plt.subplots(2)

    axs[0].set_xlabel('Time')
    axs[0].set_ylabel('Glucose')
    axs[0].plot(time, glucose)
    axs[1].set_xlabel('Time')
    axs[1].set_ylabel('Measurement')

    def onclick(event):
        idx = (np.abs(time - event.xdata)).argmin()
        axs[1].cla()
        axs[1].set_xlabel('')
        axs[1].set_ylabel('Measurement')
        axs[1].plot(measurement[idx])
        fig.canvas.draw()


    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()


			