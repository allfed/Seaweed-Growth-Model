"""
Main file that ties the other ones together.
"""
class Ocean_Section():
    """
    Class the represents a section of the ocean.
    alculates for every section how quickly seaweed can grow
    and also saves the single factors for growth
    """
    def __init__(self):
        self.salinity_factor = None
        self.nutrient_factor = None
        self.illumination_factor = None
        self.self_shading_factor = None
        self.temp_factor = None
        self.seaweed_growth_rate = None
        