import wfdb
from wfdb import processing


def resample_record_and_annotations(record, annotations, fs_target):
    fs_current = record.fs

    multichan_resampled_signal, multichan_resampled_ann = wfdb.processing.resample_multichan(xs=record.p_signal,
                                                                                             ann=annotations,
                                                                                             fs=fs_current,
                                                                                             fs_target=fs_target)
    return multichan_resampled_signal, multichan_resampled_ann
