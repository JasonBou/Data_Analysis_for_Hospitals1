import numpy as np

one_list_warning = "One argument is a list"
two_lists_warning = "Both arguments are lists, not arrays"

def custom_sum(arg1, arg2):
    if isinstance (arg1, np.ndarray) and isinstance (arg2, np.ndarray):
        return arg1 + arg2
    elif isinstance (arg1, list) and isinstance(arg2, list):
        return two_lists_warning 
    else: 
    #(isinstance (arg1, np.ndarray) and isinstance (arg2, list)) or (isinstance (arg1, list) and isinstance (arg2,np.ndarray)):
        return one_list_warning
    
