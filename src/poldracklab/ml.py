"""Functions for cross-validation

This module provides functions for cross-validation, including
functions to split data into training and testing sets.

The module contains the following functions:

- `BalancedKFold`: Split data into training and testing sets using anova across CV folds

"""

from statsmodels.regression.linear_model import OLS
from sklearn.model_selection import KFold
import numpy as np
from typing import Iterator, Tuple


class BalancedKFold:
    """
    This function uses anova across CV folds to find
    a set of folds that are balanced in their distriutions
    of the X value - see Kohavi, 1995
    - we don't actually need X but we take it for consistency

    Args:
        nfolds (int): the number of folds to use
        pthresh (float): the p-value threshold for a good split
        verbose (bool): whether to print verbose output
    """

    def __init__(self, nfolds: int = 5, pthresh: float = 0.8, verbose: bool = False):
        self.nfolds = nfolds
        self.pthresh = pthresh
        self.verbose = verbose

    def split(
        self, X: np.ndarray, Y: np.ndarray, max_splits: int = 1000
    ) -> Iterator[Tuple[np.ndarray, np.ndarray]]:
        """
        Split the data into training and testing sets

        Args:
            X (np.ndarray): the input data
            Y (np.ndarray): the target data
            max_splits (int): the maximum number of splits to try

        Returns:
            Iterator[Tuple[np.ndarray, np.ndarray]]: the training and testing sets
        """

        nsubs = len(Y)

        # cycle through until we find a split that is good enough

        runctr = 0
        best_pval = 0.0
        while 1:
            runctr += 1
            cv = KFold(n_splits=self.nfolds, shuffle=True)

            idx = np.zeros((nsubs, self.nfolds))  # this is the design matrix
            folds = []
            ctr = 0
            for train, test in cv.split(Y):
                idx[test, ctr] = 1
                folds.append([train, test])
                ctr += 1

            lm_y = OLS(Y - np.mean(Y), idx).fit()

            if lm_y.f_pvalue > best_pval:
                best_pval = lm_y.f_pvalue
                best_folds = folds

            if lm_y.f_pvalue > self.pthresh:
                if self.verbose:
                    print(lm_y.summary())
                return iter(folds)

            if runctr > max_splits:
                print("no sufficient split found, returning best (p=%f)" % best_pval)
                return iter(best_folds)
