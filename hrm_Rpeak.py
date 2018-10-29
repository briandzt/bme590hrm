def find_peak(data):
    import numpy as np
    import scipy.signal as sci
    import logging
    logging.basicConfig(filename="mainlog.txt",
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    time = data[(slice(None), 0)]
    voltage = data[(slice(None), 1)]
    maxv = np.max(voltage)
    minv = np.min(voltage)
    voltage = sci.savgol_filter(voltage, 3, 2)
    histv = np.histogram(voltage, bins=10)
    revflag = 0
    if np.argmax(histv[0]) > np.average(histv[0], weights=histv[1][0:-1]):
        revflag = 1
        threv = maxv - (maxv - minv) * 2 / 3
        lowflag = (voltage > threv)
        voltage = -voltage
    else:
        threv = (maxv - minv) * 2 / 3 + minv
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
                if revflag == 1:
                    peak.append([time[i], -voltage[i]])
                else:
                    peak.append([time[i], voltage[i]])
    peakv = np.array([i[1] for i in peak])
    if (np.std(peakv) > 0.1*np.mean(peakv)):
        finalpeak = []
        for i in range(peakv.size):
            if not peakv[i] < (np.mean(peakv)-np.std(peakv)):
                if (i != 0 and i != peakv.size-1):
                    t1 = peak[i][0]-peak[i-1][0]
                    t2 = peak[i+1][0]-peak[i][0]
                    if t1/t2 <= 1.1:
                        finalpeak.append(peak[i])
                elif i == 0:
                    t1 = peak[i][0]-peak[i+1][0]
                    t2 = peak[i+1][0]-peak[i+2][0]
                    if t1/t2 >= 1.1:
                        finalpeak.append(peak[i])
                else:
                    finalpeak.append(peak[i])
    else:
        finalpeak = peak
    if len(finalpeak) == 0:
        logging.debug('The algorithm failed to find peaks within '
                      'given data. Please check the data file to'
                      ' make sure it is a valid ECG data. If it is, '
                      'Better algorithm for this program to find peaks '
                      'is under development.')
        raise ValueError('The algorithm failed to find peaks within'
                         ' given data. Please check the data file to'
                         ' make sure it is a valid ECG data. If it is, '
                         'Better algorithm for this program to find peaks '
                         'is under development.')
    return finalpeak
