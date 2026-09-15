import torch
import torch.nn as nn

a = nn.Parameter(torch.ones(512))
bias = nn.Parameter(torch.zeros(512))
eps=1e-6
x = torch.normal(mean=5, std=3.56, size=(512,))
mean = x.mean()
avg = (x - mean)
std = x.std()
z = a * (x - mean) / (std + eps) + bias
z.std()
#
assert torch.isclose(z.var(), (z.std()**2), atol=1e-8)
assert torch.isclose(z.mean(), torch.tensor(0.0), atol=1e-6)
assert torch.isclose(z.std(), torch.tensor(1.0), atol=1e-6)
#
print(f"z.mean = {z.mean(-1)}")
print(f"z.std = {z.std(-1)}")
