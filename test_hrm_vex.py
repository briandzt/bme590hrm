import pytest
import numpy as np


@pytest.mark.parametrize("truegroup", [(np.array([[0, 1], [0, 0], [0, -1]]),
                                        (1, -1)),
                                       (np.array([[0, -0.5], [0, 0], [0, 1]]),
                                        (1, -0.5)),
                                       (np.array([[0, 0], [0, 0], [0, 1]]),
                                        (1, 0)),
                                       ])
def test_vex(truegroup):
    from hrm_Vex import hrm_Vex
    metrics = {
        "mean_hr_bpm": 0,
        "voltage_extremes": (),
        "duration": 0,
        "num_beats": 0,
        "beats": [],
    }
    result = hrm_Vex(truegroup[0], metrics)
    assert result["voltage_extremes"] == truegroup[1]
