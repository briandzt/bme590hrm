def hrm_num_beats(data, metrics):
    """Take in list for voltage and time point of Rpeak, find total
       number of Rpeaks and update the metrics dictionary

    Parameters
    ----------
    data: ndarry(dtype=float, ndim=2)
        [[time, voltage]]
        Array containing the peaks of ECG script with voltage and related time.

    metrics : dict
        "mean_hr_bpm": float
        "voltage_extremes": tuple
        "duration": float
        "num_beats": int
        "beats": list
        dictionary used to store metrics of ECG data

    Returns
    -------
    metrics: dict
    same dictionary as in parameters with updated "beats" entry

    """
    import numpy as np
    num_beats = len(data)
    metrics["num_beats"] = num_beats
    return metrics
