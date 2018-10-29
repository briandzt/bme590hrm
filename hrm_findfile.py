def hrm_findfile(filename=-1):
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
    if filename == -1:
        script_dir = os.path.dirname(__file__)
        real_path = 'Test_data'
        act_path = os.path.join(script_dir, real_path)
        os.chdir(act_path)
        for file in glob.glob("*.csv"):
            if (hrm_checkinput(os.path.join(act_path, file))):
                filelist.append(file)
    else:
        if [filename[-4:-1]+filename[-1]] != '.csv':
            filename = filename+'.csv'
        filename = os.path.join(act_path, filename)
        if os.path.isfile(filename) and hrm_checkinput(filename):
            filelist.append(os.path.join(act_path, filename))
        else:
            logging.error('Specified file not exist')
            raise ImportError('The specified name of the file cannot be find')
    if len(filelist) == 0:
        logging.error('No valid file found under directory')
        raise ImportError('No valid data file in Test_/'
                          'data directory can be found')
    finfo = 'Following files were processed: '
    for i in filelist:
        finfo = finfo + i + '，'
    logging.info(finfo)
    return filelist
