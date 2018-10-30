import pytest
import numpy as np


def test_hrm_Output():
    import os
    from hrm_In_Out import hrm_Output
    import json
    metrics = {
        "mean_hr_bpm": 3,
        "voltage_extremes": (1, 2),
        "duration": 30,
        "num_beats": 5,
        "beats": [1.4, 4.5, 6.7],
    }
    filename = 'check_Output'
    filename2 = 'check_Output2.csv'
    filenameact = 'check_Output.json'
    filenameact2 = 'check_Output2.json'
    script_dir = os.path.dirname(__file__)
    real_path = 'Test_Output/'
    act_path = os.path.join(script_dir, real_path)
    act_path1 = os.path.join(act_path, filenameact)
    act_path2 = os.path.join(act_path, filenameact2)
    hrm_Output(metrics, filename)
    hrm_Output(metrics, filename2)
    assert os.path.isfile(act_path1)
    assert os.path.isfile(act_path2)
    with open(act_path1) as f:
        result = json.load(f)
    with open(act_path2) as f:
        result2 = json.load(f)
    assert result["mean_hr_bpm"] == result2["mean_hr_bpm"] == 3
    assert result["duration"] == result2["duration"] == 30
    assert result["voltage_extremes"] == result2["voltage_extremes"] == [1, 2]
    assert result["num_beats"] == result2["num_beats"] == 5
    assert result["beats"] == result2["beats"] == [1.4, 4.5, 6.7]
    os.remove(act_path1)
    os.remove(act_path2)
