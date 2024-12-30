import numpy as np
from poldracklab.ml.balanced_kfold import BalancedKFold


def test_get_balanced_folds():
    Y = np.random.randn(100, 1)
    bkf = BalancedKFold(nfolds=5, pthresh=0.8)
    folds = bkf.split(Y, Y)
    assert len(list(folds)) == 5
