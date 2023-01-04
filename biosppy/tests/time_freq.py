# -*- coding: utf-8 -*-
"""
biosppy.tests.time_freq
-------------------
This module provides methods to test the time frequency feature extraction module.
:copyright: (c) 2015-2018 by Instituto de Telecomunicacoes
:license: BSD 3-clause, see LICENSE for more details.
"""

# Imports
# 3rd party
import numpy as np

# local
from ..features.time_freq import get_DWT


def getData(size=100, sampling_rate=100):
    const0 = np.zeros(size)
    const1 = np.ones(size)
    constNeg = -1 * np.ones(size)

    f = 5
    x = np.arange(0, size/sampling_rate, 1/sampling_rate)
    sine = np.sin(2 * np.pi * f * x)
    np.random.seed(0)
    sine = sine + np.random.normal(0, 0.5, size)
    lin = np.arange(size)
    sine = +2*np.sin(2 * np.pi * 10 * x)
    return const0, const1, constNeg, lin, sine


def test(size=1000, sampling_rate=100):

    const0, const1, constNeg, lin, sine = getData(size, sampling_rate)
    
    const0_ca, const0_cd  = get_DWT(const0)
    const1_ca, const1_cd = get_DWT(const1)
    constNeg_ca, constNeg_cd = get_DWT(constNeg)
    lin_ca, lin_cd = get_DWT(lin)
    sine_a, sine_d = get_DWT(sine)
    
    print("End Check")

