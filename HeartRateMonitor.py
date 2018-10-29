from hrm_findfile import *
from hrm_In_Out import *
from hrm_duration import hrm_duration
from hrm_Vex import hrm_Vex
from hrm_Rpeak import find_peak
from hrm_beats import hrm_beats
from hrm_num_beats import hrm_num_beats
from hrm_mean_hrbpm import hrm_mean_hrbpm
import logging
import os
import numpy as np

if __name__ == "__main__":
    logging.basicConfig(filename="mainlog.txt",
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    filename = input('please type in the index of test data'
                     ' to be evaluated. Enter -1 to scan all data. ')
    time = input('please define the time for bpm /'
                 'calculation. ')
    filelist = hrm_findfile(filename)
    for i in filelist:
        raw_data = hrm_Input(i)
        metrics = {
            "mean_hr_bpm": 0,
            "voltage_extremes": (),
            "duration": 0,
            "num_beats": 0,
            "beats": [],
        }
        metrics = hrm_Vex(raw_data, metrics)
        logging.info('Voltage extreme recorded')
        metrics = hrm_duration(raw_data, metrics)
        logging.info('duration recorded')
        peak = find_peak(raw_data)
        metrics = hrm_num_beats(peak, metrics)
        logging.info('beats number recorded')
        metrics = hrm_beats(peak, metrics)
        logging.info('peak time recorded')
        metrics = hrm_mean_hrbpm(peak, metrics, time)
        logging.info('mean bpm recorded')
        hrm_Output(metrics, filename)
