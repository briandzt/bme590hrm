def find_peak(data):
    import numpy as np
    import scipy.signal as sci
    time = np.array([i[0] for i in data])
    voltage = np.array([i[1] for i in data])
    maxv = np.max(voltage)
    minv = np.min(voltage)
    voltage = sci.savgol_filter(voltage, 3, 2)
    threv = (maxv-minv)*2/3+minv
    lowflag = (voltage < threv)
    voltage[lowflag] = 0
    peak = []
    for i in range(voltage.size):
        if i != 0 and i != (voltage.size-1):
            score = 0
            if (voltage[i] - voltage[i - 1] > 0):
                score += 1
            if (voltage[i + 1] - voltage[i] < 0):
                score += 1
            elif ((voltage[i + 1] - voltage[i] == 0) and
                  (voltage[i] - voltage[i - 1] > 0)):
                k = 0
                flag = 0
                while (flag == 0):
                    k += 1
                    flag = voltage[i + 1 + k] - voltage[i + k]
                if flag < 0:
                    score += 1
            if score >= 2:
                peak.append([time[i], voltage[i]])
    peakv = np.array([i[1] for i in peak])
    if (np.std(peakv) > 0.1*np.mean(peakv)):
        finalpeak = []
        for i in range(peakv.size):
            if not peakv[i] < (np.mean(peakv)-np.std(peakv)):
                finalpeak.append(peak[i])
    else:
        finalpeak = peak
    return finalpeak
