from poldracklab.stats import r_to_z, z_to_r
import numpy as np


def test_r_to_z():
    assert np.allclose(
        r_to_z([0.5, 0.5, 0.5]),
        [0.5493061443340549, 0.5493061443340549, 0.5493061443340549],
    )


def test_z_to_r():
    assert np.allclose(
        z_to_r([0.5493061443340549, 0.5493061443340549, 0.5493061443340549]),
        [0.5, 0.5, 0.5],
    )
