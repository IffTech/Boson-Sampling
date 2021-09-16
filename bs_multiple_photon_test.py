# multiple photons are fed into an interferometer and the probability of
# the photons being detected in different modes are calculated.


import boson_sampling as bs
from strawberryfields.utils import random_interferometer

# Generate Random (4 x 4) unitary to represent an interferometer
# with 4 mode I/O
random_interferometer = random_interferometer(4)

# Input configuration, multiple photons in different modes, with
# some modes containing more than one photon
photons_in = [3, 1, 0, 1]

# store sum of total probabilities for later sanity check
# all output configuration probabilities should add up to one
probability_sum = 0

# `gen_output_configurations()` generates all possible photon output
# configurations. Unlike the `bs_single_photon_test.py` demonstration,
# it is no longer sufficient to get permutations of the input.
# For example, there is a non-zero probability that all five photons
# will be detected on any one mode!
for photons_out_configuration in bs.gen_output_configurations(sum(photons_in),
                                                              len(photons_in)):
    # Given the input and output configurations, as well as the
    # unitary matrix representing the inferometers, calculate the
    # probability the particular photon output will be detected
    output_probability = bs.output_probability(photons_in,
                                               photons_out_configuration,
                                               random_interferometer)
    print("Probability of photon output {0} : {1}"
          .format(photons_out_configuration, output_probability))
    probability_sum += output_probability

print("Sum of all probabilities", probability_sum)
