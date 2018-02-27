class ECG:
    def __init__(self, t_list = None, v_list = None, delta_t = None):
        self.t_list = t_list
        self.v_list = v_list
        self.duration = t_list[end]
        self.delta_t = delta_t
        self.count_beat()
        self.voltage_ex()

    def count_beat(self):
        """
                Returns the maximum difference of a list
                :param x: list to be input
                :type x: list
                :raises TypeError: if input is not a list
                :raises ValueError: if the list contains a non-float or integer
                :raises ValueError: if list contains +/-infinity

                :return: the maximum difference of adjacent numbers
                :rtype: float
                """
        try:
            import numpy as np
            import logging
            from peak_detect import detect_peaks
        except ImportError:
            print("Necessary imports failed")
            return
        else:
            logging.basicConfig(filename='count_beat.log', level=logging.DEBUG,
                        filemode='w')

        max_voltage = max(self.v_list)
        index_max_v = self.v_list.index(max_voltage)
        qrs = []
        if self.delta_t >= 0.01:
            qrs = self.v_list[index_max_v -10:index_max_v + 10]
        else:
            qrs = self.v_list[index_max_v - 20:index_max_v + 20]

        v_corr = np.correlate(self.v_list, qrs, "full")
        v_corr_max = max(v_corr)
        min_interval = 1/180
        ind = detect_peaks(v_corr, mph=0.5 * v_corr_max, mpd=min_interval, edge='rising')
        #num_beats
        self.num_beats = ind.size
        beat_list = []
        for index in ind:
            beat_list.append(self.t_list[index])
        #beats
        self.beats = np.array(beat_list)

    def voltage_ex(self):
        from voltage_extremes import voltage_extremes
        self.voltage_extremes = voltage_extremes(self.v_list)




