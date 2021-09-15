# A rough basis for the work in `bs_aabs_scaling.py`
# which attempts to show how as the number of modes increases
# the less and less likely it is a single mode, multi-photon output
# will be found

import boson_sampling as bs
from sympy.utilities.iterables import multiset_permutations
from strawberryfields.utils import random_interferometer
import numpy as np

# Generate Random Unitary
unitary_mat = random_interferometer(40)

# 2 photons, for interferometer of 40 modes
arr_zero = np.zeros(40, dtype=np.uintc)
photons = np.array([1] * 2, dtype=np.uintc)
arr_zero[:2] = photons
photons_in = arr_zero.tolist()

# store results
results_sum = 0

for photons_out in multiset_permutations(photons_in):
    result = bs.output_probability(photons_in, photons_out,
                                   unitary_mat)
    print("Probability of photon output {0} : {1}".format(photons_out, result))
    results_sum += result

print("Sum of all probabilities", results_sum)