# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 09:42:53 2018

@author: icruicks
"""
from sklearn.base import BaseEstimator, ClassifierMixin
import numpy as np

class NBI(BaseEstimator, ClassifierMixin):
    
    def __init__(self):
        pass

    def fit(self, A):
        '''
        A is a biaprtite network of two not neccesarily equal dimensions and a numpy 
        array of binary data
        '''
        A = np.asanyarray(A)
        k_x = np.sum(A, axis=0)
        k_y = np.sum(A, axis=1)
        W = np.zeros((A.shape[1], A.shape[1]))
        for i in range(W.shape[0]):
            for j in range(W.shape[1]):
                W[i,j] = np.divide(1, k_x[j], out=np.zeros_like(k_x[j]), where=k_x[j]!=0)*np.sum(np.divide(np.multiply(A[:,i],A[:,j]), k_y))
        self.W_ =W
        
        return self
    
    def predict(self, a):
        
        a = np.asanyarray(a)
        f_prime = np.zeros(a.shape[0])
        
        for j in range(f_prime.shape[0]):
            f_prime[j] = np.sum(np.multiply(self.W_[j,:], a))
        
        self.y_ = f_prime
        return self.y_
    