import numpy as np
import pandas as pd

def find_min_distance(df, ref):
    '''
    Takes panda dataframe with X and Y columns and reference coordinates,
    Returns index of the row containing coordinates closest to the reference coordinates
    '''
    return np.argmin([np.sum([(a - b)**2 for a,b in zip(ref, row)]) for row in df.values])