

from statsmodels.regression.linear_model import OLS
from sklearn import cross_validation
import numpy as N



def get_balanced_folds(y,nfolds,pthresh=0.8):
    """
    This function uses anova across CV folds to find
    a set of folds that are balanced in their distriutions
    of the X value - see Kohavi, 1995
    """

    nsubs=len(y)

    # cycle through until we find a split that is good enough
    
    good_split=0
    while good_split==0:
        cv=cross_validation.KFold(n=nsubs,n_folds=nfolds,shuffle=True)
        ctr=0
        idx=N.zeros((nsubs,nfolds)) # this is the design matrix
        for train,test in cv:
            idx[test,ctr]=1
            ctr+=1

        lm_y=OLS(y-N.mean(y),idx).fit()

        if lm_y.f_pvalue>pthresh:
            good_split=1
            return cv
