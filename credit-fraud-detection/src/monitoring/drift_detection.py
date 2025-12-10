import pandas as pd
from scipy.stats import ks_2samp

def detect_drift(new_data, old_data, feature):
    stat, pvalue = ks_2samp(new_data[feature], old_data[feature])
    return pvalue < 0.05  # drift detected
