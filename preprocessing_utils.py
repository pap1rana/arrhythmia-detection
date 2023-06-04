import wfdb
import bwr
import scipy
import numpy as np

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


def remove_noise_convolution(signal):
    # Create a normalized Hanning window
    # bigger windowSize = smoother curve
    windowSize = 12
    window = np.hanning(windowSize)
    window = window / window.sum()

    signal_ch1, signal_ch2 = signal[:, 0], signal[:, 1]

    # Mode is set to 'valid' because it's less harmful to completely cut offa bit of the beginning and end of the signal
    # than to produce something that doesn't make sense
    signal_without_noise = np.column_stack((np.convolve(window, signal_ch1, mode='valid'),
                                           np.convolve(window, signal_ch2, mode='valid')))

    return signal_without_noise


# TODO: check if this works as intended? plotting the result yields suspiciously flat curve
def cutoff_freqs_fir_filter(signal):
    signal_ch1, signal_ch2 = signal[:, 0], signal[:, 1]

    fs = 200
    nyquist = 0.5 * fs
    # Lower cutoff frequency (Hz)
    lowcut = 0.05
    # Upper cutoff frequency (Hz)
    highcut = 50
    low = lowcut / nyquist
    high = highcut / nyquist
    numtaps = 101
    b = scipy.signal.firwin(numtaps=numtaps, fs=fs, cutoff=[low, high], pass_zero=False)

    signal_ch1, signal_ch2 = scipy.signal.lfilter(b, 1, signal_ch1), scipy.signal.lfilter(b, 1, signal_ch2)
    signal_without_noise = np.column_stack((signal_ch1, signal_ch2))

    return signal_without_noise


def remove_baseline_wander_wavelets(signal):
    signal_ch1, signal_ch2 = signal[:, 0], signal[:, 1]

    baseline_ch1 = bwr.calc_baseline(signal_ch1)
    baseline_ch2 = bwr.calc_baseline(signal_ch2)

    signal_ch1 = signal_ch1 - baseline_ch1
    signal_ch2 = signal_ch2 - baseline_ch2

    signal_without_wander = np.column_stack((signal_ch1, signal_ch2))

    return signal_without_wander

