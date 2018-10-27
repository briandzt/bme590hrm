def hrm_Input(num):
    import numpy as np
    import os
    script_dir = os.path.dirname(__file__)
    real_path = 'Test_data/test_data'+str(num)+'.csv'
    act_path = os.path.join(script_dir, real_path)
    my_data = np.genfromtxt(act_path, delimiter=',')
    return my_data


def hrm_Output(outdata, num):
    import json
    import os
    script_dir = os.path.dirname(__file__)
    real_path = 'Test_Output/'
    act_path = os.path.join(script_dir, real_path)
    if not os.path.exists(act_path):
        os.makedirs(act_path)
    file = open(act_path+'test_data'+str(num)+'.json', 'w')
    data = json.dumps(outdata)
    file.write(data)
    file.close()
    return 1
