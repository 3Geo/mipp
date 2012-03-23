#
# Extension to bin_reader.py as generating arrays
#

import numpy as np
from bin_reader import *

def read_intarray(fp, idxx):
    binarray = np.empty(idxx, int)
    for i in range(idxx):
      binarray[i] = read_int2(fp.read(2))
    return binarray

def read_int4array(fp, idxx):
    binarray = np.empty(idxx, int)
    for i in range(idxx):
      binarray[i] = read_int4(fp.read(4))
    return binarray

def read_int2array2(fp, idxx, idxy):
    binarray = np.empty((idxx, idxy), int)
    for i in range(idxx):
        for j in range(idxy):
            binarray[i][j] = read_int2(fp.read(2))
    return binarray

def read_int4array2(fp, idxx, idxy):
    binarray = np.empty((idxx, idxy), int)
    for i in range(idxx):
        for j in range(idxy):
            binarray[i][j] = read_int4(fp.read(4))
    return binarray

def read_int2array3(fp, idxx, idxy, idxz):
    binarray = np.empty((idxx, idxy, idxz), int)
    for i in range(idxx):
        for j in range(idxy):
            for z in range(idxz):
                binarray[i][j][z] = read_int2(fp.read(2))
    return binarray

def read_int4array3(fp, idxx, idxy, idxz):
    binarray = np.empty((idxx, idxy, idxz), int)
    for i in range(idxx):
        for j in range(idxy):
            for z in range(idxz):
                binarray[i][j][z] = read_int4(fp.read(4))
    return binarray

def read_chararray2(fp, idxx, idxy):
    binarray = np.empty((idxx, idxy), str)
    for i in range(idxx):
        for j in range(idxy):
            binarray[i][j] = fp.read(6)
    return binarray

