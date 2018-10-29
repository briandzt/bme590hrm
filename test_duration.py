import pytest
import numpy as np


@pytest.mark.parametrize("truegroup", [(np.array([[0, 1], [1, 0], [2, -1]]),
                                        2),
                                       (np.array([[0, -0.5], [0.5, 0],
                                                  [0.7, 1], [0.9, 4]]),
                                        0.9),
                                       (np.array([[0.5, 0]]),
                                        0.5),
                                       ])

def test_hrm_duration(truegroup):
    from hrm_duration import hrm_duration
    metrics = {
        "mean_hr_bpm": 0,
        "voltage_extremes": (),
        "duration": 0,
        "num_beats": 0,
        "beats": [],
    }
    result = hrm_duration(truegroup[0], metrics)
    assert result["duration"] == truegroup[1]