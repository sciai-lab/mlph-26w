"""Load the CT scan and generate its design matrix on first use.

Each entry of the matrix is the exact path length of one ray through one
pixel. The generated array stays local in data/.
"""
from pathlib import Path

import numpy as np


IMAGE_SHAPE = (99, 117)
SINOGRAM_SHAPE = (30, 155)
DATA_DIR = Path(__file__).resolve().parent / "data"


def path_lengths(centers, origin, direction):
    """Return the length of a straight ray inside each unit-square pixel."""
    enter = np.full(centers.shape[0], -np.inf)
    leave = np.full(centers.shape[0], np.inf)
    for axis in range(2):
        if abs(direction[axis]) < 1e-12:
            # The ray is parallel to this axis: it stays either inside or outside.
            leave[np.abs(centers[:, axis] - origin[axis]) > 0.5] = -np.inf
            continue
        first = (centers[:, axis] - 0.5 - origin[axis]) / direction[axis]
        second = (centers[:, axis] + 0.5 - origin[axis]) / direction[axis]
        enter = np.maximum(enter, np.minimum(first, second))
        leave = np.minimum(leave, np.maximum(first, second))
    return np.maximum(leave - enter, 0.0)


def make_design_matrix():
    """Return the pixels-by-rays design matrix as float64."""
    rows, columns = IMAGE_SHAPE
    angle_count, detector_count = SINOGRAM_SHAPE
    x, y = np.meshgrid(np.arange(columns) - (columns - 1) / 2,
                       np.arange(rows) - (rows - 1) / 2)
    centers = np.stack([x.ravel(), y.ravel()], axis=-1)
    angles = np.linspace(0, np.pi, angle_count, endpoint=False) + np.pi / angle_count
    offsets = np.arange(detector_count) - (detector_count - 1) / 2
    matrix = np.empty((rows * columns, angle_count * detector_count), dtype=np.float64)
    for a, angle in enumerate(angles):
        direction = np.array([np.cos(angle), -np.sin(angle)])
        normal = np.array([np.sin(angle), np.cos(angle)])
        for d, offset in enumerate(offsets):
            matrix[:, a * detector_count + d] = path_lengths(centers, offset * normal, direction)
    return matrix


def load_ct_data():
    """Return X (11583, 4650) and the flattened noisy measurements y (4650,)."""
    cache = DATA_DIR / "design_matrix.npy"
    if not cache.exists():
        np.save(cache, make_design_matrix())
    matrix = np.load(cache, mmap_mode="r")
    measurements = np.load(DATA_DIR / "sino.npy").reshape(-1)
    expected = (np.prod(IMAGE_SHAPE), np.prod(SINOGRAM_SHAPE))
    if matrix.shape != expected or measurements.shape != (expected[1],):
        raise ValueError("CT files do not match the expected image and sinogram dimensions")
    return matrix, measurements


if __name__ == "__main__":
    X, y = load_ct_data()
    print(f"Image: {IMAGE_SHAPE}; sinogram: {SINOGRAM_SHAPE}; X: {X.shape}; y: {y.shape}")
