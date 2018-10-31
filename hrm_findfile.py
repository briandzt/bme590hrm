def hrm_findfile(filename='-1'):
    """Search the Test_data directory for specified or valid ECG
       data csv file and return a list containing their names

    Parameters
    ----------
    filename: str
        User defined name of the data file to be processed. The
        name can either or not contain .csv extension. -1 means
        to scan all valid data file within the directory

    Returns
    -------
    filelist: list
        List containing names of specified ECG data or all valid
        ECG data in the directory if input filename is -1

    Raises
    ------
    ValueError
        if input file name cannot be find

    ImportError
        if no vaild file can be found within the directory

    """
    import os
    import glob
    import warnings
    import logging
    from hrm_checkinput import hrm_checkinput
    logging.basicConfig(filename="runfilelog.txt",
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    script_dir = os.path.dirname(__file__)
    real_path = 'Test_data'
    act_path = os.path.join(script_dir, real_path)
    filelist = []
    if filename == '-1':
        script_dir = os.path.dirname(__file__)
        real_path = 'Test_data'
        act_path = os.path.join(script_dir, real_path)
        os.chdir(act_path)
        for file in glob.glob("*.csv"):
            if (hrm_checkinput(os.path.join(act_path, file))):
                filelist.append(file)
    else:
        if (filename[-4:-1]+filename[-1]) != '.csv':
            filename = filename+'.csv'
        filename1 = os.path.join(act_path, filename)
        if os.path.isfile(filename1) and hrm_checkinput(filename1):
            filelist.append(filename)
        else:
            logging.error('Specified file not exist')
            raise ValueError('The specified name of the file cannot be find')
    if len(filelist) == 0:
        logging.error('No valid file found under directory')
        raise ImportError('No valid data file in Test_/'
                          'data directory can be found')
    finfo = 'Following files were processed: '
    for i in filelist:
        finfo = finfo + i + '，'
    logging.info(finfo)
    return filelist
