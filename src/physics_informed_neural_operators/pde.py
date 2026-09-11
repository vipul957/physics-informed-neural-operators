"""Small finite-difference utilities for physics-informed experiments."""
from __future__ import annotations
import numpy as np

def laplacian_1d(u: np.ndarray, dx: float) -> np.ndarray:
    if dx <= 0 or len(u) < 3: raise ValueError("invalid grid")
    return (u[:-2] - 2*u[1:-1] + u[2:]) / dx**2

def heat_residual(u_now: np.ndarray, u_next: np.ndarray, alpha: float, dt: float, dx: float) -> np.ndarray:
    """Residual of u_t = alpha * u_xx at interior points."""
    if len(u_now) != len(u_next): raise ValueError("states must have equal length")
    return (u_next[1:-1] - u_now[1:-1]) / dt - alpha * laplacian_1d(u_now, dx)
