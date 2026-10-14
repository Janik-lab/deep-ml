import numpy as np
def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]

    """
    x = np.array(x)

    x_min = np.min(x)
    x_max = np.max(x)

    x_normalized = (x - x_min) / (x_max - x_min)
    # Your code here
    return x_normalized