def hrm_duration(data, metrics):
    import numpy as np
    time = data[(slice(None), 0)]
    duration = time[-1]
    metrics["duration"] = duration
    return metrics
