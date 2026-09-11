import numpy as np
from physics_informed_neural_operators.pde import laplacian_1d, heat_residual

def test_laplacian_linear_function(): assert np.allclose(laplacian_1d(np.arange(5.), 1), 0)

def test_heat_residual_shape(): assert heat_residual(np.zeros(5), np.zeros(5), .1, .1, 1).shape == (3,)
