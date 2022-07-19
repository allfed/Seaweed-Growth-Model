"""
Contains all functions needed to calculate the growth of
seaweed. Based on the publication:
James, S.C. and Boriah, V. (2010), Modeling algae growth
in an open-channel raceway
Journal of Computational Biology, 17(7), 895−906.
"""
def growth_factor_combination(opt_growth_rate, non_opt_illumniation, non_opt_temperature,
                            non_opt_nutrients, non_opt_salinity, self_shading):
    """
    Calculates the actual production rate of the seaweed
    Arguments:
        opt_growth_rate: the optimal growth rate of the algae
        non_opt_illumniation: the non-optimal illumination of the algae
        non_opt_temperature: the non-optimal temperature of the algae
        non_opt_nutrients: the non-optimal nutrients of the algae
        non_opt_salinity: the non-optimal salinity of the algae
        self_shading: the self-shading of the algae
    Returns:
        The actual production rate of the algae
    """
    return opt_growth_rate * non_opt_illumniation * - non_opt_temperature * \
           non_opt_nutrients * non_opt_salinity * self_shading


