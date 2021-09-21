# Boson Sampling Library

The following library was developed to better understand
[Aaronson-Arkhipov Boson Sampling (AABS)](https://arxiv.org/pdf/1011.3245.pdf) 
(the acronym "AABS" for the particular Boson Sampling setup was encountered in Kruse et al.'s paper [A detailed study of Gaussian Boson Sampling](http://arxiv.org/abs/1801.07488))
by simulating the behavior of fock state inputs through a random unitary based linear interferometer and calculating the probabilities of certain fock state ouptuts.


## Installation

You can either

```
pip install bosonsampling
```

or clone the library and within the directory (as well as having your favorite python environment activate) run the following:

```
pip install .
```

## Usage

1. Import `bosonsampling` for core functionality and the `random_interferometer()` function from `strawberryfields.utils` to set up a random interferometer.

    ```python
    import bosonsampling as bs
    from strawberryfields.utils import random_interferometer
    ```

2. Create your random_interferometer

    ```python
    # creates a 4x4 unitary matrix
    random_interferometer = random_interferometer(4)
    ```

3. Create your input Fock states

    ```python
    # 0 photons in mode 1
    # 1 photon in mode 2
    # 3 photons in mode 3
    # 4 photons in mode 4
    photons_in = [0,1,3,4]
    ```

4. You can either:

    a. Measure the probability of a certain output state 

    ```python
    photons_out = [0,0,0,8]
    output_probability = bs.output_probability(photons_in, photons_out, random_interferometer)
    ```

    b. OR Measure the probability of ALL output states

    ```python
    for photon_out_configuration in bs.gen_output_configurations(sum(photons_in), len(photons_in)):

        output_probability = bs.output_probability(photons_in, photon_out_configuration, random_interferometer)

        print("Probability of photon output {0} : {1}".format(photon_out_configuration, output_probability))
    ```

## Example Files

Example files have been included to explain different possible usages with `bosonsampling` and can be found in the `examples` folder.

All files prefixed with `bs_` are dedicated solely to `bosonsampling.py`. 

However, there are files prefixed with `sf_` that show how identical behavior can be obtained with [Strawberry Fields](https://strawberryfields.ai/) (great for verifying results) and how `bosonsampling` can be used in conjunction with it as well.

* `bs_single_photon_test.py` - demonstrates a single photon entering the interferometer and calculating the probability of all possible outputs
* `bs_multiple_photon_test.py` - demonstrates multiple photons entering the interferometer and calculating the probability of all possible outputs, emphasizing how `gen_output_configurations()` can come in handy for such scenarios.
* `bs_aabs_setup.py` - demonstrates a setup similar to what would be called for in the Aaronson-Arkhipov paper with a multiple, single-photon fock state input with the modes right next to eachother and how the probability of detecting a "collision" (an output state that has multiple photons in a single mode) is incredibly low
* `bs_aabs_scaling.py` - Is essentially a duplicate of `bs_aabs_setup.py` but has an outer loop designed to make the interferometer larger with each iteration but keeps the number of inputted photons identical so one can observe the decreasing probability of collision.

* `sf_single_photon_test.py` - Is `bs_single_photon_test.py` but implemented with Xanadu's Strawberry Fields framework
* `sf_multiple_photon_test.py` - Is `bs_multiple_photon_test.py` but implemented with Xanadu's Strawberry Fields framework.

## Contributing

If you find a bug or have an idea to improve the library, please feel free to either make an Issue or a Pull Request with your suggested changes! If you are contributing code, please do note that this library attempts to follow the [PEP-8 Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/#package-and-module-names) as well as using [Google Style Python Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

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
provided the origin of the AABS acronym used throughout the project and has a very nice illustration on page 2 that describes the column and row indexing necessary to generate the proper submatrix that Sevag Gharibian also goes over.

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

Note: This video was barely consulted, but appred to be very well made and is given by Alex Arkhipov himself!
[Quantum computing with noninteracting particles - Alex Arkhipov](https://www.youtube.com/watch?v=fpRgp8sxcyo)
