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

1. The program will ask for a number to track the raw data file to be read. 
2. The program then asks for a time used to calculate mean beat per minutes.
3. _hrm_Input_ function is called to read raw data into a numpy array
4. _hrm_

