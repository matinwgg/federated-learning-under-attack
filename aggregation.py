from __future__ import annotations
import numpy as np

def fedavg(updates: list[np.ndarray], weights: list[float] | None = None) -> np.ndarray:
    if not updates: raise ValueError('at least one update is required')
    shape = updates[0].shape
    if any(u.shape != shape for u in updates): raise ValueError('shape mismatch')
    if weights is None: weights = [1.0] * len(updates)
    if len(weights) != len(updates) or sum(weights) <= 0: raise ValueError('invalid weights')
    return sum((u*w for u,w in zip(updates,weights)), np.zeros(shape)) / sum(weights)

def coordinate_median(updates: list[np.ndarray]) -> np.ndarray:
    if not updates: raise ValueError('at least one update is required')
    return np.median(np.stack(updates), axis=0)

def clip(update: np.ndarray, max_norm: float) -> np.ndarray:
    if max_norm <= 0: raise ValueError('max_norm must be positive')
    norm = np.linalg.norm(update)
    return update if norm <= max_norm else update * (max_norm / norm)
