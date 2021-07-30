import numpy as np


def mse(img1: np.ndarray, img2: np.ndarray) -> float:
    height, width, dim = img1.shape
    return ((img1 - img2) ** 2 / (height * width * dim)).sum()
