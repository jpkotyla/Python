import numpy as np
import pandas as pd
from pandas import Series,DataFrame,Index


def E_pdf(pdf):
    assert abs(pdf.sum() - 1.0) < 0.001
    E = 0
    for i in pdf.index:
        E += i*pdf.ix[i]
    return E

def Var_pdf(pdf):
    return(E_pdf(pdf**2) - E_pdf(pdf)**2)


def pdf_n_rolls_p_sided_dp(n,p):
    assert(n>0)

    pdfs = {}
    pdfs[1] = Series({i:1./p for i in range(1,p+1)})

    if n == 1:
        return pdfs[1],pdfs

    else:
        for i in range(2,n+1):
            pdf_new = Series(index= Index(range(i,i*p+1)))
            for ind in pdf_new.index:
                pdf_new.ix[ind] = pdfs[i-1].ix[ind-p:ind-1].sum()/p
            pdfs[i] = pdf_new
    return pdfs[n],pdfs

def mixed_rolls(t1,p2):
    n1,p1 = t1
    max_val = n1*p1*p2

    first_pdf = pdf_n_rolls_p_sided_dp(n1,p1)[0]
    import pdb;pdb.set_trace()
    combo_pdf = Series(index = Index(range(n1,max_val+1))).fillna(0)
    pdfs = pdf_n_rolls_p_sided_dp(n1*p1,p2)[1]

    for ind in first_pdf.index:
        combo_pdf = combo_pdf.combine(other = (first_pdf.ix[ind]*pdfs[ind]).reindex(combo_pdf.index).fillna(0),
                                      func = lambda x,y:x+y)
    return combo_pdf


def mutli_roll(pdf_1,p2):
    first_pdf = pdf_1
    combo_pdf = Series(index = Index(range(min(pdf_1.index),max(pdf_1.index)*p2+1))).fillna(0)
    pdfs = pdf_n_rolls_p_sided_dp(int(max(pdf_1.index)),p2)[1]

    for ind in first_pdf.index:
        combo_pdf = combo_pdf.combine(other = (first_pdf.ix[ind]*pdfs[int(ind)]).reindex(combo_pdf.index).fillna(0),
                                      func = lambda x,y: x+y)

    return combo_pdf



pdf6 = mixed_rolls((1,4),6)

pdf8 = mutli_roll(pdf6,8)
pdf12 = mutli_roll(pdf8,12)


def combine_add(ser1,ser2):
    res = ser1 + ser2.fillna(0)
