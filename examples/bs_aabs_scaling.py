# Boson Sampling Library - A library to help better understand Aaronson-Arkhipov Boson Sampling (AABS)
# Copyright (C) 2021  If and Only If (Iff) Technologies

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

## Program Description: 

# See `bs_aabs_setup.py` for more details

import bosonsampling as bs
from sympy.utilities.iterables import multiset_permutations
from strawberryfields.utils import random_interferometer
import numpy as np


for num_modes in range(5, 50):

    # Generate Interferometer
    random_interferometer = random_interferometer(num_modes)

    # Generate two modes with single photon inbuts
    arr_zero = np.zeros(num_modes, dtype=np.uintc)
    photons = np.array([1] * 2, dtype=np.uintc)
    arr_zero[:2] = photons
    photons_in = arr_zero.tolist()

    # sanity check, ensure for each run all output probabilities sum up to one
    probability_sum = 0

    # generate all possible output configurations
    for photon_out_configuration in bs.gen_output_configurations(sum(photons_in),
                                                                 len(photons_in)):
        # Given the input and output configurations, as well as the
        # unitary matrix representing the inferometers, calculate the
        # probability the particular photon output will be detected
        output_probability = bs.output_probability(photons_in,
                                                   photon_out_configuration,
                                                   random_interferometer)
        print("Probability of photon output {0} : {1}"
              .format(photon_out_configuration, output_probability))
        probability_sum += output_probability

    print("Sum of all probabilities", probability_sum)