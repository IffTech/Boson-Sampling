# Boson Sampling Library

The following library was developed to better understand
[Aaronson-Arkhipov Boson Sampling (AABS)](https://arxiv.org/pdf/1011.3245.pdf) 
and its potential for proving quantum supremacy by simulating
the behavior of individual photon fock state inputs through a 
random unitary based linear interferometer.

All functions are found in the `boson_sampling.py` file, which is invoked
by the other demonstration scripts.

## Credits

The following resources were used to develop the main functions 
behind library:

### Videos 

[Quantum Supremacy via Boson Sampling: Theory and Practice | Quantum Colloquium](https://www.youtube.com/watch?v=jhBeK9y6DCo) by the Perimeter Institute with Scott Aaronson as the guest speaker.

Provides the formula in the first few minutes for calculating the probability of a certain photon output configuration (although the papers below also have equivalent formulations).

[Quantum Complexity Theory: Lecture 9 - Boson Sampling](https://www.youtube.com/watch?v=RKH1jvNb0Vc)
by Sevag Gharibian

Provided an excellent explanation of the column and row indexing/copying required to generate a matrix, which is the basis for both the default and memory efficient implementations of the submatrix generator in the library.

[Generating integer partitions](https://jeromekelleher.net/generating-integer-partitions.html)
by Jerome Kelleher

Provided the integer partitioning function which is used to help generate all possible output photon states
in `gen_output_configurations()` function

[Get all permutations of a numpy array](https://stackoverflow.com/a/41210450)
by Bill Bell 

Provided a method of using `sympy` to generate all unique permutations of a given
numpy array (works with ordinary lists too) and is part of the 
`gen_output_configurations()` function

### Papers

[An introduction to boson-sampling](http://arxiv.org/abs/1406.6767)
by Gard et al.

[A detailed study of Gaussian Boson Sampling](http://arxiv.org/abs/1801.07488)
by Kruse et al.

## Websites

[Boson sampling and the permanent](https://strawberryfields.ai/photonics/demos/run_boson_sampling.html)

provided the basis for code in `sf_single_photon_test.py` and `sf_multiple_photon_test.py`

### Additional Resources

These are resources that did not contribute directly to the code but
were invaluable in learning more about boson sampling:

[Experimental Boson Sampling](https://www.nature.com/articles/nphoton.2013.102)
by Tillman et al.

[Introduction to boson-sampling](https://www.youtube.com/watch?v=tlgYp-I5dvs)
by Peter Rohde

[Gaussian Boson Sampling Complexity - Part 1](https://www.youtube.com/watch?v=G3SGty8sbnw)
by Andrew Tanggara 

Note: I didn't watch much of this presentation compared to others but
it seemed to be very well made and is given by Alex Arkhipov himself!
[Quantum computing with noninteracting particles - Alex Arkhipov](https://www.youtube.com/watch?v=fpRgp8sxcyo)
