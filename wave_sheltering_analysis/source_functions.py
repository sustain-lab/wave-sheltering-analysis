import numpy as np
from wave_sheltering_analysis.stress import wind_speed_at_reference_height
from wave_sheltering_analysis.wave_quantities import angular_frequency, 
    group_speed, phase_speed


def wind_input_source_function(Uz, z, f, k, Ff, rhoa, rhow, sheltering):
    """
    Wind input function by Donelan et al. (2012).
    This version is for frequency spectrum (F(f)) 
    of waves in direction of wind.

    Uz: Wind speed at height z (m/s)
    z: Height (m)
    f: Frequency (Hz)
    k: Wavenumber (rad / m**2)
    Ff: Frequency spectrum F(f) (m**2/Hz)
    rhoa: Air density (kg/m**3)
    rhow: Water density (kg/m**3)
    sheltering: A non-dimensional sheltering coefficient
    """
    omega = angular_frequency(f)
    wavelength = 2 * np.pi / k
    Cp = phase_speed(omega, k)
    Cg = group_speed(omega, k)

    input_height = wavelength / 2
    input_height[input_height > 10] = 10
    Uin = wind_speed_at_reference_height(Uz, z, ustar, input_height)
    Urel = Uin - Cp

    return sheltering * np.abs(Urel) * Urel * rhoa / rhow * omega * k / grav / Cg * Ff
