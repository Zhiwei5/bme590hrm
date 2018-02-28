import glob

all_csv = glob.glob('*.csv')
for info in all_csv:
    time = list()
    voltage = list()
    # delta_t = 0.0
    data = open(info)
    for line in data:
        line = line.replace('\n', '')
        word = line.split(',')
        word_time = float(word[0])
        time.append(word_time)
        word_voltage = float(word[1])
        voltage.append(word_voltage)
    delta_t = time[2] - time[1]
    str_minutes = input()
    minutes = float(str_minutes)
    from ecg import ECG
    # how should I assign the attributes to a name
    abc = ECG(time,voltage,delta_t,minutes)





