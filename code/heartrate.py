def heart_bpm(number_beats,duration,minutes):
    """
        find the minimum and the maximum of a list of voltage and return a tuple

        :param number_beats: the input should be a int
        :param duration: the input should be a float
        :param minutes: the input should be a float
        :raises TypeError:  if the input is not a list or the input includes string
        :raises ValueError: if the input includes string

        :returns: return a float equals estimated average heart rate over a user-specified number of minutes
        :rtype: float
        """
    try:
        import logging
    except ImportError:
        print("Necessary imports failed")
        return
    logging.basicConfig(filename='max_difference.log', filemode='w',
                        level=logging.DEBUG)
    beat_per_min = number_beats / (duration / 60)
    mean_hr_bpm = beat_per_min * minutes
    return mean_hr_bpm
