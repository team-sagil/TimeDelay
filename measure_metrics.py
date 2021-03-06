import numpy as np
import sys

def measure_metrics(dataset, measurementset):
    fulldata = np.load(dataset)['arr_0']
    N_data = float(len(np.unique(fulldata['full_pair_id'])))
    data = np.load(measurementset)['arr_0']
    N_measured = float(len(np.unique(data['pair_id'])))
    
    dt_trues = data['dt']
    dt_ests = data['est']
    dt_est_err = data['est_err']

    # success fraction
    f =  N_measured / N_data

    # Chi2 value
    normalization = 1. / (f * N_data)
    diff = ((dt_ests - dt_trues) / dt_est_err) ** 2
    chi2 = normalization * diff.sum()

    # precision
    prec = dt_est_err / dt_trues
    P = normalization * prec.sum()

    # accuracy or bias
    bias = ((dt_ests - dt_trues) / dt_trues)
    A = normalization * bias.sum()

    return {'f': f,
            'chi2': chi2,
            'P': P,
            'A': A}

if __name__ == '__main__':
    for key, value in measure_metrics(*sys.argv[1:]).iteritems():
        print "%s: %s" % (key, value)

    
