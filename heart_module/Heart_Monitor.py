def main():
    import glob
    import logging
    logging.basicConfig(filename='main.log', level=logging.DEBUG,
                        filemode='w')
    all_csv = glob.glob('*.csv')
    for info in all_csv:
        time = list()
        voltage = list()
        data = open(info)
        for line in data:
            line = line.replace('\n', '')
            word = line.split(',')
            try:
                word_time = float(word[0])
                time.append(word_time)
            except ValueError:
                pass
                logging.warning('Wrong data or missing data')
            try:
                word_voltage = float(word[1])
                voltage.append(word_voltage)
            except ValueError:
                pass
                logging.warning('Wrong data or missing data')
        delta_t = time[2] - time[1]
        str_minutes = input()
        minutes = float(str_minutes)
        from heart_module.ecg import ECG
        patient = ECG(time, voltage, delta_t, minutes)
        print(patient.num_beats)
        from heart_module.json_add import json_add
        json_add(patient.mean_hr_bpm, patient.voltage_extremes,
                 patient.duration, patient.num_beats, patient.beat_list,
                 info)
        logging.info("function run as expected")


if __name__ == "__main__":
    main()
