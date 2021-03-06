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

# A single photon is fed into an interferometer and the probability of
# the photon being detected in another mode are calculated.

import bosonsampling as bs
from strawberryfields.utils import random_interferometer

# Generate Random (4 x 4) unitary to represent an interferometer
# with 4 mode I/O
random_interferometer = random_interferometer(4)

# Input configuration, one photon down first mode,
# no photons down other modes
photon_in = [1, 0, 0, 0]

# store sum of total probabilities for later sanity check
# all output configuration probabilities should add up to one
probability_sum = 0

# `gen_output_configurations()` generates all possible photon output
# configurations. In this particular instance, an input of
# [1, 0, 0, 0] will give four possible unique permutations.
for photon_out_configuration in bs.gen_output_configurations(sum(photon_in),
                                                             len(photon_in)):
    # Given the input and output configurations, as well as the
    # unitary matrix representing the inferometers, calculate the
    # probability the particular photon output will be detected
    output_probability = bs.output_probability(photon_in,
                                               photon_out_configuration,
                                               random_interferometer)
    print("Probability of photon output {0} : {1}"
          .format(photon_out_configuration, output_probability))
    probability_sum += output_probability

# Sanity check, all probabilities should sum up to 1
print("Sum of all probabilities", probability_sum)
