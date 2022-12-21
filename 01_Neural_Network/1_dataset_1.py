import os
import torch

# print("torch_version is:{}".format(torch.__version__))

from torch.utils.data import Dataset
from torch.utils.data import Sampler


def eg_1_1():
    x = torch.linspace(-1, 1, 10)
    y = x ** 2

    class SimpleDataset(Dataset):
        def __init__(self, x, y):
            super().__init__()
            self.x = x
            self.y = y

        def __getitem__(self, index):
            return {"x": self.x[index], "y": self.y[index]}

        def __len__(self):
            return len(self.x)

    simpledataset = SimpleDataset(x, y)
    index = 0
    # __getitem__
    print("simpledataset.__getitem__({}): {}".format(index, simpledataset.__getitem__(index)))
    print("simpledataset[{}]: {}".format(index, simpledataset[index]))
    # __len__
    print("simpledataset.__len__):{}".format(simpledataset.__len__()))
    print("len(simpledataset):{}".format(len(simpledataset)))


def eg_1_2_0():
    import matplotlib.pyplot as plt

    import os
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
    from torchvision.datasets.mnist import MNIST
    train_dataset = MNIST(root="./mnist_data",
                          train=True,
                          transform=None,
                          download=False)

    plt.imshow(train_dataset[0][0], cmap='gray')
    plt.show()


eg_1_2_0()
eg_1_1()
