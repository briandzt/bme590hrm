def hrm_duration(data, metrics):
    """Take in raw data，find duration of the ECG data and store
       it in the dictionary

    Parameters
    ----------
    data: ndarry(dtype=float, ndim=2)
        [[time, voltage]]
        Array containing the whole ECG script with voltage and related time

    metrics: dict
        "mean_hr_bpm": float
        "voltage_extremes": tuple
        "duration": float
        "num_beats": int
        "beats": list
        dictionary used to store metrics of ECG data

    Returns
    -------
    metrics: dict
        Same dictionary as input with updated duration entry

    """
    import numpy as np
    time = data[(slice(None), 0)]
    duration = time[-1]
    metrics["duration"] = duration
    return metrics
