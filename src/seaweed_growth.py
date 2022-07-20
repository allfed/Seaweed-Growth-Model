"""
Contains all functions needed to calculate the growth of
seaweed. Based on the publication:
James, S.C. and Boriah, V. (2010), Modeling algae growth
in an open-channel raceway
Journal of Computational Biology, 17(7), 895−906.
"""
import math


def growth_factor_combination(opt_growth_rate, non_opt_illumniation, non_opt_temperature,
                            non_opt_nutrients, non_opt_salinity, self_shading=1):
    """
    Calculates the actual production rate of the seaweed
    Arguments:
        opt_growth_rate: the optimal growth rate of the algae
        non_opt_illumniation: the non-optimal illumination of the algae
        non_opt_temperature: the non-optimal temperature of the algae
        non_opt_nutrients: the non-optimal nutrients of the algae
        non_opt_salinity: the non-optimal salinity of the algae
        self_shading: the self-shading of the algae: default value 1, as we not always have
        information about the density of the algae
    Returns:
        The actual production rate of the algae
    """
    # Make sure all factors are between 0 and 1
    factors = [opt_growth_rate, non_opt_illumniation, non_opt_temperature, non_opt_nutrients, non_opt_salinity, self_shading]
    for factor in factors:
        assert 0 <= factor <= 1
    # Calculate the actual production rate
    return opt_growth_rate * non_opt_illumniation * non_opt_temperature * \
           non_opt_nutrients * non_opt_salinity * self_shading


def calculate_illumination_factor(illumination):
    """
    Calculates the illumination factor
    Arguments:
        illumination: the illumination of the algae in W/m²
    Returns:
        The illumination factor
    """
    if illumination < 21.9:
        return illumination / 21.9
    elif illumination > 100:
        return 100 / illumination
    else:
        return 1


def calculate_temperature_factor(temperature):
    """
    Calculates the temperature factor
    Arguments:
        temperature: the temperature of the water in °C
    Returns:
        The temperature factor
    """
    # where Kt1 = 0.017°C−2 and Kt2 = 0.06°C−2. These coefficients were determined by 
    # fitting the preceding equation such that g(15°C) = 0.25 and g(36°C) = 0.1
    Kt1 = 0.017
    Kt2 = 0.06

    if temperature < 24:
        return math.exp(-Kt1 * (24 - temperature)**2)
    elif temperature > 30:
        return math.exp(-Kt2 * (temperature - 30)**2)
    else:
        return 1

def calculate_nutrient_factor(nitrate, ammonium, phosphate):
    """
    Calculates the nutrient factor, which is the minimum of the three nutrients
    Arguments:
        nitrate: the nitrate concentration in mg/L
        ammonium: the ammonium concentration in mg/L
        phosphate: the phosphate concentration in mg/L
    Returns:
        The nutrient factor
    """
    # where KNO3 = 0.4 μM, KNH4 = 0.3 μM, and KPO4 = 0.1 μM.
    # were implemented because these yield growth rates consistent with  observations by Lapointe [1987]
    # "Phosphorus- and nitrogen-limited photosynthesis and growth of Gracilaria tikvahiae (Rhodophyceae)
    # in the Florida Keys: an experimental field study"
    KNO3 = 0.4
    KNH4 = 0.3
    KPO4 = 0.1
    # Calculate the single nutrient factors
    nitrate_factor = nitrate / (KNO3 + nitrate)
    ammonium_factor = ammonium / (KNH4 + ammonium)
    phosphate_factor = phosphate / (KPO4 + phosphate)
    # Calculate the nutrient factor
    return min(nitrate_factor, ammonium_factor, phosphate_factor)


def calculate_salinity_factor(salinity):
    """
    Calculates the salinity factor
    Arguments:
        salinity: the salinity of the water in ppt
    Returns:
        The salinity factor
    """
    # with  = 0.007 ppt−2 and = 0.063 ppt−2.
    kS1 = 0.007
    kS2 = 0.063
    if salinity < 24:
        return math.exp(-kS1 * (24 - salinity)**2)
    elif salinity > 36:
        return math.exp(-kS2 * (salinity - 36)**2)
    else:
        return 1


def calculate_self_shading_factor(density):
    """
    Calculates the self-shading factor
    Arguments:
        density: the density (kg/m2) of the algae
    Returns:
        The self-shading factor
    """
    if density >= 0.4:
        return math.exp(-0.513 * (density - 0.4))
    else:
        return 1
