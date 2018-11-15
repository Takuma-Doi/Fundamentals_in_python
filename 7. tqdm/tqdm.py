# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 16:16:54 2018
@author: dadad

=====================================
This is the examples of 'tqdm'puckage
=====================================
"""

import time
from tqdm import tqdm

# usage 1
for i in tqdm(range(100)):
    time.sleep(0.1)

#############################
# usage 2
proc_bar = tqdm(range(100))
for i in proc_bar:
    time.sleep(0.1)
proc_bar.close()

#############################
# usage 3
proc_bar = tqdm(range(100))
for i in proc_bar:
    proc_bar.update(1)
    time.sleep(0.1)
proc_bar.close()

#############################
# usage 4
total_len = range(240)
proc_bar = tqdm(total= 100)
for i in proc_bar:
    proc_bar.update((1/total_len) * 100)
    time.sleep(0.1)
proc_bar.close()
