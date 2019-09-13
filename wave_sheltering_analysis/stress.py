import numpy as np

VISCOSITY_AIR = 1.56e-5
VISCOSITY_WATER = 0.9E-6
VON_KARMAN = 0.4


def drag_coefficient(ustar: float, U: float) -> float:
    """Returns the drag coefficient given input 
    friction velocity ustar and wind speed U."""
    return (ustar / U)**2


def friction_velocity_smooth(Uz: float, z: float) -> (float, float):
    """Returns the friction velocity given input wind speed 
    and height, assuming smooth law of the wall."""
    ALPHA = 0.132
    z0 = 1e-3
    for n in range(20):
        ustar = VON_KARMAN * Uz / np.log(z / z0)
        z0 = ALPHA * VISCOSITY_AIR / ustar
    return ustar


def wind_speed_at_reference_height(Uz: float, z: float, ustar: float, 
    zref: float) -> float:
    """Scales input wind speed Uz at height z to reference 
    height zref given friction velocity ustar."""
    return Uz + ustar / VON_KARMAN * np.log(zref / z)
