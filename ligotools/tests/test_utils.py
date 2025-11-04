import numpy as np
import os
import sys
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from ligotools.utils import whiten, write_wavfile, reqshift

def test_write_wavfile_creates_file():
    test_data = np.array([0.1, 0.5, -0.3, 0.8, -0.2])
    test_filename = "test_audio.wav"
    test_fs = 4096
    
    write_wavfile(test_filename, test_fs, test_data)
    assert os.path.exists(test_filename)
    
    if os.path.exists(test_filename):
        os.remove(test_filename)

def test_reqshift_changes_data():
    sample_rate = 4096
    t = np.linspace(0, 1, sample_rate)
    test_signal = np.sin(2 * np.pi * 100 * t)
    
    shifted_signal = reqshift(test_signal, fshift=50, sample_rate=sample_rate)
    
    assert len(shifted_signal) == len(test_signal)
    assert not np.array_equal(shifted_signal, test_signal)