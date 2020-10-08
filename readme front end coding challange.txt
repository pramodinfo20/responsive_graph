Data Format HDF5: 
https://en.wikipedia.org/wiki/Hierarchical_Data_Format
HDF5 format is a hierarchical data structure, consists mainly of the following components: attributes, groups and data sets. Attributes are used for storing meta-data. Groups and data sets could be considered as folders and files, respectively, in classical file system.

Structure of IRUBIS HDF5 files Attributes:
* wavenumbers, array: Wx1, with W - number of data samples
From here you can extract wavenumbers, which are commonly used as x-axis (horizontal) for plotting spectra.

Groups:
* internal
* external

The internal group has the following structure:
** glucose
** measurement
** time

time - integers, size Nx1, with N - number of data samples, consists of UNIX timestamps, at which a spectrum was measured.

measurement - floats, size NxW, with N - number of data samples, W - number of wavenumber, each row is a spectrum.

glucose - floats, size Nx1, with N - number of data samples, consists of glucose values that were calculated based on corresponding measurement spectra.


Coding challenge:

We like to see two graphs. One should contain glucose over time and the second graph should show the corresponding measurement. Please focus on data visualization and the understanding of the data. The backend of this challenge should be Python based. The data has to be extracted directly from the HDF5 file without copy&paste into the code. 
