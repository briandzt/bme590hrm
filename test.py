import numpy as np
import sys
import os
import glob
import warnings
from hrm_checkinput import hrm_checkinput


def check_num(numstring):
    try:
        float(numstring)
        return True
    except ValueError:
        return False
x = np.array([[1, 1, 1, 1, 1], [1, 2, 3, 4, 5]])
print(np.histogram(x[0]))
x = '  5,'

print(check_num(x))
# y = x[1][0:-1]
# print (y)

# script_dir = os.path.dirname(__file__)
# real_path = 'Test_data'
# act_path = os.path.join(script_dir, real_path)
# os.chdir(act_path)
# filelist = []
# for file in glob.glob("*.csv"):
#     if (hrm_checkinput(os.path.join(act_path,file))):
#         filelist.append(os.path.join(act_path,file))

#
# my_data = np.array([[2,3],[2,3]])
# with open(act_path) as f:
#     my_data = np.genfromtxt(act_path, delimiter=',')
# wronginput = []
# previous_size = my_data.size
# for i,x in enumerate(my_data):
#     if np.isnan(x[0]) or np.isnan(x[1]):
#         wronginput.append(i)
# my_data = np.delete(my_data,wronginput,0)
# if my_data.size == 0:
#     raise ValueError("The selected file has no valid data entry")
# if my_data.size < (previous_size/2):
#     warnings.warn('Over 50% of the entries within the data is unreadable')
# print (my_data.size)


# script_dir = os.path.dirname(__file__)
# real_path = 'Test_data/test_data' + str(1) + '.csv'
# act_path = os.path.join(script_dir, real_path)
# my_data = np.array([])
# with open(act_path) as f:
#     lis = [line.split(',') for line in f]
#     for i,x in enumerate(lis):
#         print("line{0} = {1}".format(i,x))
