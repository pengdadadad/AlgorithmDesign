from Ourtimer.ourtimer import calculate_time
import matplotlib.pyplot as plt
F0 = 0
F1 = 1
my_list = [0] * 100
my_list1 = [0] * 100


# 递归算法
def gen_fibonacci(num):
    if num == 0:
        my_list[num] = F0
        return F0
    if num == 1:
        my_list[num] = F1
        return F1
    ret = gen_fibonacci(num - 1) + gen_fibonacci(num - 2)
    if my_list[num] == 0:
        my_list[num] = ret
    return ret


# 非递归算法
def gen_fibonacci1(num):
    my_list1[0] = F0
    my_list1[1] = F1
    for i in range(2, num):
        my_list1[i] = my_list1[i-1] + my_list1[i-2]


time1 = []
x1 = []
for i in range(35):
    x1.append(i)
    time1.append(calculate_time(gen_fibonacci, i))

time2 = []
x2 = []
for i in range(35):
    x2.append(i)
    time2.append(calculate_time(gen_fibonacci1, i))

plt.plot(x1, time1, x2, time2)
plt.show()
