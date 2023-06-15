import wfdb
import numpy as np
from wfdb import processing


class HeartbeatSlicer:
    def __init__(self, record_path, sampfrom=0, sampto=None, num_heartbeats=3):
        self.record = wfdb.rdrecord(record_name=record_path, sampfrom=sampfrom, sampto=sampto)
        self.annotations = wfdb.rdann(record_name=record_path, extension='atr', sampfrom=sampfrom, sampto=sampto, shift_samps=True)
        self.ann_symbols = self.annotations.symbol
        self.ecg_data = self.record.p_signal[:, 0]
        self.sampling_rate = self.record.fs
        self.peak_indices = self.detect_peaks()
        self.num_heartbeats = num_heartbeats
        self.label_dict = {
            '!': -1,
            '"': -1,
            '+': -1,
            '[': -1,
            ']': -1,
            '|': -1,
            '~': -1,
            'x': -1,
            'Q': -1,
            'N': 0,
            '/': 0,
            'f': 0,
            'A': 1,
            'B': 1,
            'E': 1,
            'F': 1,
            'J': 1,
            'L': 1,
            'R': 1,
            'S': 1,
            'V': 1,
            'a': 1,
            'e': 1,
            'j': 1,
        }

    def detect_peaks(self):
        """
        Detects peaks in the ECG data.

        Returns: numpy array with the indices of peaks.
        """

        # peak_indices = processing.gqrs_detect(sig=self.ecg_data, fs=self.sampling_rate)

        peak_indices = self.annotations.sample

        return np.array(peak_indices, dtype=object)

    def slice_heartbeats(self):
        """
        Slice the ECG data into sequences of a fixed number of consecutive heartbeats.

        num_heartbeats : The number of consecutive heartbeats to include in each sequence.

        Returns: 2D numpy array, each row is a sequence of heartbeats.
        """
        heartbeats = []

        for i in range(self.num_heartbeats, len(self.peak_indices)-self.num_heartbeats):
            start = self.peak_indices[i] - (self.peak_indices[i] - self.peak_indices[i-self.num_heartbeats])//2
            end = self.peak_indices[i] +  (self.peak_indices[i+self.num_heartbeats] - self.peak_indices[i])//2
            sequence = self.ecg_data[start:end]

            heartbeats.append(sequence)

        return np.array(heartbeats, dtype=object)

    def annotate_heartbeats(self):
        """
        Annotates the heartbeats obtained from the slice_heartbeats() method. It assigns labels to each heartbeat based on the provided label dictionary. The labels are added to the heartbeats array as a new column.

        Returns: numpy.ndarray: The annotated heartbeats array with the labels added as a new column.

        """
        heartbeats = self.slice_heartbeats()

        anns = list(map(lambda x: self.label_dict.get(x, x), self.ann_symbols[self.num_heartbeats:-self.num_heartbeats]))

        return np.column_stack((heartbeats, anns))


