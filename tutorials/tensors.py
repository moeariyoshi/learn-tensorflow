#!/usr/bin/env python3
"""
Tensorflow Tensor Tutorial
"""

import torch
import numpy as np

if __name__ == "__main__":

    # Initializing tensors

    ## From data
    data = [[1, 2],[3, 4]]
    x_data = torch.tensor(data)

    ## From NumPy Array
    np_array = np.array(data)
    x_np = torch.from_numpy(np_array)

    ## From other tensors
    x_ones = torch.ones_like(x_data) # retains the properties of x_data
    print(f"Ones Tensor: \n {x_ones} \n")

    x_rand = torch.rand_like(x_data, dtype=torch.float) # overrides the datatype of x_data
    print(f"Random Tensor: \n {x_rand} \n")

    ## From different values with some shape 
    shape = (2,3,)
    rand_tensor = torch.rand(shape)
    ones_tensor = torch.ones(shape)
    zeros_tensor = torch.zeros(shape)

    print(f"Random Tensor: \n {rand_tensor} \n")
    print(f"Ones Tensor: \n {ones_tensor} \n")
    print(f"Zeros Tensor: \n {zeros_tensor}")

    # Attributes

    tensor = torch.rand(3,4)

    print(f"Shape of tensor: {tensor.shape}")
    print(f"Datatype of tensor: {tensor.dtype}")
    print(f"Device tensor is stored on: {tensor.device}")
