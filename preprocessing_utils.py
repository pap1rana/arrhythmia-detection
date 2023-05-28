import wfdb
import numpy as np
import bwr

from wfdb import processing


def resample_record_and_annotations(record, annotations, fs_target):
    fs_current = record.fs

    multichan_resampled_signal, multichan_resampled_ann = wfdb.processing.resample_multichan(xs=record.p_signal,
                                                                                             ann=annotations,
                                                                                             fs=fs_current,
                                                                                             fs_target=fs_target)
    return multichan_resampled_signal, multichan_resampled_ann


def normalize_signal_and_center(signal):
    normalized_signal = wfdb.processing.normalize_bound(signal, lb=0, ub=1)
    signal_means = np.mean(normalized_signal, axis=0)
    centered_signal = normalized_signal - signal_means

    return centered_signal


def remove_baseline_wander_wavelets(signal):
    signal_ch1, signal_ch2 = signal[:, 0], signal[:, 1]

    baseline_ch1 = bwr.calc_baseline(signal_ch1)
    baseline_ch2 = bwr.calc_baseline(signal_ch2)

    signal_ch1 = signal_ch1 - baseline_ch1
    signal_ch2 = signal_ch2 - baseline_ch2

    signal_without_wander = np.column_stack((signal_ch1, signal_ch2))

    return signal_without_wander

