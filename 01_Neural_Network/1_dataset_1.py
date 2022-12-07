
import os
import torch

# print("torch_version is:{}".format(torch.__version__))

from torch.utils.data import Dataset
from torch.utils.data import Sampler

def eg_1_1():

    x = torch.linspace(-1, 1, 10)
    y = x**2

    class SimpleDataset(Dataset):
        def __init__(self, x, y):
            super().__init__()
            self.x = x
            self.y = y

        def __getitem__(self, index1):
            return {"x": self.x[index1], "y": self.y[index1]}

        def __len__(self):
            return len(self.x)

    simpledataset = SimpleDataset(x, y)
    index = 1
    # __getitem__
    print("simpledataset.__getitem__({}): {}".format(index, simpledataset.__getitem__(index)))
    print("simpledataset[{}]: {}".format(index, simpledataset[index]))
    # __len__
    print("simpledataset.__len__):{}".format(index, simpledataset.__len__()))
    print("len(simpledataset):{}".format(len(simpledataset)))

eg_1_1()