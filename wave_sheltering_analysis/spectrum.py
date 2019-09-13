import numpy as np


def jonswap_peak_frequency(U10: float, fetch: float, grav: float) -> float:
    """Returns the JONSWAP equilibrium peak frequency in Hz, 
    given input wind speed at 10-m height (m/s), fetch (m), 
    and gravitational acceleration (m/s**2)."""
    return 3.5 * (grav**2 / (U10 * fetch))**(1. / 3)


def jonswap(f: float, U10: float, fetch: float, grav: float) -> float:
    """Returns the JONSWAP spectrum (m**2/Hz) given input frequency (Hz), 
    wind speed at 10-m height U10 (m/s), fetch (m), and gravitational acceleration."""
    BETA = -1.25
    GAMMA = 3.3 # peak enhancement

    omega = 2 * np.pi * f
    alpha = 0.076 * nondimensional_fetch(U10, fetch, grav)**(-0.22)
    f_peak = jonswap_peak_frequency(U10, fetch, grav)

    if type(f) is np.ndarray:
        sigma = 0.07 * np.ones(f.size)
        sigma[f > f_peak] = 0.09
    else: 
        sigma = 0.09 if f > f_peak else 0.07

    r = np.exp(-0.5 * ((f - f_peak) / (sigma * f_peak))**2)

    return 2 * np.pi * alpha * grav**2 / omega**5 \ 
        * np.exp(BETA * (f_peak / f)**4) * GAMMA**r


def nondimensional_fetch(U, fetch, grav):
    """Returns non-dimensional fetch based on input wind speed U (m/s), 
    fetch (m), and gravitational acceleration (m/s**2)."""
    return grav * fetch / U**2
