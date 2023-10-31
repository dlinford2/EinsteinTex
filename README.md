# EinsteinTex

## Use

EinsteinTex is a Python package designed to make your life easier when working with LaTeX documents for General Relativity computations and theory. This package provides a convenient way to generate LaTeX files containing equations, metrics, and tensors commonly used in General Relativity research and education.

## Features

Automatic LaTeX Generation: EinsteinTex automatically generates LaTeX code for various components, including Metric Tensors, Christoffel Symbols, Riemann Curvature Tensors, Ricci Tensors, Ricci Scalars, and Einstein Tensors.
Customization: You can easily customize the output file name and the document title to suit your needs.
Optimized for General Relativity: EinsteinTex is designed specifically for use in General Relativity research, making it a valuable tool for students, educators, and researchers in the field.

## Installation

You can install EinsteinTex via pip:

> pip install EinsteinTex

## Getting Started

Here's a simple example of how to create a LaTeX document using EinsteinTex:

```python
from EinsteinTex import EinsteinTex

# Initialize EinsteinTex with the desired output file name
einstein_tex = EinsteinTex('my_gr_document.tex')

# Print the preamble with your desired title
einstein_tex.print_preamble('General Relativity Computations')

# Create and print the FLRW Metric Tensor -- Note that the user can specify their own metric instead
metric_tensor = einstein_tex.create_FLRW_metric_tensor()
einstein_tex.print_metric_tensor(metric_tensor)

# Calculate and print the Christoffel Symbols
christoffel = einstein_tex.calculate_christoffel_symbols(metric_tensor)
einstein_tex.print_christoffel_symbols(christoffel)

# Add more computations and sections as needed

# Print the end of the document
einstein_tex.print_end()
```

You can also have EinsteinTex print an entire document, containing a number of different tensors, etc, from a given metric, e.g.,

```python
from EinsteinTex import EinsteinTex

# Initialize EinsteinTex with the desired output file name
einstein_tex = EinsteinTex('my_gr_document.tex')
einstein_tex.print_entire_document(metric_tensor, 'FLRW Results')
```

Users can specify their own metric by modifying the following code snippet:

```python
import sympy as sp
from einsteinpy.symbolic import MetricTensor

t, r, theta, phi = sp.symbols('t r theta phi') # Define a set of symbols to use for coordinates
a = sp.Function('a')(t)  # Scale factor
tensor = MetricTensor( # Define the metric itself
    sp.Array([
        [-1, 0, 0, 0],
        [0, a**2, 0, 0],
        [0, 0, a**2, 0],
        [0, 0, 0, a**2]
    ]),
    syms=(t, r, theta, phi)
)
```

## Contributions

Contributions and bug reports are welcome! Feel free to open issues or submit pull requests on GitHub.
