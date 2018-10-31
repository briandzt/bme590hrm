def hrm_mean_hrbpm(peak, metrics, time=-1):
    """Take in list of peak voltage and related time point as well as the
       specified time. Calculate the bpm, store into the given dictionary
       and return the same dictionary.

    Parameters
    ----------
    peak: ndarry(dtype=float, ndim=2)
        [[time, voltage]]
        Array containing peaks of ECG script with voltage and related time.

    metrics:dict
        "mean_hr_bpm": float
        "voltage_extremes": tuple
        "duration": float
        "num_beats": int
        "beats": list
        dictionary used to store metrics of ECG data

    time: str
        User specified time used as the time interval for bpm calculation.

    Returns
    -------
    metrics: dict
    same dictionary as in parameters with updated "beats" entry

    """
    import numpy as np
    import warnings
    import logging
    logging.basicConfig(filename="bpmlog.txt",
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    num = 0
    time = float(time)*60
    if time != -1 and time <= peak[-1][0]:
        for i in peak:
            if i[0] < time:
                num += 1
            elif i[0] == time:
                num += 1
                bpm = float(num)*60/time
            else:
                bpm = float(num)*60/time
                break
    else:
        bpm = float(len(peak))*60/metrics['duration']
    metrics["mean_hr_bpm"] = bpm
    if not (bpm > 30 or bpm < 110):
        warnings.warn('The bpm of this data is abnormal'
                      'comparing to a normal human bpm')
        logging.warning('bpm of this datais abnormal'
                        'comparing to a normal human bpm')
    return metrics
