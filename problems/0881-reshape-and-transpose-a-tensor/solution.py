import torch
import math

def flatten_then_reshape(x: torch.Tensor, new_shape) -> torch.Tensor:
    # TODO: flatten x to 1-D, then rearrange into new_shape
    number_of_elements = x.numel()
    new_number_of_elements = math.prod(new_shape)
    x = torch.flatten(x)

    if number_of_elements == new_number_of_elements:
        reshaped_tensor = x.reshape(new_shape)
    else:
        raise ValueError("Number of elements must stay the same")

    return reshaped_tensor

def transpose_last_two(x: torch.Tensor) -> torch.Tensor:
    # TODO: swap the last two dimensions of x
    transposed_x = x.transpose(-2, -1)
    return transposed_x

    
