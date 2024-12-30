import numpy as np
from poldracklab.fmri import spm_hrf


def test_spm_hrf():
    TR = 2.0
    p = np.array([6, 16, 1, 1, 6, 0, 32])
    fMRI_T = 16.0
    hrf = spm_hrf(TR, p=p, fMRI_T=fMRI_T)
    hrf_default = spm_hrf(TR)
    assert hrf is not None
    assert hrf.shape == (int(p[6] / TR),)
    assert np.allclose(hrf, hrf_default)


if __name__ == "__main__":
    test_spm_hrf()
