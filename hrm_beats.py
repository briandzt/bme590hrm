def hrm_beats(peak, metrics):
    import numpy as np
    beats = np.array([i[0] for i in peak])
    metrics["beats"] = beats.tolist()
    return metrics
