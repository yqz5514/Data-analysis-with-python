import numpy as np

def calculate(lis):
    calculations = dict()
    list_len = 9 # List length to store for further usage
    if len(lis) == list_len:
        # p = np.reshape([0,1,2,3,4,5,6,7,8], (3,3)) More efficient method
        n = np.ones((3,3))
        n[0,0:3] = lis[0:3].copy()
        n[1,0:3] = lis[3:6].copy()
        n[2,0:3] = lis[6:9].copy()
        flatten_mat = n.flatten() # Flatten Matrix along rows by default

        # Mean of 3x3 Matrix Calculations
        flatten_mean = np.mean(flatten_mat)
        calculations['mean'] = [list(np.mean(n, axis = 0)) , list(np.mean(n, axis = 1)), flatten_mean]

        # Variance of 3x3 Matrix Calculations
        flatten_var = np.var(flatten_mat)
        calculations['variance'] = [list(np.var(n, axis = 0)) , list(np.var(n, axis = 1)), flatten_var]

        # Standard Deviations of 3x3 Matrix Calculations
        flatten_std = np.std(flatten_mat)
        calculations['standard deviation'] = [list(np.std(n, axis = 0)) , list(np.std(n, axis = 1)), flatten_std]

        # Maximum Value of 3x3 Matrix Calculations
        flatten_max = np.max(flatten_mat)
        calculations['max'] = [list(np.max(n, axis = 0).astype('int32')) , list(np.max(n, axis = 1).astype('int32')), flatten_max.astype('int32')]

        # Minimum Value of 3x3 Matrix Calculations
        flatten_min = np.min(flatten_mat)
        calculations['min'] = [list(np.min(n, axis = 0).astype('int32')) , list(np.min(n, axis = 1).astype('int32')), flatten_min.astype('int32')]

        # Sum of values of 3x3 Matrix Calculation
        flatten_sum = np.sum(flatten_mat)
        calculations['sum'] = [list(np.sum(n, axis = 0).astype('int32')) , list(np.sum(n, axis = 1).astype('int32')), flatten_sum.astype('int32')]


        return calculations
    else:
        raise ValueError("List must contain nine numbers.")
