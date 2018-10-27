from hrm_In_Out import *
from hrm_duration import hrm_duration
from hrm_Vex import hrm_Vex
from hrm_Rpeak import find_peak
from hrm_beats import hrm_beats
from hrm_num_beats import hrm_num_beats
from hrm_mean_hrbpm import hrm_mean_hrbpm

import os
import numpy as np

if __name__ == "__main__":
    print ('hellow world')
    dataindex = input('please type in the index of /'
                      'test data to be evaluated')
    time = input('please define the time for bpm /'
                 'calculation. ')
    raw_data = hrm_Input(dataindex)

    metrics = {
        "mean_hr_bpm": 0,
        "voltage_extremes": (),
        "duration": 0,
        "num_beats": 0,
        "beats": [],
    }
    metrics = hrm_Vex(raw_data, metrics)
    metrics = hrm_duration(raw_data, metrics)
    peak = find_peak(raw_data)
    metrics = hrm_num_beats(peak, metrics)
    metrics = hrm_beats(peak, metrics)
    metrics = hrm_mean_hrbpm(peak, metrics, time)
    print (metrics)
    hrm_Output(metrics, dataindex)
