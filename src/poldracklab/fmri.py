#!/usr/bin/env python

import scipy.stats
import numpy as np
from typing import Optional


def spm_hrf(
    TR: (float, np.ndarray), fMRI_T: float = 16.0, p: Optional[np.ndarray] = None
) -> np.ndarray:
    """An implementation of spm_hrf.m from the SPM distribution

    Arguments:

    Required:
    TR: repetition time(s) at which to generate the HRF (in seconds)

    Optional:

    fMRI_T: float = 16.0
        time steps per second for the hrf (default 16)

    p: list with parameters of the two gamma functions:
                                                         defaults
                                                        (seconds)
       p[0] - delay of response (relative to onset)         6
       p[1] - delay of undershoot (relative to onset)      16
       p[2] - dispersion of response                        1
       p[3] - dispersion of undershoot                      1
       p[4] - ratio of response to undershoot               6
       p[5] - onset (seconds)                               0
       p[6] - length of kernel (seconds)                   32

    Returns:
        np.ndarray: HRF(s)
    """

    if p is None:
        p = np.array([6, 16, 1, 1, 6, 0, 32])

    TR = float(TR)
    dt = TR / fMRI_T
    u = np.arange(p[6] / dt + 1) - p[5] / dt
    hrf = (
        scipy.stats.gamma.pdf(u, p[0] / p[2], scale=1.0 / (dt / p[2]))
        - scipy.stats.gamma.pdf(u, p[1] / p[3], scale=1.0 / (dt / p[3])) / p[4]
    )
    good_pts = np.array(range(int(p[6] / TR))) * fMRI_T
    hrf = hrf[list(good_pts.astype("int"))]
    # hrf = hrf([0:(p(7)/RT)]*fMRI_T + 1);
    hrf = hrf / np.sum(hrf)
    return hrf
