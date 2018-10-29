import pytest
import numpy as np


@pytest.mark.parametrize("truegroup", [(np.array([[0, 1], [1, 0], [0, -1]]),
                                        3),
                                       (np.array([[1, -0.5], [0, 0],
                                                  [3, 1], [2, 4]]),
                                        4),
                                       (np.array([[0.5, 0]]),
                                        1),
                                       ])
def test_num_beats(truegroup):
    from hrm_num_beats import hrm_num_beats
    metrics = {
        "mean_hr_bpm": 0,
        "voltage_extremes": (),
        "duration": 0,
        "num_beats": 0,
        "beats": [],
    }
    result = hrm_num_beats(truegroup[0], metrics)
    assert result["num_beats"] == truegroup[1]
