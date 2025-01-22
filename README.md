# EinsteinTex

## Use

EinsteinTex is a Python package designed to make your life easier when working with LaTeX documents for comptutations related to General Relativity. This package provides a convenient way to generate LaTeX files containing equations, metrics, and tensors commonly used in General Relativity.

## Features

* Automatic LaTeX Generation: EinsteinTex automatically generates LaTeX code for various components, including Metric Tensors, Christoffel Symbols, Riemann Curvature Tensors, Ricci Tensors, Ricci Scalars, and Einstein Tensors.

* Customization: You can easily customize the output file name and the document title to suit your needs.

* Optimized for General Relativity: EinsteinTex is designed specifically for use in General Relativity research, making it a valuable tool for students, educators, and researchers in the field.

## Installation

You can install EinsteinTex via pip:

``` bash
pip install EinsteinTex
```

## Getting Started

Here's a simple example of how to create a LaTeX document using EinsteinTex:

```python
from EinsteinTex import EinsteinTexClass

# Initialize EinsteinTex with the desired output file name
einstein_tex = EinsteinTexClass('my_gr_document.tex')

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
from EinsteinTex import EinsteinTexClass

# Initialize EinsteinTex with the desired output file name
einstein_tex = EinsteinTexClass('my_gr_document.tex')
metric_tensor = einstein_tex.create_FLRW_metric_tensor()
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

## Troubleshooting: `ModuleNotFoundError: No module named 'EinsteinTex'`

If you encounter a `ModuleNotFoundError` after installing **EinsteinTex**, this issue may be caused by Python not recognizing the package's installation path, especially when using an editable installation (`pip install -e .`). Follow these steps to fix the issue:

### 1. Verify Installation

Run the following command to check where **EinsteinTex** is installed:

```bash
pip show EinsteinTex
```

Look for the `Location` or `Editable project` location field in the output. This indicates where the package is installed. For example:

```
Location: /path/to/EinsteinTex
Editable project location: /path/to/EinsteinTex
```

If the package is installed in editable mode, Python may not automatically detect the installation.

### 2. Check Python's Search Path

Verify that the installation directory is included in Python's search path:

```python
import sys
print(sys.path)
```

If the installation directory (e.g., `/path/to/EinsteinTex`) is not listed, Python won’t recognize the package.

### 3. Fix the Search Path

To fix the issue, add the installation directory to Python’s search path manually in your script or notebook:

```python
import sys
sys.path.append('/path/to/EinsteinTex')  # Replace with your actual path
from EinsteinTex import EinsteinTex
```

This will allow Python to find the package.

### 4. Permanent Fix (Optional)

For a permanent fix, set the `PYTHONPATH` environment variable to include the installation directory. For example:

```bash
export PYTHONPATH="/path/to/EinsteinTex:$PYTHONPATH"
```

You can add this line to your shell configuration file (e.g., .bashrc, .zshrc, etc.) to make it persistent across sessions.

### 5. Restart Your Environment

If you’re using an environment like Jupyter or Deepnote, restart the kernel after making these changes and try importing the package again:

```python
from EinsteinTex import EinsteinTex
```

### Need More Help?

By following these steps, you should be able to resolve any `ModuleNotFoundError` issues related to **EinsteinTex**. If the problem persists, feel free to [open an issue](https://github.com/dlinford2/EinsteinTex/issues) on this repository for further assistance.

## Contributions

Contributions and bug reports are welcome! Feel free to open issues or submit pull requests on GitHub.
