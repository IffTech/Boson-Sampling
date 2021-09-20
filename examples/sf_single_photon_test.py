# Worked based on: 
# https://strawberryfields.ai/photonics/demos/run_boson_sampling.html

# Use Xanadu's strawberryfields to simulate boson sampling for a single
# photon.

# Use Xanadu's strawberryfields to simulate boson sampling for a
# multi-photon input instead of `boson_sampling`'s system
# see `bs_single_photon_test.py` for the `boson_sampling` equivalent.

import strawberryfields as sf
from strawberryfields.ops import *
from strawberryfields.utils import random_interferometer
from sympy.utilities.iterables import multiset_permutations
import numpy as np

import bosonsampling as bs

boson_sampling = sf.Program(4)

# Create a random interferometer
random_interferometer = random_interferometer(4)

photons_in = [0, 0, 0, 1]

# Create the Strawberryfields program that will simulate the sampling
# process. The "4" indicates there are 4 photonic modes that will be
# used, in accordance with the 4 modes declared above
boson_sampling = sf.Program(4)

with boson_sampling.context as q:

    # Prepare the input fock states,
    # The "index" in `photons_in` denotes the exact mode
    # while the value at the index denotes the number of photons
    # in the Fock state
    for mode, photon_ct in enumerate(photons_in):
        if photon_ct == 0:
            Vac | q[mode]
        else:
            Fock(photon_ct) | q[mode]

    # Add the random interferometer to the program
    Interferometer(random_interferometer, mesh="rectangular") | q

    # MeasureFock() | q

# Configure the simulator the strawberryfields program will run on.
# Specify the simulation will simulate up to `sum(photons_in) + 1`
# Fock amplitudes so |0> + |1> ... |sum(photons_in)>
eng = sf.Engine(backend="fock", backend_options={"cutoff_dim": (sum(photons_in) + 1)})
results = eng.run(boson_sampling)

# Get all fock state probabilities
probs = results.state.all_fock_probs()

# ensure that all photon output configurations have been accounted for,
# sanity check dictates all probabilities must sum to one.
prob_sum = 0

# Iterate through all possible photon output configurations and print
# their probabilities out
for photons_out in bs.gen_output_configurations(sum(photons_in), len(photons_in)):
    print("output configuration: {0}, probability: {1}"
          .format(photons_out, probs[tuple(photons_out)]))

    prob_sum += probs[tuple(photons_out)]

print("sum of probabilities: {0}".format(prob_sum))
