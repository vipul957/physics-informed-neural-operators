from __future__ import annotations
import numpy as np
def physics_loss(data_residual, physics_residual, boundary_residual, physics_weight=1., boundary_weight=1.):
    """Combine data, PDE, and boundary mean-square residuals."""
    if physics_weight < 0 or boundary_weight < 0: raise ValueError("weights must be non-negative")
    mse=lambda x: float(np.mean(np.asarray(x,dtype=float)**2))
    return mse(data_residual)+physics_weight*mse(physics_residual)+boundary_weight*mse(boundary_residual)
