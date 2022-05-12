from torch import nn

model = nn.Conv2d(3, 16, 1)
print(isinstance(model, nn.Conv2d))     # True
print(type(model) == nn.Conv2d)         # True
