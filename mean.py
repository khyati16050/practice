import numpy as npy

n = int(input("Enter the number of elements"))
lst = []
for i in range(n):
    num = int(input())
    lst.append(num)
new_lst = npy.array(lst)
# print(new_lst)
mean = npy.mean(new_lst)
med = npy.median(new_lst)
variance = npy.var(new_lst)
stdev = npy.std(new_lst)
print(mean,med,variance,stdev)