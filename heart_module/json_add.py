def json_add(mean_hr_bpm, voltage_extremes, duration, num_beats, beats, info):
    """
            dump all the attributes of a object in a dictionary and then
            to a json file

            :param mean_hr_bpm: the input should be a int
            :param voltage_extremes: the input should be a int
            :param num_beats: the input should be a int
            :param duration: the input should be a float
            :param beats: the input should be a float
            :param info: the input should be a string
            :raises ValueError: if the input includes string

            :returns: return a float equals estimated average heart rate over a
            user-specified number of minutes
            :rtype: float
            """
    # ecg_info = dict()
    ecg_info = {'mean_hr_bpm': mean_hr_bpm, 'voltage_extremes': voltage_extremes,
                'duration': duration, 'num_beats': num_beats, 'beats': beats}
    try:
        import json
        import logging
    except ImportError:
        print("Necessary imports failed")
        return
    logging.basicConfig(filename='json_add.log', level=logging.DEBUG,
                        filemode='w')
    file = open(info.replace('.csv', '.json'), 'w')
    asd = json.dumps(ecg_info)
    file.write(asd)
    logging.info("function run as expected")
    return file
