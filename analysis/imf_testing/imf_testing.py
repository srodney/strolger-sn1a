#!/usr/bin/env python
import os,sys,pdb,scipy,glob
from pylab import *
from strolger_util import util as u
from strolger_util import imf
from scipy.integrate import quad


def imfs(m1,m2):
    num1 = quad(imf.salpeter,m1,m2)[0]
    den1 = quad(imf.salpeter1,0.1,125)[0]
    ## print ('Salpeter k=%1.4f' %(num1/den1))
    

    p0=[0.5,1.]
    num = quad(imf.kroupa,m1,m2,args=tuple(p0))[0]
    den = quad(imf.kroupa1,0.1,125,args=tuple(p0))[0]
    ## print ('Kroupa k=%1.4f' %(num/den))
    return(num1/den1, num/den)


data = []
for m1 in arange(2.5,4.1,0.1):
    for m2 in arange(7,11.0,0.1):
        data.append(imfs(m1,m2))

data=array(data)
#print(average(data[:,0]), average(data[:,1]))
print(std(data[:,0]), std(data[:,1]))
med=quad(imf.salpeter,3,8)[0]/quad(imf.salpeter1,0.1,125)[0]
print(med)
print('minus %2.1f%%, plus %2.1f%%' %(std(data[:,0])/med*100., std(data[:,1])/med*100.))



