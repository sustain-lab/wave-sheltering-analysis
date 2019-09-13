import numpy as np


def angular_frequency(f):
    return 2 * np.pi * f


def group_speed(omega, k):
    Cg = np.zeros(omega.size)
    Cg[1:] = np.diff(omega) / np.diff(k)
    Cg[0] = Cg[1]
    return Cg


def phase_speed(omega, k):
    return omega / k
