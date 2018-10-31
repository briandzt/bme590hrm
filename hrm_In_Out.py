def hrm_Input(filename):
    """Takes in the name of the file and convert data
       in the file to a numpy array.

    Parameters
    ----------
    filename: str
        A string with the name and extension

    Returns
    -------
    mydata: ndarry(dtype=float, ndim=2)
        [[time, voltage]]
        Array containing the whole ECG script with voltage and related time

    Raises
    ------
    ValueError:
        If no entries in the ECG script is complete, either miss time
        or voltage value
        If all entries in the ECG script has the same voltage value

    """
    import logging
    import numpy as np
    import warnings
    import os
    logging.basicConfig(filename="Inlog.txt",
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
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
        logging.debug('No valid entry for the whole file '+filename)
        raise ValueError("The selected file has no valid data entry")
    if my_data.size < (previous_size / 2):
        warnings.warn('Over 50% of the entries within the data is unreadable')
        logging.debug('Over 50% of the entries within the data is unreadable')
    print('INFO: Assigning {0} sets of data '
          'from {1}'.format(my_data.size, filename))
    logging.info('INFO: Assigning {0} sets of data'
                 ' from {1}'.format(my_data.size, filename))
    if np.unique(my_data[1]).size == 1:
        logging.debug('"The input data has uniform input"')
        raise ValueError("The input data has uniform input, please check if"
                         "the data is a valid ECG data file")
    return my_data


def hrm_Output(outdata, filename):
    """Takes in name of raw data file and related dictionary
       with calculated metrics. Store the dictionary into a
       json file with the name of raw data file.

    Parameters
    ----------
    outdata: dict
        "mean_hr_bpm": float
        "voltage_extremes": tuple
        "duration": float
        "num_beats": int
        "beats": list
        dictionary used to store metrics of ECG data

    filename: str
        Name of the raw data file

    Returns
    -------
    1 if the function progresses to the end

    """
    import json
    import os
    import logging
    logging.basicConfig(filename="Outlog.txt",
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    script_dir = os.path.dirname(__file__)
    real_path = 'Test_Output/'
    act_path = os.path.join(script_dir, real_path)
    if not os.path.exists(act_path):
        os.makedirs(act_path)
    if (filename[-4:-1] + filename[-1]) == '.csv':
        filename = filename[0:-4]
    act_path = os.path.join(act_path, filename+'.json')
    file = open(act_path, 'w')
    data = json.dumps(outdata)
    file.write(data)
    file.close()
    logging.info('Parameter successfully generated for file '+filename)
    return 1
