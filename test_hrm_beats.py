import pytest
import numpy as np


@pytest.mark.parametrize("truegroup", [(np.array([[0, 1], [1, 0], [0, -1]]),
                                        [0.0, 1.0, 0.0]),
                                       (np.array([[1, -0.5], [0, 0],
                                                  [3, 1], [2, 4]]),
                                        [1, 0, 3, 2]),
                                       (np.array([[0.5, 0], [1, 0], [0, 1]]),
                                        [0.5, 1, 0]),
                                       ])
def test_beats(truegroup):
    from hrm_beats import hrm_beats
    metrics = {
        "mean_hr_bpm": 0,
        "voltage_extremes": (),
        "duration": 0,
        "num_beats": 0,
        "beats": [],
    }
    result = hrm_beats(truegroup[0], metrics)
    assert result["beats"] == truegroup[1]
