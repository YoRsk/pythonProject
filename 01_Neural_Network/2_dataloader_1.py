
import matplotlib.pyplot as plt

import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

def eg_1_2_0():
    from torchvision.datasets.mnist import MNIST
    train_dataset = MNIST(root="./mnist_data",
                          train=True,
                          transform=None,
                          download=False)

    plt.imshow(train_dataset[0][0], cmap='gray')
    plt.show()


eg_1_2_0()
