def hrm_Vex(data, metrics):
    import numpy as np
    voltage = np.array([i[1] for i in data])
    maxv = np.max(voltage)
    minv = np.min(voltage)
    metrics["voltage_extremes"] = (maxv, minv)
    return metrics
