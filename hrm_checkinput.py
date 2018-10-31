def hrm_checkinput(filename):
    """Function to check if

    Parameters
    ----------
    filename: str
        String contains the directory of the file to be checked

    Returns
    -------
    flag: bool
        boolean to indicate whether input file has valid format
    """
    import os
    flag = True
    with open(filename) as f:
        lis = [line.split(',') for line in f]
        for i, x in enumerate(lis):
            if len(x) != 2:
                flag = False
    return flag
