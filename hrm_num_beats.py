def hrm_num_beats(data, metrics):
    import numpy as np
    num_beats = len(data)
    metrics["num_beats"] = num_beats
    return metrics
