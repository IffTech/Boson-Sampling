# See `bs_aabs_setup.py` for more details 

import boson_sampling as bs
from sympy.utilities.iterables import multiset_permutations
from strawberryfields.utils import random_interferometer
import numpy as np


for num_modes in range(5, 60):

    unitary_mat = random_interferometer(num_modes)

    arr_zero = np.zeros(num_modes, dtype=np.uintc)
    photons = np.array([1] * 3, dtype=np.uintc)
    arr_zero[:3] = photons
    photons_in = arr_zero.tolist()

    # store results
    results_sum = 0

    for photons_out in multiset_permutations(photons_in):
        result = bs.output_probability(photons_in, photons_out,
                                    unitary_mat)
        #print("Probability of photon output {0} : {1}".format(photons_out, result))
        results_sum += result

    print("Sum of all probabilities", results_sum)