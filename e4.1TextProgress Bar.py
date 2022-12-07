# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import time
scale = 10
print("--------start--------")
for i in range(scale + 1):
    a, b = '**' * i, '--' * (scale - i)
    c = (i/scale)*100
    print("{:^3.0f}%[{}->{}]".format(c, a, b))
    time.sleep(0.1)
print("-------- end --------")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
