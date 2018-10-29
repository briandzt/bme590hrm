def hrm_findfile(filename=-1):
    import os
    import glob
    import warnings
    from hrm_checkinput import hrm_checkinput
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
            if len(filelist) == 0:
                raise ImportError('No valid data file in Test_/'
                                  'data directory can be found')
    else:
        if [filename[-4:-1]+filename[-1]] != '.csv':
            filename = filename+'.csv'
        if os.path.isfile(os.path.join(act_path, filename)):
            filelist.append(os.path.join(act_path, filename))
        else:
            raise ImportError('The specified name of the file cannot be find')
    return filelist
