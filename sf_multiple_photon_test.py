# Worked based on: 
# https://strawberryfields.ai/photonics/demos/run_boson_sampling.html

# Use Xanadu's strawberryfields to simulate boson sampling for multiple
# photons


import strawberryfields as sf
from strawberryfields.ops import *
from strawberryfields.utils import random_interferometer
from sympy.utilities.iterables import multiset_permutations
import numpy as np

import boson_sampling as bs

boson_sampling = sf.Program(4)

unitary_mat = random_interferometer(4)

photons_in = [0, 3, 2, 2]

with boson_sampling.context as q:

    # prepare input fock states
    for mode, photon_ct in enumerate(photons_in):
        if photon_ct == 0:
            Vac | q[mode]
        else:
            Fock(photon_ct) | q[mode]

    # random interferometer
    Interferometer(unitary_mat, mesh="rectangular") | q

    # MeasureFock() | q

eng = sf.Engine(backend="fock", backend_options={"cutoff_dim": (sum(photons_in) + 1)})
results = eng.run(boson_sampling)

probs = results.state.all_fock_probs()
prob_sum = 0

for photons_out in bs.gen_output_configurations(sum(photons_in), len(photons_in)):
    print("output configuration: {0}, probability: {1}"
          .format(photons_out, probs[tuple(photons_out)]))

    prob_sum += probs[tuple(photons_out)]

print("sum of probabilities: {0}".format(prob_sum))