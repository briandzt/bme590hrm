def hrm_beats(peak, metrics):
    """Record time of each Rpeak, store into list and save into
    metrics dictionary

    Parameters
    ----------
    peak : ndarry(dtype=float, ndim=2)
        [[time, voltage]]
        Array containing the peak voltage and related time

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
    beats = np.array([i[0] for i in peak])
    metrics["beats"] = beats.tolist()
    return metrics
