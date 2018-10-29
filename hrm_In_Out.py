def hrm_Input(filename):
    import numpy as np
    import warnings
    import os
    script_dir = os.path.dirname(__file__)
    real_path = 'Test_data'
    act_path = os.path.join(script_dir, real_path)
    act_path = os.path.join(act_path, filename)
    my_data = np.array([])
    with open(act_path) as f:
        my_data = np.genfromtxt(act_path, delimiter=',')
    wronginput = []
    previous_size = my_data.size
    for i, x in enumerate(my_data):
        if np.isnan(x[0]) or np.isnan(x[1]):
            wronginput.append(i)
    my_data = np.delete(my_data, wronginput, 0)
    if my_data.size == 0:
        raise ValueError("The selected file has no valid data entry")
    if my_data.size < (previous_size / 2):
        warnings.warn('Over 50% of the entries within the data is unreadable')
    print('INFO: Assigning {0} sets of data to /'
          'from {1}'.format(my_data.size, filename))
    return my_data


def hrm_Output(outdata, filename):
    import json
    import os
    script_dir = os.path.dirname(__file__)
    real_path = 'Test_Output/'
    act_path = os.path.join(script_dir, real_path)
    if not os.path.exists(act_path):
        os.makedirs(act_path)
    filename = filename[0:-4] + '.json'
    act_path = os.path.join(act_path, filename)
    file = open(act_path, 'w')
    data = json.dumps(outdata)
    file.write(data)
    file.close()
    return 1
