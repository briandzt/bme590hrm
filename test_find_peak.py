import pytest
import numpy as np


@pytest.mark.parametrize("truegroup", [('Test_data/Rpeaktest1.csv',
                                        35),
                                       ('Test_data/Rpeaktest2.csv',
                                        34),
                                       ('Test_data/Rpeaktest3.csv',
                                        32),
                                       ])
def test_hrm_find_peak(truegroup):
    from hrm_Rpeak import find_peak
    import os
    script_dir = os.path.dirname(__file__)
    act_path = os.path.join(script_dir, truegroup[0])
    with open(act_path) as f:
        my_data = np.genfromtxt(act_path, delimiter=',')
    result = find_peak(my_data)
    assert len(result) == truegroup[1]
