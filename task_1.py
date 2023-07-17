import numpy as np
feature_1 = [1, 2, 3, 3, 1]
feature_2 = [6, 8, 11, 10, 7]
a = np.array((feature_1, feature_2))
a = a.T
mean_a = a.mean(0)
print('a_mean = %s' % mean_a)
a_centered = a - mean_a
print('a_centered =\n %s:' % a_centered)
a_centered_sp = a_centered[:, 0] @ a_centered[:, 1]
a_centered_sp /= a_centered.shape[0] - 1
print('a_centered_sp = %s:' % a_centered_sp)
cov = np.cov(a.T)[0, 1]
print('cov = %s:' % cov)
