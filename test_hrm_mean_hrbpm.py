import pytest
import numpy as np


@pytest.mark.parametrize("truegroup", [(np.array([[0, 1], [6, 0],
                                                  [10, -1]]), 0.1, 20.0),
                                       (np.array([[0, 1], [6, 0],
                                                  [10, -1]]), 1, 6.0),
                                       (np.array([[0, 1], [6, 0],
                                                  [12, -1]]), 0.2, 15.0),
                                       ])
def test_hrm_mean_hrbpm(truegroup):
    from hrm_mean_hrbpm import hrm_mean_hrbpm
    metrics = {
        "mean_hr_bpm": 0,
        "voltage_extremes": (),
        "duration": 30,
        "num_beats": 0,
        "beats": [],
    }
    result = hrm_mean_hrbpm(truegroup[0], metrics, truegroup[1])
    assert result["mean_hr_bpm"] == truegroup[2]
