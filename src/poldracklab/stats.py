"""
utils to convert between r and z values
"""

import numpy as np


def r_to_z(r):
    if isinstance(r, list):
        r = np.array(r)
    # fisher transform
    z = 0.5 * np.log((1.0 + r) / (1.0 - r))
    # replace inf with nan
    z[np.where(np.isinf(z))] = np.nan

    return z


def z_to_r(z):
    if isinstance(z, list):
        z = np.array(z)
    # inverse transform
    return (np.exp(2.0 * z) - 1) / (np.exp(2.0 * z) + 1)
