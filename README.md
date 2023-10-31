# EinsteinTex

## Use

EinsteinTex is a Python package designed to make your life easier when working with LaTeX documents for General Relativity computations and theory. This package provides a convenient way to generate LaTeX files containing equations, metrics, and tensors commonly used in General Relativity research and education.

## Features

Automatic LaTeX Generation: EinsteinTex automatically generates LaTeX code for various components, including Metric Tensors, Christoffel Symbols, Riemann Curvature Tensors, Ricci Tensors, Ricci Scalars, and Einstein Tensors.
Customization: You can easily customize the output file name and the document title to suit your needs.
Optimized for General Relativity: EinsteinTex is designed specifically for use in General Relativity research, making it a valuable tool for students, educators, and researchers in the field.

## Installation

You can install EinsteinTex via pip:

> pip install EinsteinTex==0.1

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

## Documentation

For detailed information on how to use EinsteinTex, you can refer to the documentation available on GitHub.

## Contributions

Contributions and bug reports are welcome! Feel free to open issues or submit pull requests on GitHub.
