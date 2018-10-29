# bme590hrm
This repository contains the files for BME590-06 Heart Rate Monitor Project

Author: Zengtian Deng

Version 1.0.0 

License: GNU General Public License v3.0

## Contents
This repository includes:
* A folder called _Test_data_ that stores all ECG data
* requirement.txt that include all packages required for the project
* .travis.yml file that handle unittest for pull request
* several python files used to create the Heart Rate Monitor Program

## Workflow
So far, the program requires the following setup in order to function properly:
* raw data needs to be put in a folder called _Test_data_;
* The input file name should be in the format "test_datan.csv", where n is a number 
that differentiate raw data from each other.

The whole program functions by executing file _HeartRateMonitor.py_. The workflow of the program is:

1. The program will ask a for file name to track the raw data file to be read.
enter -1 to process all possible file in _Test_data_ folder. The user can input
the file name with or without extension 
2. The program then asks for a time used to calculate mean beat per minutes. If
the input is not a valid number, the program will ask for another input of number.
3. _hrm_checkinput_ is called to verify the validity of the data file to be processed
4. _hrm_Input_ is called to read raw data into a numpy array. The metrics dictionary
is then created by the main program before actuall processing begins
5. _hrm_Vex_ is called to store min and max voltage in the ECG script
6. _hrm_duration_ is called to store the duration of the ECG script
7. _find_peak_ is called to find R peak in ECG script. The function will return a list
with element contains the voltage value and corresponding time of each detected R peak
8._hrm_num_beats_ is called to calculate total number of beats in ECG data
9._hrm_beats_ is called to calculate the time of each beats' R peak
10._hrm_mean_hrbpm is called to calculate bpm either using the provided time or the actual duration
of the program if the user defined time is larger than the duration of the ECG script

