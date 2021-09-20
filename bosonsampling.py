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

import numpy as np
import scipy as sp
import thewalrus
from sympy.utilities.iterables import multiset_permutations


def gen_submatrix(photons_in, photons_out, unitary_mat):
    """Generates a submatrix from a given unitary matrix representing
    a linear interferometer whose permanent can be used to calculate
    photon output configuration probabilities.

    Args:
        photons_in ([int]):
            A list with each integer entry representing the number
            of individual photons in the input modes for the
            interferometer
        photons_out ([int]):
            A list with each integer entry representing the number
            of individual photons at the ouptut modes for the
            interferometer
        unitary_mat (np.array):
            A unitary matrix describing an interferometer

    Raises:
        ValueError:
            If the number of photons inputted do not equal the number
            of photons output, a ValueError is raised.

    Returns:
        np.array:
            A submatrix built from the originally inputted `unitary_mat`
            argument
    """

    if sum(photons_in) != sum(photons_out):
        raise ValueError("Number of photons inputted is not equal"
                         "to number outputted!")

    photon_count = sum(photons_in)

    # Generate a matrix consisting solely of columns from the main
    # unitary matrix. Row dimension is preserved but the number of
    # columns is equal to the number of photons.
    col_mat = np.zeros((unitary_mat.shape[0], photon_count),
                       dtype=np.cdouble)

    # Obtain columns for `col_mat`, based on the input photon
    # configuration.
    # Given a photon input [1,2,0,0], the first column of the main
    # unitary matrix is copied, then the second column is copied
    # TWICE, with no other columns copied to created an (N x 3) submatrix
    # (where N is whatever the row dimension is on the main unitary)
    col_idx = 0
    for col, val in enumerate(photons_in):
        for i in range(val):
            col_mat[:, col_idx] = unitary_mat[:, col]
            col_idx += 1

    # Create the final submatrix, which should be (number of photons in
    # x number of photons out) large
    sub_mat = np.zeros((photon_count, photon_count), dtype=np.cdouble)

    # Looking at the output photon configuration, rows from `col_mat`
    # are indexed and added to the final submatrix.
    # If the output is [1,2,0,0] then the first row of `col_mat` is
    # copied once, then the second row copied TWICE to create the final
    # submatrix (going off the previous example, should be 3 x 3)
    row_idx = 0
    for row, val in enumerate(photons_out):
        for i in range(val):
            sub_mat[row_idx, :] = col_mat[row, :]
            row_idx += 1

    return sub_mat


def gen_submatrix_memeff(photons_in, photons_out, unitary_mat):
    """A memory-efficient implementation of `gen_submatrix`, does not
    require the creation of an intermediate, column-only submatrix.

    Args:
        photons_in ([int]):
            A list with each integer entry representing the number
            of individual photons in the input modes for the
            interferometer
        photons_out ([int]):
            A list with each integer entry representing the number
            of individual photons at the ouptut modes for the
            interferometer
        unitary_mat (np.array):
            A unitary matrix describing an interferometer

    Raises:
        ValueError:
            If the number of photons inputted do not equal the number
            of photons output, a ValueError is raised.

    Returns:
        np.array:
            A submatrix built from the originally inputted `unitary_mat`
            argument
    """

    if sum(photons_in) != sum(photons_out):
        raise ValueError("Number of photons inputted is not equal"
                         "to number ouptutted!")

    sub_mat = np.zeros(photons_in.sum(), photons_in.sum(), dtype=np.uintc)

    col_idx = 0
    for photons_in_idx, photons_in_ct in enumerate(photons_in):
        if photons_in_ct > 0:
            for _ in range(photons_in_ct):
                col = unitary_mat[:, photons_in_idx]  # get the column
                row_idx = 0
                for photons_out_idx, photons_out_ct in enumerate(photons_out):
                    if photons_out_ct > 0:
                        for _ in range(photons_out_ct):
                            sub_mat[row_idx, col_idx] = col[photons_out_idx]
                            row_idx += 1
                col_idx += 1


def output_probability(photons_in, photons_out, unitary_mat):
    """Calculate the probability of a certain photon output
    configuration (n number of photons across m modes) given the
    inputted photons and the unitary matrix representing a
    linear interferometer

    Args:
        photons_in ([int]):
            A list with each integer entry representing the number
            of individual photons in the input modes for the
            interferometer
        photons_out ([int]):
            A list with each integer entry representing the number
            of individual photons at the ouptut modes for the
            interferometer
        unitary_mat (np.array):
            A unitary matrix describing an interferometer

    Returns:
        float: probability photons will be detected in the given
        `photons_out` configuration
    """

    sub_mat = gen_submatrix(photons_in, photons_out, unitary_mat)

    modulus_squared = np.abs(thewalrus.perm(sub_mat))**2
    denom = (sp.special.factorial(photons_in).prod() *
             sp.special.factorial(photons_out).prod())

    return modulus_squared / denom


def _accel_asc(n):
    """Jerome Kelleher's integer partition generating function,
    obtained from: (https://jeromekelleher.net/generating-integer-
    partitions.html).

    Generates Integer partitions of any positive integer, i.e.
    all positive integer sequences that sum up to the integer in
    question

    Args:
        n (int):
            The integer to generate partitions for

    Yields:
        [int]:
            A list of integers that have a sum equal to n
    """
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]


def gen_output_configurations(num_photons, num_modes):
    """Generate all possible output photon configurations given the
    number of photons on input and the number of modes present in the
    input.

    Args:
        num_photons (int):
            The total number of photons inputted into the system
        num_modes (int):
            The total number of modes photons can be present in

    Yields:
        [type]: [description]
    """

    # generate all possible photon outputs that sum up to the
    # number of photons inputted.
    # Ex: 5 photon input can produce an output of [5], [4,1],
    # [3,2],...[1,1,1,1,1]
    # Note that the notation above does NOT account for mode limitations
    # so Kelleher's function (see `_accel_asc()``) may generate a
    # configuration that is not physically feasible (exceeds number of
    # available modes).
    # The `len(num_photons_partition <= num_modes)` ensures this
    # does not happen.
    for num_photons_partition in _accel_asc(num_photons):
        if len(num_photons_partition) <= num_modes:
            # certain outputs may fall shy of the number of modes
            # and need to be zero-padded
            zero_arr = [0] * num_modes
            for idx, val in enumerate(num_photons_partition):
                zero_arr[idx] = val
            # multiset_permutation usage to generate unique permutations
            # of a list:
            # (https://stackoverflow.com/a/41210450)
            # for each properly padded output, generate all unique
            # permutations of that output.
            # Ex: [1,0,0,0] can produced [1,0,0,0], [0,1,0,0], [0,0,1,0]
            # ,etc.
            for p in multiset_permutations(zero_arr):
                yield p
