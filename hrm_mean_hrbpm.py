def hrm_mean_hrbpm(peak, metrics, time=-1):
    import numpy as np
    num = 0
    time = 20
    if time != -1 and time < peak[-1][0]:
        for i in peak:
            if i[0] <= time:
                num += 1
            else:
                bpm = num/time*60
    else:
        bpm = len(data)/data[-1][0]*60
    metrics["mean_hr_bpm"] = bpm
    return metrics
