import torch

def grad_of_quadratic(x_value: float) -> float:
    # TODO: build a tracked leaf for x, compute f(x), run backprop, return df/dx as a float
    x = torch.tensor(x_value, dtype = float , requires_grad=True)

    y = x**2 + 3*x +2 

    y.backward()

    final_grad = x.grad.item()

    return final_grad

    


