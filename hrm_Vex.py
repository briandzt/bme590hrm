def hrm_Vex(data, metrics):
    import numpy as np
    voltage = data[(slice(None), 1)]
    maxv = np.max(voltage)
    minv = np.min(voltage)
    metrics["voltage_extremes"] = (maxv, minv)
    return metrics
