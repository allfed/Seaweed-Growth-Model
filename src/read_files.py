def create_lognormal_distribution():
    """
    Creates a log-normal distribution between 1 and 100
    and returns it as a pandas dataframe
    """
    import numpy as np
    import pandas as pd
    return pd.DataFrame(np.random.lognormal(0, 1, 100), columns=['value'])

print("blah") 

