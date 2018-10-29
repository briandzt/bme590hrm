def hrm_checkinput(filename):
    import os
    with open(filename) as f:
        lis = [line.split(',') for line in f]
        for i, x in enumerate(lis):
            if len(x) != 2:
                return(False)
    return True
