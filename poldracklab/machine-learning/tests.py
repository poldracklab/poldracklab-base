import numpy


def test_balanced_folds():
if 1:
    from get_balanced_folds import get_balanced_folds
    from statsmodels.regression.linear_model import OLS
    
    y=numpy.random.randn(100)
    nfolds=4
    pthresh=0.8
    cv=get_balanced_folds(y,nfolds,pthresh)
    ctr=0
    y_fold=numpy.zeros(len(y))
    idx=numpy.zeros((len(y),nfolds))
    for train, test in cv:
            idx[test,ctr]=1
            ctr+=1

    lm_y=OLS(y-numpy.mean(y),idx).fit()

    assert(lm_y.f_pvalue>pthresh)
    

    