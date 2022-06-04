import timeit

import torch

gpu_device = "mps"
dtype = torch.float
number = 10
size = 8192
cpumat = torch.randn(size,size,dtype=dtype)
gpumat = cpumat.to(gpu_device)

cpu_time = timeit.timeit("torch.matmul(cpumat,cpumat)",number=number,globals=globals())
print("cpu_time: {:.6f} seconds".format(cpu_time))
gpu_time = timeit.timeit("torch.matmul(gpumat,gpumat)",number=number,globals=globals())
print("gpu_time: {: .6f} seconds".format(gpu_time))
