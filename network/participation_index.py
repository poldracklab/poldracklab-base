import numpy

def participation_index(W,Ci):
    """
    based on participation_coefficient.m from MATLAB
    Brain Connectivity Toolbox
    W: adjacency matrix
    Ci: community labels
    
    """
    

    ## n=length(W);                        %number of vertices
    n=len(Ci)
    ## Ko=sum(W,2);                        %(out)degree
    Ko=numpy.sum(W,1)
    
    ## Gc=(W~=0)*diag(Ci);                 %neighbor community affiliation
    Gc=(W>0).dot(numpy.diag(Ci))
    
    ## Kc2=zeros(n,1);                     %community-specific neighbors
    Kc2=numpy.zeros(n)
    
    ## for i=1:max(Ci);
    ##    Kc2=Kc2+(sum(W.*(Gc==i),2).^2);
    ## end
    for i in numpy.unique(Ci)[1:]:
        Kc2=Kc2 + (numpy.sum(W*(Gc==i),1)**2)
        
    ## P=ones(n,1)-Kc2./(Ko.^2);
    P=numpy.ones(n)-Kc2/(Ko**2)
    P[Ko==0]=0                          #%P=0 if for nodes with no (out)neighbors
    return P
