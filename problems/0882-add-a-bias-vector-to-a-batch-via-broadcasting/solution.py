import torch

def add_bias(x: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
    # TODO: add b to every row of x using broadcasting
    new_Tensor_with_bias = x + b

    return new_Tensor_with_bias

