# A single photon is fed into an interferometer and the probability of
# the photon being detected in another mode are calculated.

import boson_sampling as bs
from strawberryfields.utils import random_interferometer

# Generate Random (4 x 4) unitary to represent an interferometer
# with 4 mode I/O
unitary_mat = random_interferometer(4)

# Input configuration, one photon down first mode,
# no photons down other modes
photons_in = [1, 0, 0, 0]

# store sum of total probabilities for later sanity check
# all output configuration probabilities should add up to one
results_sum = 0

# `gen_output_configurations()` generates all possible photon output
# configurations. In this particular instance, an input of
# [1, 0, 0, 0] will give four possible unique permutations.
for photons_out in bs.gen_output_configurations(sum(photons_in),
                                                len(photons_in)):
    # Given the input and output configurations, as well as the
    # unitary matrix representing the inferometers, calculate the
    # probability the particular photon output will be detected
    result = bs.output_probability(photons_in, photons_out,
                                   unitary_mat)
    print("Probability of photon output {0} : {1}".format(photons_out, result))
    results_sum += result

# Sanity check, all probabilities should sum up to 1
print("Sum of all probabilities", results_sum)
