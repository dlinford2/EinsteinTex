import sympy as sp
from einsteinpy.symbolic import ChristoffelSymbols, MetricTensor, RicciTensor, RicciScalar, RiemannCurvatureTensor, EinsteinTensor

METRIC_DIMENSION = 4

class EinsteinTexClass:
    
    def __init__(self, output_file_name):
        self.output_file_name = output_file_name
        
    # Custom function to format derivatives
    def format_derivative(self, expr):
        if isinstance(expr, sp.Derivative):
            return sp.latex(expr, mode='inline')
        else:
            return sp.latex(expr)

    def print_preamble(self, title):
        with open(self.output_file_name, 'a') as output_file:
            preamble = (
                '\\documentclass{article}\n'
                '\\usepackage{amsmath}\n'
                '\\usepackage{geometry}\n'
                '\\geometry{margin=1.5in}\n'
                '\\title{' + title + '}\n'
                '\\begin{document}\n'
                '\\maketitle\n'
            )
            output_file.write(preamble)

    def print_end(self):
        with open(self.output_file_name, 'a') as output_file:
            end = '\\end{document}\n'
            output_file.write(end)
    
    def print_horizontal_space(self):
        with open(self.output_file_name, 'a') as output_file:
            output_file.write('\\\\\n')
            output_file.write('\\\\')
    

    # Define the FLRW Metric Tensor
    def create_FLRW_metric_tensor(self):
        t, r, theta, phi = sp.symbols('t r theta phi')
        a = sp.Function('a')(t)  # Scale factor
        tensor = MetricTensor(
            sp.Array([
                [-1, 0, 0, 0],
                [0, a**2, 0, 0],
                [0, 0, a**2, 0],
                [0, 0, 0, a**2]
            ]),
            syms=(t, r, theta, phi)
        )
        return tensor

    def print_metric_tensor(self, metric_tensor):
        with open(self.output_file_name, 'a') as output_file:
            output_file.write('\n')
            output_file.write("\n\\section{Metric Tensor:}\n")
            latex_tensor = sp.latex(metric_tensor.tensor())
            output_file.write('\\begin{equation*}')
            output_file.write('g_{\\mu\\nu} = ' + latex_tensor)
            output_file.write('\\end{equation*}')
            output_file.write('\n')

    def calculate_christoffel_symbols(self, metric):
        christoffel = ChristoffelSymbols.from_metric(metric)
        return christoffel

    def print_christoffel_symbols(self, christoffel):
        with open(self.output_file_name, 'a') as output_file:
            output_file.write('\n')
            output_file.write("\n\\section{Christoffel Symbols:}\n")
            metric_dimension = METRIC_DIMENSION
            zero_values = []
            christ_output = '\\\\\n\\\\\n'
            for i in range(metric_dimension):
                for j in range(metric_dimension):
                    for k in range(metric_dimension):
                        symbol = f'$\\Gamma^{{{i}}}_' + f'{{{j}{k}}}$'
                        expression = self.format_derivative(christoffel[i][j][k])
                        if expression == str(0):
                            if symbol not in zero_values:
                                zero_values.append(symbol)
                        else:
                            christ_output += f"{symbol} = ${expression}$, "
            zero_string = ' = '.join(zero_values) + ' = $0$\n' if zero_values else ''
            if(len(zero_values) > 0):
                output_file.write(zero_string)
                self.print_horizontal_space()
            output_file.write(christ_output[:-2] + '\n')
    
    def calculate_riemann_curvature_tensor(self, christoffel):
        riemann = RiemannCurvatureTensor.from_christoffels(christoffel)
        return riemann

    def print_riemann_curvature_tensor(self, riemann):
        with open(self.output_file_name, 'a') as output_file:
            output_file.write('\n')
            metric_dimension = METRIC_DIMENSION
            output_file.write("\n\\section{Riemann Curvature Tensor:}\n")
            zero_values = []
            riemann_output = '\\\\\n\\\\\n'
            for a in range(metric_dimension):
                for b in range(metric_dimension):
                    for c in range(metric_dimension):
                        for d in range(metric_dimension):
                            symbol = f'$R^{{{a}}}_{{{b}{c}{d}}}$'
                            expression = self.format_derivative(riemann.tensor()[a, b, c, d])
                            if expression == str(0):
                                if symbol not in zero_values:
                                    zero_values.append(symbol)
                            else:
                                riemann_output += f"{symbol} = ${expression}$, "
            zero_string = ' = '.join(zero_values) + ' = $0$\n' if zero_values else ''
            if(len(zero_values) > 0):
                output_file.write(zero_string)
                self.print_horizontal_space()
            output_file.write(riemann_output[:-2] + '\n')

    
    def calculate_ricci_tensor(self, riemann):
        ricci_tensor = RicciTensor.from_riemann(riemann)
        return ricci_tensor

    def print_ricci_tensor(self, ricci_tensor):
        with open(self.output_file_name, 'a') as output_file:
            output_file.write('\n')
            metric_dimension = METRIC_DIMENSION
            output_file.write("\n\\section{Ricci Tensor:}\n")
            zero_values = []
            ricci_output = '\\\\\n\\\\\n'
            for i in range(metric_dimension):
                for j in range(metric_dimension):
                    symbol = f'$R' + f'_{{{i}{j}}}$'
                    expression = self.format_derivative(ricci_tensor[i][j])
                    if expression == str(0):
                        if symbol not in zero_values:
                            zero_values.append(symbol)
                    else:
                        ricci_output += f"{symbol} = ${expression}$, "
            zero_string = ' = '.join(zero_values) + ' = $0$\n' if zero_values else ''
            if(len(zero_values) > 0):
                output_file.write(zero_string)
                self.print_horizontal_space()
            output_file.write(ricci_output[:-2] + '\n')

    def calculate_ricci_scalar(self, ricci_tensor):
        ricci_scalar = RicciScalar.from_riccitensor(ricci_tensor)
        return ricci_scalar

    def print_ricci_scalar(self, ricci_scalar):
        with open(self.output_file_name, 'a') as output_file:
            output_file.write('\n')
            output_file.write("\n\\section{Ricci Scalar:}")
            output_file.write('\n')
            expression = sp.latex(ricci_scalar.expr)
            output_file.write('\\begin{center}')
            output_file.write(f"R = ${expression}$")
            output_file.write('\\end{center}')
            output_file.write('\n')
    
    def calculate_einstein_tensor(self, metric):
        einstein = EinsteinTensor.from_metric(metric)
        return einstein

    def print_einstein_tensor(self, einstein):
        with open(self.output_file_name, 'a') as output_file:
            metric_dimension = METRIC_DIMENSION
            output_file.write("\n\section{Einstein Tensor:}\n")
            zero_values = []
            einstein_output = '\\\\\n\\\\\n'
            for i in range(metric_dimension):
                for j in range(metric_dimension):
                    symbol = f'$G' + f'_{{{i}{j}}}$'
                    expression = self.format_derivative(einstein[i][j])
                    if expression == str(0):
                        if symbol not in zero_values:
                            zero_values.append(symbol)
                    else:
                        einstein_output += f"{symbol} = ${expression}$, "
            zero_string = ' = '.join(zero_values) + ' = $0$\n' if zero_values else ''
            if(len(zero_values) > 0):
                output_file.write(zero_string)
                #self.print_horizontal_space()
            output_file.write(einstein_output[:-2] + '\n')
            
    def print_entire_document(self, metric, title):
        
        self.print_preamble(title)
        

        self.print_metric_tensor(metric)

        # Calculate the Christoffel Symbols
        christoffel = self.calculate_christoffel_symbols(metric)
        self.print_christoffel_symbols(christoffel)

        # Calculate the Riemann Curvature Tensor
        riemann = self.calculate_riemann_curvature_tensor(christoffel)
        self.print_riemann_curvature_tensor(riemann)

        # Calculate the Ricci Tensor
        ricci_tensor = self.calculate_ricci_tensor(riemann)
        self.print_ricci_tensor(ricci_tensor)

        # Calculate the Ricci Scalar
        ricci_scalar = self.calculate_ricci_scalar(ricci_tensor)
        self.print_ricci_scalar(ricci_scalar)

        # Calculate the Einstein Tensor
        einstein = self.calculate_einstein_tensor(metric)
        self.print_einstein_tensor(einstein)

        self.print_end()
