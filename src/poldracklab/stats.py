"""
utils to convert between r and z values
"""

import numpy as np


def r_to_z(r: float | list | np.ndarray) -> float | np.ndarray:
    """
    Convert r values to z values

    Args:
        r (float or list): the r values to convert

    Returns:
        float or np.ndarray: the z values
    """
    if isinstance(r, list):
        r = np.array(r)
    # fisher transform
    z = 0.5 * np.log((1.0 + r) / (1.0 - r))
    # replace inf with nan
    z[np.where(np.isinf(z))] = np.nan
    return z


def z_to_r(z: float | list | np.ndarray) -> float | np.ndarray:
    """
    Convert z values to r values

    Args:
        z (float or list): the z values to convert

    Returns:
        float or np.ndarray: the r values
    """
    if isinstance(z, list):
        z = np.array(z)
    # inverse transform
    return (np.exp(2.0 * z) - 1) / (np.exp(2.0 * z) + 1)
