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

# A basis for the work in `bs_aabs_scaling.py`
# which attempts to show how as the number of modes the interferometer
# can take increases, the less and less likely it is a single mode,
# multi-photon fock state output (a "collision" as its referred to
# in the Aaronson-Arkhipov paper) will be found given multiple,
# single photon fock states inputted

# In this instance a fixed-sized (albeit large) random interferometer
# set up is used. In `bs_aabs_scaling.py` the interferometer will
# increase in size

import bosonsampling as bs
from sympy.utilities.iterables import multiset_permutations
from strawberryfields.utils import random_interferometer
import numpy as np

# Generate large random interferometer
random_interferometer = random_interferometer(40)

# two single photon fock states are created for input. Note
# how the modes selected are right next to each other, as part of
# the original Aaronson-Arkhipov proposal
arr_zero = np.zeros(40, dtype=np.uintc)
photons = np.array([1] * 2, dtype=np.uintc)
arr_zero[:2] = photons
photons_in = arr_zero.tolist()

# store sum of total probabilities for later sanity check
# all output configuration probabilities should add up to one
probability_sum = 0


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