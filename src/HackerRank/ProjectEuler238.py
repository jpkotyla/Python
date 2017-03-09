import numpy as np
import pandas as pd


def E_pdf(pdf):
    assert abs(pdf.sum() - 1.0) < 0.001
    E = 0
    for i in pdf.index:
        E += i*pdf.ix[i]
    return E

def Var_pdf(pdf):
    return(E_pdf(pdf**2) - E_pdf(pdf)**2)


