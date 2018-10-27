def hrm_duration(data, metrics):
    import numpy as np
    time = np.array([i[0] for i in data])
    duration = time[-1]
    metrics["duration"] = duration
    return metrics
